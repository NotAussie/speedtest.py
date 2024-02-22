from .latency import Latency


class Download:
    def __init__(self, data: dict) -> None:
        self.__raw__ = data

        # Create object
        self.__latency__ = Latency(self.__raw__["latency"])

    @property
    def bandwidth(self) -> int:
        """The download bandwidth"""
        return self.__raw__["bandwidth"]

    @property
    def elapsed(self) -> int:
        """The time the download took"""
        return self.__raw__["elapsed"]

    @property
    def bytes(self) -> int:
        """The amount of bytes sent"""
        return self.__raw__["bytes"]

    @property
    def latency(self) -> Latency:
        """The latency of the download"""
        return self.__latency__
