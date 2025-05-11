def validate(s : str) -> bool:
    while s:
        oldLength : int = len(s)
        if "()" in s:
            s = s.replace('()', "")
        if "{}" in s:
            s = s.replace('{}', "")
        if '[]' in s:
            s = s.replace('[]', "")
        if oldLength == len(s):
            return False
    return True

# def isPair(b1 : str, b2 : str) -> bool:
#     if (b1 == '(' and b2 == ")"):
#         return True
#     if (b1 == '[' and b2 == "]"):
#         return True
#     if (b1 == '{' and b2 == "}"):
#         return True
#     return False

# def isClosingBracket(s : str) -> bool:
#     if (s in ["}", "]", ")"]):
#         return True