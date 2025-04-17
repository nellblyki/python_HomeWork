#Implement String#digit? (in Java StringUtils.isDigit(String)), which should return true if given object is a single digit (0-9), false otherwise.
def is_digit(string):
    if not isinstance(string, str) or len(string) != 1:
        return False
    return string.isdigit() 
