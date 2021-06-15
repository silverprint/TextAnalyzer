from task_template import TEXTS

user_data = dict(bob='123', ann='pass123', mike='password123', liz='pass123')
n_words = n_titlecase = n_upercase = n_lowercase = n_numers = sum_numbers = 0
n_len = {}
separator = "-" * 40

# user verification
username = input("username: ")
if username not in user_data.keys():
    print(f"Username {username} does not exist.")
else:
    password = input("password: ")
    print(separator)
    if password != user_data[username]:
        print(f"Incorrect password.")
    else:
        # say hello
        print(f"Welcome to the app, {username}\n We have 3 texts to be analyzed.")
        print(separator)

        # text selection and evaluation
        text_number = int(input("Enter a number btw. 1 and 3 to select: "))
        print(separator)

        text = TEXTS[text_number-1].split()
        cleaned_text = {word.strip(".,:?!") for word in text}

        n_words = len(cleaned_text)
        for word in cleaned_text:
            n_titlecase += 1 if word.istitle() else 0
            n_upercase += 1 if word.isupper() else 0
            n_lowercase += 1 if word.islower() else 0
            if word.isnumeric():
                n_numers += 1
                sum_numbers += int(word)
            word_length = len(word)
            n_len[word_length] = n_len.setdefault(word_length, 0) + 1

        print(f"There are {n_words} words in the selected text.")
        print(f"There are {n_titlecase} titlecase words.")
        print(f"There are {n_upercase} uppercase words.")
        print(f"There are {n_lowercase} lowercase words.")
        print(f"There are {n_numers} numeric strings.")
        print(f"The sum of all the numbers {sum_numbers}")

        # word length graph
        print(separator)
        print("LEN|  OCCURENCES  |NR.")
        print(separator)

        max_length = max(n_len.keys())
        for length in range(max_length):
            length += 1  # fix indexing from zero
            s_length = (len(str(max_length)) - len(str(length)) + 1) * " " + str(length)  # indent fix
            n_len.setdefault(length,0)  # non existing keys fix
            print(f"{s_length}|{n_len[length] * '*' + (14 - n_len[length]) * ' '}|{n_len[length]}")
