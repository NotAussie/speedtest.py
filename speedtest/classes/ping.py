class Ping:
    def __init__(self, data: dict) -> None:
        self.__raw__ = data

    @property
    def low(self) -> float:
        """The lowest amount of latency of the connection"""
        return self.__raw__["low"]

    @property
    def high(self) -> float:
        """The highest amount of latency of the connection"""
        return self.__raw__["high"]

    @property
    def jitter(self) -> float:
        """The jitter of the connection"""
        return self.__raw__["jitter"]

    @property
    def latency(self) -> float:
        """The latency of the connection"""
        return self.__raw__["latency"]
