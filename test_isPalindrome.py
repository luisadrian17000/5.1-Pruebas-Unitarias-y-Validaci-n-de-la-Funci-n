def is_palindrome(s: str) -> bool:

    if s == "":
        return None


    i = 0
    j = len(s) - 1

    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    
    
    return True 



def test_string():
    assert is_palindrome("aeiouoiea") == True
    

def test_empty_string():
    assert is_palindrome("") is None


def test_palindrome_number():
    assert is_palindrome("0000") == True



def test_is_not_palindrome_number():
    assert is_palindrome("8548745237984598494392022") == False


def test_is_not_palindrome_string():
    assert is_palindrome("asdfkjhajksbcbyedbfala") == False


def test_solo_dos_caracteres():
    assert is_palindrome("ab") == False
    









