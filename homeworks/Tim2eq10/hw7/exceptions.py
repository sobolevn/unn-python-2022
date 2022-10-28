class BaseParseError(Exception):
    pass


class GetIdError(BaseParseError):
    """I use it when we can't find id for current email"""
    pass
