# Take the following Python code that stores a string (parsing a string):

# str = 'X-DSPAM-Confidence:0.8475'

# Use find and string slicing to extract the portion of the string after the colon character and then
# use the float function to convert the extracted string into a floating point number. [define str, use
# str.find]

text = 'X-DSPAM-Confidence:0.8475'

colon_pos = text.find(':')  # Find the position of the colon
number_str = text[colon_pos + 1:]  # Slice from just after the colon to the end
number = float(number_str)  # Convert to float

print(number)
