def check_email(string):
    if " " in string:
        return False
    if "@" not in string:
        return False
    if "@." in string:
        return False
    if "." in string[string.find("@"):]:
        return True
    else:
        return False
