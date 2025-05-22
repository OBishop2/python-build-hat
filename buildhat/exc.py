"""Exceptions for all build HAT classes"""

class MotorError(Exception):
    """Error raised when invalid arguments passed to motor functions"""


class BuildHATError(Exception):
    """Error raised when HAT not found"""


class DeviceError(Exception):
    """Error raised when there is a Device issue"""
