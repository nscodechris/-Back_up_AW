
# week 3 challenge 1

def count_down():
    # Creating a count_down from 50 to 0 using range
    print("-"*50)
    input("Week 3 Challenge 1, press enter and a countdown from 50 - 0 will start")
    for i in range(50, -1, -1):
        print(i)
    return

# week 3 challenge 2

def format_text():
    print("-"*50)
    my_string = "Python is a _nice_ #LANGUAGE#"
    # Putting every word in my_string to a list
    my_string_list = my_string.split()
    # Iterate through the my_string_list
    for i in my_string_list:
        # Getting the index of each word in the list
        word_index = my_string_list.index(i)
        # Checking if a word in the list starts with "_" removing symbols & convert the word to UPPER_CASES
        if i.startswith("_"):
            # print(word_index)
            i = i[1:-1]
            i = i.upper()
            # print(i)
            my_string_list[word_index] = i
        # Checking if a word in the list starts with "#" removing symbols & convert the word to lower_cases
        elif i.startswith("#"):
            i = i[1:-1]
            i = i.lower()
            # print(i)
            my_string_list[word_index] = i
    # print(my_string_list)
    # Joining the my_string_list words in to a new string
    new_string = ' '.join([str(elem) for elem in my_string_list])
    print("Week 3, Challenge 2")
    print("OLD STRING: Python is a _nice_ #LANGUAGE#")
    print(f"NEW STRING: {new_string}")


# week 3 challenge 3
def my_counter(challenge_text, string_or_list):
    print("-"*50)
    count_dict = {}
    for i in string_or_list:
        if i in count_dict:
            count_dict[i] += 1
        else:
            count_dict[i] = 1
    print(challenge_text)
    return print(count_dict)


count_down()
format_text()
my_counter("Week 3, Challenge 3, with numbers, numbers used: '1 2 3 3'", [1, 2, 3, 3])
my_counter("Week 3, Challenge 3, with text, text used: 'Christoffer'", "Christoffer")


