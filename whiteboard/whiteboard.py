# Given a string of letters, write a function to see if the word  (case insensitive) is a palindrome (the same word spelled forward and backwards).
# The given string will contain only letters 
# Examples:
# is_palindrome("RaceCar") \\ => True
# is_palindrome("mom")  \\ => True
# is_palindrome("Shoha") \\ => False

# assuming that all incoming strings can be changed to lowercase

# Take in a string, s
# change it to lowercase, s = s.lower()
# if the string is the same forward and backwards (if == statement) => True
# if not the same => False

# maybe still can use the .reverse() method if I turn my string into a list????


# reversing a string
#   slice from -1
#   .reverse()



def solution(s):
    s = s.lower()
    return s == s[::-1]

# def solution(s):
#     s = s.lower()
#     temp = list(s)
#     temp.reverse()
#     temp = ''.join(temp)
#     return s == temp

