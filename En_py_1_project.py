"""
projekt_1.py
discord: petulek
"""
import re

# Registered users
USERS = {
    'bob': '123',
    'ann': 'pass123',
    'mike': 'password123',
    'liz': 'pass123'
}

# Texts for analysis
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

"""
Function for verifying user data.
    User must input his username and password.
    If user logs in, program will continue.
    If user does not exist, user will receive message and program will be terminated
"""
def login():
    
    username = input("username: ")
    password = input("password: ")
    if USERS.get(username) == password:
        print("----------------------------------------")
        print(f"Welcome to the app, {username}")
        return True
    else:
        print("Unregistered user, terminating the program..")
        return False


def analyze_text(text):
    """
    Function for text analysis.
    Splits the input text into a list of words. The default delimiter is a space.
    It divides words into different lists.
    It then calculates different statistics.
    """
    words = text.split()
    word_len = [len(word.strip(".,!?")) for word in words]
    title_words = [word for word in words if word.istitle()]
    upper_words = [word for word in words if word.isupper()]
    lower_words = [word for word in words if word.islower()]
    numeric = [word for word in words if re.match(r'^-?\d+(?:\.\d+)?$', word)]

    word_count = len(words)
    title_count = len(title_words)
    upper_count = len(upper_words)
    lower_count = len(lower_words)
    numeric_count = len(numeric)
    numeric_sum = sum(int(word) for word in numeric)

    word_len_counts = {}
    for length in word_len:
        word_len_counts[length] = word_len_counts.get(length, 0) + 1

    return (word_count, title_count, upper_count, lower_count, numeric_count, numeric_sum, word_len_counts)

"""
Function to display analysis results.
"""
def display_results(stats):
    word_count, title_count, upper_count, lower_count, numeric_count, numeric_sum, word_len_counts = stats
    print("----------------------------------------")
    print(f"There are {word_count} words in the selected text.")
    print(f"There are {title_count} titlecase words.")
    print(f"There are {upper_count} uppercase words.")
    print(f"There are {lower_count} lowercase words.")
    print(f"There are {numeric_count} numeric strings.")
    print(f"The sum of all the numbers {numeric_sum}")

    print("----------------------------------------")
    print("LEN|  OCCURENCES  |NR.")
    print("----------------------------------------")
    for length, count in sorted(word_len_counts.items()):
        print(f"{length:3}| {'*' * count:14}|{count}")


"""
Main function.
The user must be successfully logged in, otherwise the script will terminate.
After successful login, the user can choose from three texts. If he enters a higher number, the script will end.
If the user entered the correct number of text, he will get the calculated statistics.
"""
def main():
    if not login():
        return
    print("We have 3 texts to be analyzed.")
    while True:
        try:
            selection = int(input("Enter a number btw. 1 and 3 to select: "))
            if selection not in range(1, 4):
                print("Invalid input. Program terminated.")
                return
            break
        except ValueError:
            print("Invalid input. Program terminated.")
            return

    selected_text = TEXTS[selection - 1]
    stats = analyze_text(selected_text)
    display_results(stats)


if __name__ == "__main__":
    main()