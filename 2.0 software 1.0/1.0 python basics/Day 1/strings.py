#concatination and interpolation


# #concatination
# first_name = "John"
# last_name = "Ven"
# full_name = first_name + last_name

# #interpolation
# print(f"my fullname is {full_name}")

# laugh = "Ha" * 7
# print(laugh)

# #length
# message = "Hello, python!"
# print(len(message))

# name = "Alice"
# age = 30
# score = 95.5

# #method 1: f-strings recommend like fill in the blank
# print(f"Hello, {name}! You are {age} years old.")
# print(f"Your score is {score:.1f}%")

# #method 2: format() method
# print("Hello, {}! You are {} years old." .format(name,age))

# #method 3: % formatting (older style)
# print("Hello, %s! You are %d years old." %(name, age))

# email = input("Enter your email ")
# if "@" in email and "." in email:
#     username = email.split("@")[0]
#     domain = email.split("@")[1]
#     print(f"Username: {username.title}")
#     print(f"Domain: {domain}")
# else:
#     print("Invalid email format")


# text = "The quick brown fox jumps over the lazy dog"
# print(f"Text: {text}")
# print(f"Lenght: {len(text)} characters")
# print(f"Words: {len(text.split())} words")
# print(f"Uppercase: {text.upper()}")
# print(f"Title case: {text.title()}")
# print(f"Contains 'fox': {'fox' in text}")

# full_name = "jOhN DOe"

# print(f"{full_name.title()}")
# first_name =full_name.split(' ')[0]
# last_name = full_name.split(' ')[1]

# print(f"first name: {first_name}")
# print(f"Last name: {last_name}")


# sentence = "python is an amazing programming language"

# print(f"Words: {len(sentence.split())} words")
# print(f"Length: {len(sentence)} characters")
# letter = "a"
# count = sentence.count(letter)
# print(f"The letter {letter} appears {count} times")

message = "Hello"
cipher_text = ""

for char in message:
    if char.isalpha():  # Check if it's a letter
        # Shift by 1 and wrap around if needed
        if char.islower():
            cipher_text += chr((ord(char) - ord('a') + 1) % 26 + ord('a'))
        else:  # uppercase
            cipher_text += chr((ord(char) - ord('A') + 1) % 26 + ord('A'))
    else:
        cipher_text += char  # Leave non-letter characters as is

print("Original:", message)
print("Ciphered:", cipher_text)
