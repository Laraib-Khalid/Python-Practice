import random
import string

# Helper function to generate random 3-letter string
def random_chars(n=3):
    return ''.join(random.choices(string.ascii_lowercase, k=n))

# -----------------------------
# ENCRYPTION FUNCTION
# -----------------------------
def encrypt_message(message):
    """
    Encrypts a given message word by word according to the rules:
    - If a word has >=3 characters:
        * Move the first letter to the end
        * Add 3 random characters at the start and end
    - Else: reverse the word
    """
    words = message.split()
    coded_words = []

    for word in words:
        if len(word) >= 3:
            first_char = word[0]
            modified_word = word[1:] + first_char
            rand_start = random_chars()
            rand_end = random_chars()
            coded_word = rand_start + modified_word + rand_end
        else:
            coded_word = word[::-1]  # reverse if less than 3 chars
        coded_words.append(coded_word)

    return " ".join(coded_words)


# -----------------------------
# DECRYPTION FUNCTION
# -----------------------------
def decrypt_message(message):
    """
    Decrypts a message encoded using encrypt_message():
    - If a word has <3 characters: reverse it
    - Else:
        * Remove 3 random characters from start and end
        * Move last letter to the start
    """
    words = message.split()
    decoded_words = []

    for word in words:
        if len(word) >= 3 + 3 + 1:  # must have had random padding
            # Remove 3 chars from start and end
            core_word = word[3:-3]
            # Move last character to the beginning
            decoded_word = core_word[-1] + core_word[:-1]
        else:
            decoded_word = word[::-1]  # reverse back if <3 chars
        decoded_words.append(decoded_word)

    return " ".join(decoded_words)


# -----------------------------
# MAIN PROGRAM
# -----------------------------
if __name__ == "__main__":
    # Input message
    message = input("Enter your message: ")

    # Encrypt the message
    encrypted = encrypt_message(message)
    print("\n🔐 Encrypted Message:", encrypted)

    # Decrypt it back
    decrypted = decrypt_message(encrypted)
    print("🔓 Decrypted Message:", decrypted)
