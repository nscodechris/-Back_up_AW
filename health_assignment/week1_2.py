import math


# Coding Challenge 2

# 1. Calculating reminder of 365/12


def calculate_reminder_of_345():
    x = 345
    y = 12
    result = x / y
    return print(f"Challenge 2.1\nThe reminder by dividing 345/12 is: {result}")

# 2. Create a variable x and set it to 5 and another variable y to 3.
# Overwrite x to have the value of x * y. Subtract 5 from x. Now display the result.


def subtract():
    x = 5
    y = 3
    x = x * y
    x = x - 5
    return print(f"Challenge 2.2\nResult is:  {x}")

# 3. Orange challenge, friend has 37 oranges, takes 6, split evenly between 3 other friends,
# How many remains?


def orange_challenge():
    my_friend_oranges = 37
    my_friend_takes = 6
    total_left = my_friend_oranges - my_friend_takes
    first_friend = total_left / 3
    second_friend = total_left / 3
    third_friend = total_left / 3
    total_left = total_left - (first_friend + second_friend + third_friend)
    print(f"Challenge 2.3\nTotal oranges left: {total_left}")


def f_string_challenge():
    my_initials = "CB"
    population_town = 40000
    population_on_earth = 8
    current_week_day = "wednesday"
    duration_of_course_in_month = 4
    the_number_of_pi = math.pi
    print(f"Challenge 3\nHi my name is Christoffer Brodin, an my initials are {my_initials}\nI live in Upplands Väsby with a "
          f"population of {population_town}.\nAs we speak the population on earth is {population_on_earth} billion\nI "
          f"really enjoy the first days of education, learnd many new things in SQL even though its just "
          f"{current_week_day}.\nI'm looking forward for all the {duration_of_course_in_month} months of learning."
          f"\nWithout cheating i only know the four first decimals of pi, if you are interested to know, this is pi "
          f"{the_number_of_pi}.\nThanks for reading!")


calculate_reminder_of_345()
subtract()
orange_challenge()
f_string_challenge()
