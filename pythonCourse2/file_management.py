from io import open

text_file = open("file.txt", "w")

phrase = "Today is a good day for learning Python \nToday is sunday."

text_file.write(phrase)
text_file.close()
