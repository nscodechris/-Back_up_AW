


def email_domain():
    email = input("what is your email adress?").strip()
    user_name = email[: email.index("@")]
    domain_name = email[email.index("@")+1:]
    print(f"Your username is {user_name}, and your domain name is {domain_name}")
    output = "Your username is {0} and your domain name is {1}".format(user_name, domain_name)
    print(output)

# email_domain()

def security_system():
    known_users = ["alice", "bob", "bob", "claire", "dan", "emma", "fred", "georige", "harry"]
    # print(len(known_users))
    # print(known_users)
    while True:
        print(f" members in list {known_users}")
        print("hi my name is Travis")
        user_name = input("What is your name?").strip().lower()
        if user_name in known_users:
            print(f"Hello {user_name}!")
            remove = input("Would you like to be removed from the systam (y/n)").lower()
            if remove == "y":
                for names in list(known_users):
                    if names == user_name:
                        known_users.remove(user_name)

                # index_name = known_users.index(user_name)
                # known_users.pop(index_name)
               # known_users.remove(user_name)
                print(known_users)
            elif remove == "n":
                print("no problem, i didn't want you to leave anyway")
        else:
            print(f"Hmm i don't think i have met you yet {user_name}")
            add_me = input("would you like to be added to the system(Y/N?):").strip().lower()
            if add_me == "y":
                known_users.append(user_name)
                print("Nice, you have been added to the list")
            elif add_me == "n":
                print("ok, nice to see you")


def cinema_simulator():
    import pandas as pd
    movies_dict = {"Terminator": [3, 5],
                   "Alien": [18, 5],
                   "Tarzan": [12, 5]}
    while True:
        df = pd.DataFrame(movies_dict.keys())
        print(df)
        user_choice = input("What movie do you want to see?").strip().title()
        if user_choice in movies_dict.keys():
            user_age = int(input("How old are you?").strip())
            movie_age = movies_dict[user_choice][0]
            if user_age >= movie_age:
                print("You are old enough")
                ticket_to_buy = int(input("How many tickets do you want?"))
                ticket_in_store = movies_dict[user_choice][1]
                if ticket_to_buy <= ticket_in_store:
                    print(f"You bought {ticket_to_buy}, tickets")
                    movies_dict[user_choice][1] = movies_dict[user_choice][1] - ticket_to_buy
                else:
                    print(f"We dont have {ticket_to_buy}, tickets left... only have {ticket_in_store}")
            else:
                print("You are to young to see that film")
            pass
        else:
            print("We don't have that film....")


def baby_translator():
    count_quest = 0
    while count_quest < 4:
        question_list = [" rabbits cute?", " sky blue?", " ball round?"]
        for i in range(len(question_list)):
            baby_question = "Why is" + question_list[i]
            print(baby_question)
            answer = input()
            if answer == "just because":
                print("thanks")
                count_quest += 1
                pass
            else:
                print("dont understand!")
                break



def count_vovels(word):
    consonants = 0
    vovels = 0
    other = 0
    for i in word:
        if i in "a,e,o,u,i":
            vovels += 1
        elif i in " ":
            other += 1
        else:
            consonants += 1
    print(consonants, vovels, other)


def pig_language():
    # get sentence from user
    # split sentecne in words
    # loop through words and convert to pig latin
    # stick words bak togehter
    # output the final string

    user_input = input("Give me a nice sentence").strip().lower()
    user_words = user_input.split()
    new_words = []
    for words in user_words:
        if words[0] in "aioue":
            new_word = words + "yay"
            new_words.append(new_word)
        else:
            vowel_pos = 0
            for letter in words:
                if letter not in "aioue":
                    vowel_pos += 1
                else:
                    break
            cons = words[:vowel_pos]
            the_rest = words[vowel_pos:]
            new_word = the_rest + cons + "ay"
            new_words.append(new_word)
    new_sentence = " ".join(new_words)
    print(new_sentence)


