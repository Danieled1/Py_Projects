import string
import sys

def get_common_letters(str1):
    str1 = str1.lower()
    common_letters = {}
    most_common = ["e", "t", "o", "r"]

    for char in str1:
        if char.isalpha():
            if char in common_letters:
                common_letters[char] += 1
            else:
                common_letters[char] = 1

    common_letters = dict(sorted(common_letters.items(), key=lambda x: x[1], reverse=True))

    replaced_letters = {}
    for i, char in enumerate(common_letters.keys()):
        if i < len(most_common):
            replaced_letters[char] = most_common[i]
            replaced_letters[most_common[i]] = char

    return replaced_letters


def decryption(message, key):
    message = message.lower()
    translated = str.maketrans(key)
    decrypted_message = message.translate(translated)
    return decrypted_message


def add_to_file_contents(path):
    with open(path, "r") as original_file:
        data = original_file.read()

    encrypted_message = data.split("\n")[0]  # Extract the encrypted message

    with open(path, "w") as file:
        file.write(encrypted_message)  # Write the encrypted message back to the file

    with open("results.txt", "a") as results:
        results.write(decryption(data, get_common_letters(data)))


def get_longest_word(file):
    longest_word = ""
    with open(file, "r") as results:
        data = results.read()
        data = data.translate(str.maketrans("", "", string.punctuation))
        words = data.split()
        longest_word = max(words, key=len)

    return longest_word


def number_of_lines(path):
    with open(path, "r") as results:
        lines = results.readlines()

    return len(lines)


def main():
    original_stdout = sys.stdout
    results = "results.txt"
    path = "message.txt"
    i = 0

    with open(path, "r") as encrypted:
        data = encrypted.read()

    add_to_file_contents(path)

    with open(path, "a") as new_file:
        new_file.write("\n")
        while i < number_of_lines(results):
            new_file.write(f"{get_longest_word(results)} ")
            i += 1

    with open(path, "a") as final_mark:
        sys.stdout = final_mark
        final_mark.write("\n")
        num = 5
        print("*   *")
        for row in range(num):
            for col in range(num):
                if row == col or (num - col - 1) == row:
                    print("*", end='')
                else:
                    print(" ", end='')
            print('')
        print("*   *")
        sys.stdout = original_stdout


if __name__ == "__main__":
    main()
