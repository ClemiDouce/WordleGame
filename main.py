# Init variables
secret_word = ""
user_input = ""
found_letters = set()
searched_letters = set()

try_count = 0
max_try = 3

# Choose a word
secret_word = "partir"

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
            found_letters.add(char)
            # if char in searched_letters:
            # searched_letters.remove(char)
        elif temp_char.count(char) > 0:
            result += "🟨"
            temp_char = temp_char.replace(char, '.', 1)
            # searched_letters.add(char)
        else:
            result += "⬜"
            searched_letters.add(char)
    print("Result : ", result)

    if user_input == secret_word:
        print("Bravo ! Le mot secret était bien : ", secret_word)
        break
    else:
        try_count += 1
        # print("Lettres trouvées : ", ', '.join(found_letters))
        # print("Lettres cherchées : ", ', '.join(searched_letters))
        user_input = input(f"Enter a word ({len(secret_word)} letters) : ")
