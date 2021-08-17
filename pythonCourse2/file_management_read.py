from io import open

text_file = open("file.txt", "r")

#text = text_file.read()
line_text = text_file.readlines()
text_file.close()
#print(text)
print(line_text)
print(line_text[0])
print(line_text[1])
