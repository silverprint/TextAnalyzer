from task_template import TEXTS

user_data = dict(bob='123', ann='pass123', mike='password123', liz='pass123')
n_words = n_titlecase = n_upercase = n_lowercase = n_numers = sum_numbers = n_rest = 0
n_len = {}
separator = "-" * 40

# user verification
username = input("username: ")
if username not in user_data.keys():
    print(f"Username {username} does not exist. Exiting program.")
else:
    password = input("password: ")
    print(separator)
    if password != user_data[username]:
        print(f"Invalid password. Exiting program.")
    else:
        # say hello
        print(f"Welcome to the app, {username}\n We have 3 texts to be analyzed.")
        print(separator)

        # text selection
        n_texts = len(TEXTS)
        text_number = int(input(f"Enter a number btw. 1 and {n_texts} to select: "))
        if text_number - 1 not in range(n_texts):
            print("Invalid text number. Exiting program.")
        else:
            print(separator)

            # text evaluation
            text = TEXTS[text_number - 1].split(" ")
            cleaned_text = []
            for word in text:
                cleaned_text.append(word.strip(".,:?!\n\r "))
            if "" in cleaned_text:
                cleaned_text.remove("")

            n_words = len(cleaned_text)
            for word in cleaned_text:
                if word.isalpha():
                    n_titlecase += 1 if word.istitle() or word.isupper() else 0
                    n_upercase += 1 if word.isupper() else 0
                    n_lowercase += 1 if word.islower() else 0
                elif word.isnumeric():
                    n_numers += 1
                    sum_numbers += int(word)
                else:
                    n_rest += 1;
                word_length = len(word)
                n_len[word_length] = n_len.setdefault(word_length, 0) + 1

            print(f"There are {n_words} words in the selected text.")
            print(f"There are {n_titlecase} titlecase words.")
            print(f"There are {n_upercase} uppercase words.")
            print(f"There are {n_lowercase} lowercase words.")
            print(f"There are {n_numers} numeric strings.")
            print(f"The sum of all the numbers {sum_numbers}")

            # word length graph plotting
            print(separator)
            print("LEN|  OCCURENCES  |NR.")
            print(separator)

            max_length = max(n_len.keys())
            for length in range(max_length):
                length += 1  # fix indexing from zero
                s_length = (len(str(max_length)) - len(str(length)) + 1) * " " + str(length)  # indent fix
                n_len.setdefault(length, 0)  # non existing dict keys fix
                print(f"{s_length}|{n_len[length] * '*' + (14 - n_len[length]) * ' '}|{n_len[length]}")
