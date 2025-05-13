# This file demonstrates three different approaches to extract and convert a floating-point number
# from a string containing "X-DSPAM-Confidence" data.

# Approach 1: Using find() to locate the starting position of the number
# text = "X-DSPAM-Confidence:    0.8475"
# pos = text.find("0")  # Find the position where the number starts
# print(pos)  # Print the position (should be 23)
# num = text[pos:pos+6]  # Extract 6 characters starting from the found position
# print(float(num))  # Convert the extracted string to float and print

# Approach 2: Directly finding the exact number in the string
# text = "X-DSPAM-Confidence:    0.8475"
# num = text.find("0.8475")  # Find the exact position of the number
# print(float(text[num:num+6]))  # Extract and convert the number in one step

# Approach 3: Dr. Chuck's solution - More robust approach
# text = "X-DSPAM-Confidence:    0.8475"
# ipos = text.find(":")  # Find the position of the colon
# # print(ipos)  # Print the position of the colon (should be 18)
# peice = text[ipos+1:]  # Get everything after the colon
# # print(peice)  # Print the extracted string (should be "    0.8475")
# value = float(peice)  # Convert the string to float (handles whitespace automatically)
# print(value)  # Print the final float value