# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
# Copyright 2024-2026 Arm Limited and/or its affiliates.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

from typing import Set, Type

import torch

from executorch.backends.arm._passes import ArmOpTargetedPass
from executorch.backends.arm._passes.convert_squeezes_to_view import (
    ConvertSqueezesToViewPass,
)
from executorch.backends.arm._passes.rewrite_conv_pass import RewriteConvPass
from executorch.backends.arm._passes.size_adjust_input_pass import SizeAdjustInputPass
from executorch.backends.transforms.convert_conv1d_to_conv2d_pass import (
    ConvertConv1dToConv2dPass,
)
from executorch.exir.dialects._ops import ops as exir_ops
from executorch.exir.pass_base import ExportPass


class Conv1dUnsqueezePass(ConvertConv1dToConv2dPass, ArmOpTargetedPass):
    """Convert ConvTranspose1d into ConvTranspose2d.

    Forward Conv1d is lowered atomically by ``RewriteConvPass`` so its layout
    transforms can be emitted in the rank-3 domain. TOSA has no native
    transpose-convolution 1D operator, so this pass retains the rank-4
    expansion for ConvTranspose1d.

    """

    _passes_required_after: Set[Type[ExportPass]] = {
        ConvertSqueezesToViewPass,
        RewriteConvPass,
        SizeAdjustInputPass,
    }
    target_ops = (exir_ops.edge.aten.convolution.default,)

    def _conv1d_weight_node(self, node: torch.fx.Node) -> torch.fx.Node | None:
        weight_node = super()._conv1d_weight_node(node)
        # A non-None weight node means the base pass matched the full nine-arg
        # convolution signature, so args[6] (transposed) is always present.
        if weight_node is None or not node.args[6]:
            return None
        return weight_node
