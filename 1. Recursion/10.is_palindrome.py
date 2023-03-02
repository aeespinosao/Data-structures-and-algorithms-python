def isPalindrome(strng):
    if len(strng) == 1:
        return True
    
    return strng[0]==strng[-1] and isPalindrome(strng[1:-1])

if __name__ == '__main__':
    print(isPalindrome('awesome')) # false
    print(isPalindrome('foobar')) # false
    print(isPalindrome('tacocat')) # true
    print(isPalindrome('amanaplanacanalpanama')) # true
    print(isPalindrome('amanaplanacanalpandemonium')) # false