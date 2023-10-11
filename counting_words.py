import string, sys          # importing the string module and sys module

#defining function to remove punctuation & convert into lower case to remove case sensitivity
def convert_and_casesensitive(text):
    text = text.translate(str.maketrans("","",string.punctuation))  # removing punctuation
    text = text.lower()           # convert all the text into lowercase to avoid case sensitivity
    words = text.split()
    return words

#defining function to count how many times each word appear in the full text document
def word_appear_count(words):
    word_count = {}            # creating an empty directory to store word count against each word
    for word in words:
        if word in word_count:
            word_count[word] += 1    # incrementing count value
        else:
            word_count[word] = 1
    return word_count

#defining a function to open a text file, read the file and count the total of number of appearance of each word
def open_text_file(filename):
    try:
        with open(filename, 'r', encoding="UTF-8") as file:
            text=file.read()             #read the full text and store it in the text variable
            words = convert_and_casesensitive(text)    # call the function to remove the punctuation and convert into lowercase
            word_count = word_appear_count(words)      # call the word_appear_count function to count the appearance of each word
            return word_count
    except FileNotFoundError:
        print(filename+" file does not exists in your system")              # show this message if the file not found
        sys.exit()                                                         # terminate the program

# Taking filename from user
fname=input("Please enter the filename: ")
appear=open_text_file(fname)
if appear:
    print("------------Appearance of each word is defined below------------")
    for word, count in appear.items():
        print(f"{word}: {count}")        # will print in dictionary format
else:
    print("The word file is blank")