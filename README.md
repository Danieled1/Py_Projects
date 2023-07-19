# Encryption and Decryption Script

This Python script performs encryption and decryption operations on a given text file. It includes functions to extract common letters, find the longest word, count the number of lines, and generate a final mark pattern.

## Usage

1. Ensure you have Python installed on your system.
2. Clone this repository or download the `encryption_decryption.py` file.
3. Prepare a text file with the message you want to encrypt or decrypt (e.g., `message.txt`).
4. Open the `encryption_decryption.py` file and modify the `message.txt` path if necessary.
5. Run the script by executing the command: `python encryption_decryption.py`.
6. The decrypted message will be added to the original file, and a results file will be created.
7. The script will also append the longest word from the results file to the original file for each line.
8. Finally, a pattern of a star-filled square will be printed to the end of the file.

## Customization

- To change the encryption or decryption key, modify the `most_common` list in the `common_letters` function.
- To adjust the number of lines the longest word is appended, modify the `num` variable in the `main` function.
- Feel free to explore and modify the code according to your requirements.

## License

This project is licensed under the [MIT License](LICENSE).
