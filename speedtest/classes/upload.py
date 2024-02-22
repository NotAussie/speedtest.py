from .latency import Latency


class Upload:
    def __init__(self, data: dict) -> None:
        self.__raw__ = data

        # Create object
        self.__latency__ = Latency(self.__raw__["latency"])

    @property
    def bandwidth(self) -> int:
        """The upload bandwidth"""
        return self.__raw__["bandwidth"]

    @property
    def latency(self) -> Latency:
        """The latency of the upload"""
        return self.__latency__

    @property
    def elapsed(self) -> int:
        """The time the upload took"""
        return self.__raw__["elapsed"]

    @property
    def bytes(self) -> int:
        """The amount of bytes sent"""
        return self.__raw__["bytes"]
