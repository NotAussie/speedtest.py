class Server:
    def __init__(self, result: dict) -> None:
        self.__raw__ = result

    @property
    def id(self) -> int:
        """The ID of the Speedtest instance"""

        # Get the ID from __raw__
        serverID = self.__raw__["id"]

        return serverID

    @property
    def hostname(self) -> str:
        """The hostname of the Speedtest instance"""

        # Get the host from __raw__
        serverHost = self.__raw__["host"]

        return serverHost

    @property
    def port(self) -> int:
        """The port of the Speedtest instance"""

        # Get the port from __raw__
        serverPort = self.__raw__["port"]

        return serverPort

    @property
    def name(self) -> str:
        """The name of the Speedtest instance"""

        # Get the name from __raw__
        serverName = self.__raw__["name"]

        return serverName

    @property
    def location(self) -> str:
        """The location of the Speedtest instance

        This is a general location like the city of the instance.
        """

        # Get the location from __raw__
        serverLocation = self.__raw__["location"]

        return serverLocation

    @property
    def country(self) -> str:
        """The country of the Speedtest instance"""

        # Get the country from __raw__
        serverCountry = self.__raw__["country"]

        return serverCountry


class Result:

    def __init__(self, result: dict) -> None:
        """A data class that contains a result response from the CLI

        This is the equivalent of the "result" type.
        """

        self.__raw__ = result
