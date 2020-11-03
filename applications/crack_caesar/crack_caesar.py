# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

f = open('applications\crack_caesar\ciphertext.txt')
cipher = f.read()
f.close()

letters = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
            'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']

def count_letter_freq(words):
    letter_counts = {}
    total_letters = 0 
    for char in words:
        if char in letters:
            if char not in letter_counts:
                letter_counts[char] = 1
            else:
                letter_counts[char] += 1
            total_letters += 1
    for letter in letters:
        letter_counts[letter] /= total_letters
    return letter_counts

cipher_freq = count_letter_freq(cipher)
sorted_freq = list(cipher_freq.items())
sorted_freq.sort(key=lambda x: x[1], reverse=True)
letter_freq = [x[0] for x in sorted_freq]

decoder = {k: v for k,v in zip(letter_freq, letters)}

def decode_cipher(words):
    decoded_message = ''
    for char in words:
        if char in decoder:
            decoded_message += decoder[char]
        else:
            decoded_message += char
    return decoded_message

message = decode_cipher(cipher)
print(message)

