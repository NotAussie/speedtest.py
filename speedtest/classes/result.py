class Result:
    def __init__(self, data: dict) -> None:
        self.__raw__ = data

    @property
    def id(self) -> str:
        return self.__raw__["id"]

    @property
    def url(self) -> str:
        return self.__raw__["url"]

    @property
    def image(self) -> str:
        return self.__raw__["url"] + ".png"

    @property
    def persisted(self) -> bool:
        return self.__raw__["persisted"]
