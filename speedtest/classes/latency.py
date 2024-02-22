class Latency:
    def __init__(self, data: dict) -> None:
        self.__raw__ = data

    @property
    def iqm(self) -> float:
        """The IQM of the latency"""
        return self.__raw__["iqm"]

    @property
    def low(self) -> float:
        """The lowest point of the latency"""
        return self.__raw__["low"]

    @property
    def high(self) -> float:
        """The highest point of the latency"""
        return self.__raw__["high"]

    @property
    def jitter(self) -> float:
        """The jitter of the connection"""
        return self.__raw__["jitter"]
