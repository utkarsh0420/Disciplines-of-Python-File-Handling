string = input("Enter a string :")
rev = ""
for ch in string:
    rev = ch + rev
if rev==string:
    print("It is palindrome")
else:
    print("It is not palindrome")