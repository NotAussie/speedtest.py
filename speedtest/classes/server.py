class Server:
    def __init__(self, result: dict) -> None:
        self.__raw__ = result

    @property
    def id(self) -> int:
        """The ID of the Speedtest instance"""
        return self.__raw__["id"]

    @property
    def hostname(self) -> str:
        """The hostname of the Speedtest instance"""
        return self.__raw__["host"]

    @property
    def port(self) -> int:
        """The port of the Speedtest instance"""
        return self.__raw__["port"]

    @property
    def name(self) -> str:
        """The name of the Speedtest instance"""
        return self.__raw__["name"]

    @property
    def location(self) -> str:
        """The location of the Speedtest instance

        This is a general location like the city of the instance.
        """
        return self.__raw__["location"]

    @property
    def country(self) -> str:
        """The country of the Speedtest instance"""
        return self.__raw__["country"]
