import re

def decode_message(s: str, p: str) -> bool:
    p = p.replace("?", ".").replace("*", ".*")
    return bool(re.fullmatch(p, s))
