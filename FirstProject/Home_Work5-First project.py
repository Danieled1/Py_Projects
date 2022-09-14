import string
import sys
# GLOBAL VARIABLES
LETTERS = []
TIMES = []


# Functions to return the first and second element in a tuple.
def take_1st(element):
    return element[0]


def take_2nd(element):
    return element[1]


# common_letters = returns the most 4 common chars in a string and get them into a dictionary of keys by the most common
# letters in english. {h:e.k:t,m:o,u:r...}
def common_letters(str1):
    str1 = str1.lower()
    comn_letters = []
    replaced_letters,temp = {}, {}      # 2 dictionaries to return the dictionary of keys to decrypt the string with.
    most_common = ["e","t","o","r"]     # a list of the most common letters in english
    for i in range(0,len(str1)):        # iterates over the string char by char and count the relevant chars
        if str1[i].isalpha():
            key = str1[i].lower()
            value = str1.count(str1[i])
            if value >= 4:              # skips the chars with count less than 4 to save time on running.
                letter = (key,value)
                comn_letters.append(letter)
            else:
                continue
        else:
            continue

    comn_letters = set(comn_letters)        # To remove duplicates
    comn_letters = list(comn_letters)       # to be able to use sort(), made it back to a list
    comn_letters.sort(key=take_2nd,reverse=True)
    for i in range(0,len(most_common)):     # loop to add the given chars into a dictionary of keys
        key = take_1st(comn_letters[i])     # The character
        value = most_common[i]          # The replacement for it ("E" "O" "T" "R")
        temp = {key:value}
        replaced_letters.update(temp)
        temp = {value:key}              # Add the opposite of each other
        replaced_letters.update(temp)
    return replaced_letters


# decryption = decrypt the given string by a dictionary of keys to replace, it uses the translate method.
# creates the translation table from the given keys and used translate to replace the string with that translation table
def decryption(message,key):
    message = message.lower()
    message = message.translate(str.maketrans(key))         # Created the translation table by given key with maketrans.
    return message                                          # Then we pass it as an argument tot the translate()


# add_to_file = Adds to the original file the decrypted message and create a results text file with the decryption only
def add_to_file(path):
    with open(path,"r") as original_file:     # Reads the original file
        data = original_file.read()
    with open(path,"a") as translated:      # open or create the translated file, add the decryption at the end
        translated.write("\n")
        translated.write("The encryption for the above text is:\n")
        translated.write(decryption(data,common_letters(data)))
    with open("results.txt",'a') as results:    # open or create new file called results that contain the decryption
        results.write(decryption(data,common_letters(data)))


# get_longest_word = program to get the longest word. returns the longest word out of the results file.
# it uses the translation method to remove special characters.
def get_longest_word(file):
    longest_words = []
    with open(file,"r") as results:         # Opens the file to get the file contains
        data = results.read()
    data = data.translate(str.maketrans('', '',string.punctuation))     # Removes special characters
    data = data.replace("\n", " ").split(" ")           # get rid of \n for correct lengths of words
    max1 = len(data[0])             # current max length word
    temp = data[0]                  # the current longest word
    for word in data:
        if(len(word) > max1):
            max1 = len(word)
            temp = word
            longest_words.append(temp)
    return str(longest_words).strip("'[]")      # stripped the word from special characters


# number_of_lines = simply returns the number of lines in a file. It reads the file line by line and add it to a list
def number_of_lines(path):
    with open(path,"r") as results:
        results = results.readlines()           # To create a list of lines
    return len(results)

def main():
    original_stdout = sys.stdout
    results = "results.txt"     # PATHS TO THE RESULTS FILE AND ENCRYPTED FILE
    path = "message.txt"
    i = 0
    with open(path, "r") as encrypted:      # Opens the encrypted file and read their containing
        encrypted.seek(0)
        data = encrypted.read()
    common_letters(data)                    # Get the common letters and dictionary of keys to decrypt the message
    add_to_file(path)                      # Add to the original file the decrypted message and create new results file
    with open(path, "a") as new_file:
        new_file.write("\n")
        while i < number_of_lines(results):         # prints the longest word in the results file times the lines of it
            new_file.write(f"{get_longest_word(results)} ")
            i+=1
    with open(path, "a") as final_mark:             # Prints the final mark
        sys.stdout = final_mark                # Changed the print function to print into the new file instead of screen
        final_mark.write("\n")
        num = 5
        print("*   *")
        for row in range(0,num):
            for col in range(0,num):
                if (row == col) or (num - col  - 1) == row:
                    print("*", end = '')
                else:
                    print(" ", end = '')
            print('')
        print("*   *")
        sys.stdout = original_stdout


if __name__ == "__main__":
    main()