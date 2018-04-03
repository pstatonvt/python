'''
6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. Convert the extracted value to a floating point number and print it out.
'''

text = "X-DSPAM-Confidence:    0.8475";
text.find(":")
tmp = text[19:29]
tmp = float(tmp)

print(tmp)

'''
You should use the find function to get the position of the colon in the string.
'''
