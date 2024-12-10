# pyre-strict

r"""This package adds support for device memory management implemented in MTIA."""

from typing import Any, Dict, Optional

import torch

from . import _device_t, is_initialized
from ._utils import _get_device_index


def memory_stats(device: Optional[_device_t] = None) -> Dict[str, Any]:
    r"""Return a dictionary of MTIA memory allocator statistics for a given device.

    Args:
        device (torch.device, str, or int, optional) selected device. Returns
            statistics for the current device, given by current_device(),
            if device is None (default).
    """
    if not is_initialized():
        return {}
    return torch._C._mtia_memoryStats(_get_device_index(device, optional=True))


__all__ = [
    "memory_stats",
]