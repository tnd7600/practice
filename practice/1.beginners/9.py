# Check if the given number is palindrome or not


def pelindrome(num):
    print(f"Number is {num}")
    if str(num) == str(num)[::-1]:
        return "Yes. given number is palindrome number"
    return "No. given number is not palindrome number"

a = int(input("Enter a number: "))
print(pelindrome(a))
