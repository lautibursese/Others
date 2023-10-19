import pyttsx3  # Text-to-speech library

# Open the book text file
book = open(r"book.txt")

# Read the lines from the book text file
book_text = book.readlines()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Iterate through the lines in the book and read them out loud
for i in book_text:
    engine.say(i)
    engine.runAndWait( )
