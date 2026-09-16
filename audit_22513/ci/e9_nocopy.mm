// E9 — que fait newBufferWithBytesNoCopy (MLX: allocator.cpp:207-218, make_buffer) quand le
// pointeur n'est pas aligné page, ou quand la longueur n'est pas un multiple de page ?
// Apple documente « page-aligned pointer », longueur « that results in a page-aligned
// region », retour nil sinon. MLX passe nbytes() non arrondi (array.cpp:95).
//
// Compilation : clang++ -std=c++17 -ObjC++ -fobjc-arc -framework Metal -framework Foundation e9_nocopy.mm -o e9
#import <Foundation/Foundation.h>
#import <Metal/Metal.h>

#include <mach/mach.h>
#include <mach/vm_map.h>
#include <unistd.h>

#include <cstdio>
#include <cstdlib>

static void probe(id<MTLDevice> dev, void* p, size_t len, const char* label) {
  const size_t page = static_cast<size_t>(getpagesize());
  id<MTLBuffer> b = [dev newBufferWithBytesNoCopy:p
                                           length:len
                                          options:MTLResourceStorageModeShared
                                      deallocator:nil];
  printf("%-56s ptr%%page=%-6zu len%%page=%-6zu -> %s", label,
         static_cast<size_t>(reinterpret_cast<uintptr_t>(p) % page), len % page,
         b ? "buffer" : "nil");
  if (b) {
    printf("  contents==ptr:%s  length=%lu", [b contents] == p ? "yes" : "NO",
           static_cast<unsigned long>([b length]));
  }
  printf("\n");
}

int main() {
  @autoreleasepool {
    id<MTLDevice> dev = MTLCreateSystemDefaultDevice();
    if (!dev) {
      printf("no Metal device\n");
      return 1;
    }
    printf("device=%s architecture=%s page=%d recommendedMaxWorkingSetSize=%llu hasUnifiedMemory=%d\n",
           dev.name.UTF8String, dev.architecture.name.UTF8String, getpagesize(),
           dev.recommendedMaxWorkingSetSize, dev.hasUnifiedMemory ? 1 : 0);

    vm_address_t addr = 0;
    const size_t size = 1 << 20;
    if (vm_allocate(mach_task_self(), &addr, size, VM_FLAGS_ANYWHERE) != KERN_SUCCESS) {
      printf("vm_allocate failed\n");
      return 1;
    }
    char* p = reinterpret_cast<char*>(addr);
    probe(dev, p, size, "vm_allocate: ptr page-aligned, len page-multiple");
    probe(dev, p, size - 100, "vm_allocate: ptr page-aligned, len NOT page-multiple");
    probe(dev, p + 4096, size - 4096, "vm_allocate: ptr + 4096 (4 KiB, pas 16 KiB)");
    probe(dev, p + 128, size - 128, "vm_allocate: ptr + 128 (offset d'un segment .pte)");

    // Ce que FileDataLoader obtient : operator new(size, align_val_t(16)) -> posix_memalign.
    void* a = nullptr;
    if (posix_memalign(&a, 16, 1179648) == 0) {
      probe(dev, a, 1179648, "posix_memalign(16, 1179648 = 72 pages) q_proj bf16");
    }
    void* b = nullptr;
    if (posix_memalign(&b, 16, 2304000) == 0) {
      probe(dev, b, 2304000, "posix_memalign(16, 2304000) embed_positions bf16");
    }
    void* c = nullptr;
    if (posix_memalign(&c, 16, 1536) == 0) {
      probe(dev, c, 1536, "posix_memalign(16, 1536) biais (zone small)");
    }
    void* d = nullptr;
    if (posix_memalign(&d, 16, 20480) == 0) {
      probe(dev, d, 20480, "posix_memalign(16, 20480) > 15 KiB iOS, < 32 KiB macOS");
    }
  }
  return 0;
}
