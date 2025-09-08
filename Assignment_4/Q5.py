# Using an appropriate example of a string demonstrate the use of “strip” and “replace”.

# Example string with spaces and unwanted characters
text = "   ***Hello World!!!***   "

# 1. strip(): remove leading and trailing characters (default: spaces/newlines)
cleaned = text.strip()  
print("After strip():", repr(cleaned))
# print("After strip():", str(cleaned))
# print("After strip():", (cleaned))

# strip() can also remove specific characters from both ends
cleaned_chars = text.strip(" *!")  
print("After strip(' *!'):", repr(cleaned_chars))

# 2. replace(): replace all occurrences of̃̃ a substring with another
replaced = cleaned_chars.replace("World", "Python")
print("After replace():", replaced)
