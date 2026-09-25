CHARS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def to_base62(num: int) -> str:
    if num == 0:
        return CHARS[0]

    result = []

    while num > 0:
        result.append(CHARS[num % 62])
        num //= 62

    return "".join(reversed(result))