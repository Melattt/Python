
def is_palindrome(s):
    a = s.lower()
    a = a.strip("?")
    a = a.strip("!")
    a = a.strip(".")
    a = a.replace(" ","")
    if a[::1]==a[::-1]:
        return True
    else:
        return False

#Program starts
m="Was it a rat I saw?"
f=is_palindrome(m)
print(f)
