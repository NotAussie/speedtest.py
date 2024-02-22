class Interface:
    def __init__(self, data: dict) -> None:
        self.__raw__ = data

    @property
    def internalIp(self) -> str:
        """The internal IP of the interface"""

        # Get the internalIp from __raw__
        interfaceInternalIp = self.__raw__["internalIp"]

        return interfaceInternalIp

    @property
    def externalIp(self) -> str:
        """The external IP of the interface"""

        # Get the externalIp from __raw__
        interfaceExternalIp = self.__raw__["externalIp"]

        return interfaceExternalIp

    @property
    def name(self) -> str:
        """The name of the interface

        Most of the time is empty
        """

        # Get the name from __raw__
        interfaceName = self.__raw__["name"]

        return interfaceName

    @property
    def macAddr(self) -> str:
        """The MAC address of the interface"""

        # Get the MAC address from __raw__
        interfaceMacAddr = self.__raw__["macAddr"]

        return interfaceMacAddr

    @property
    def isVpn(self) -> bool:
        """Whether a VPN was used"""

        # Get the value from __raw__
        interfaceIsVpn = self.__raw__["isVpn"]

        return interfaceIsVpn
