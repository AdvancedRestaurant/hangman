def check_email(string):
    index1 = string.rfind("@")
    index2 = string.rfind(".")
    if(' ' in string) or ('@' not in string) or (index1 > index2) or (index2 == index1 + 1):
        return False
    else:
        return True