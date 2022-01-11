# Init variables
secret_word = ""
user_input = ""
searched_letters = ""
try_count = 0
max_try = 3

# Choose a word
secret_word = "uburluesque"

# Ask an input
while len(user_input) != len(secret_word):
    user_input = input(f"Enter a word ({len(secret_word)} letters) : ")

# Check the input with word
while try_count < max_try:
    result = ""
    temp_char = secret_word
    for index, char in enumerate(user_input):
        if char == temp_char[index]:
            result += "🟩"
        elif temp_char.count(char) > 0:
            result += "🟨"
            temp_char = temp_char.replace(char, '.', 1)
        else:
            result += "⬜"
    print("Result : ", result)

    if user_input == secret_word:
        print("Bravo ! Le mot secret était bien : ", secret_word)
        break
    else:
        try_count += 1
        user_input = input(f"Enter a word ({len(secret_word)} letters) : ")

# Send color for each letter 🟩🟨⬜
