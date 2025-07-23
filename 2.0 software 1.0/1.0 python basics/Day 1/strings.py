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

name = "Alice"
age = 30
score = 95.5

#method 1: f-strings recommend like fill in the blank
print(f"Hello, {name}! You are {age} years old.")
print(f"Your score is {score:.1f}%")

#method 2: format() method
print("Hello, {}! You are {} years old." .format(name,age))

#method 3: % formatting (older style)
print("Hello, %s! You are %d years old." %(name, age))