# Username Analyzer Easy

# Ask the user to enter a username. Print:
# - The username in capitalized form.
# - The total number of characters.
# - Whether the username ends with "123".
# Example: sara123 → Sara123, length 7, ends with 123: True.

username = input("Enter a username: ")
print(username.capitalize())
print(len(username))
print(username.endswith("123"))