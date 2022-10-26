import re


def only(dictionary: dict, keys: list) -> dict:
    return {
        dict_value: dictionary[dict_value]
        for dict_value in dictionary
        if dict_value in keys
    }


def is_email(entry: str) -> bool:
    regex = re.compile(
        r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+',
    )
    return re.match(regex, entry) is not None
