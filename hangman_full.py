HANGMAN_PHOTOS = {1: "x-------x",
 2: '''
    x-------x
    |
    |
    |
    |
    |
    ''',
    3: '''
    x-------x
    |       |
    |       0
    |
    |
    |
    ''',
    4: '''
    x-------x
    |       |
    |       0
    |       |
    |
    |
    ''',
    5: '''
    x-------x
    |       |
    |       0
    |      /|\\
    |
    |
    ''',
    6: '''
    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |
    ''',
    7: '''
    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |
    '''}

def print_hangman(num_of_tries):
    """Print one of hangman's conditions by index of player's attempts
    :param: num_of_tries: number of player's erroneous attempts
    :type num_of_tries: int
    :return: print one of hangman's pictures from dictionary HANGMAN_PHOTOS by index of num_of_tries
    :rtype: string"""
    return print(HANGMAN_PHOTOS.get(num_of_tries))

def check_win(secret_word, old_letters_guessed):
    """Checks if the whole secret word was guessted correctly
   	:param: secret_word: the word to be guessed
    :param: old_lettes_guessed: the letters that were guessted (user's input)
    :type secret_word: list
    :type old_lettes_guessed: list
    :return: True if the secret word was guessed, False if not
    :rtype: boolean
    """
    arr = list(secret_word)
    for x in arr:
        if x in old_letters_guessed:
            continue
        else:
            return False
    return True

def show_hidden_word(secret_word, old_letters_guessed):
    """Displays guessed letters in the secret word, and '_' for letters that were
    not guessed yet
    :param: secret_word: the word to be guessed
    :param: old_lettes_guessed: the letters that were guessted (user's input)
    :type secret_word: list
    :type old_lettes_guessed: list
    :return: the updated list, with all guessed letters
    :rtype: list
    """
    my_str = list("_" * len(secret_word))
    for x in old_letters_guessed:
        for l in range(len(secret_word)):
            if x == secret_word[l]:
                my_str[l] = x
    return " ".join(my_str)

def check_valid_input(letter_guessed, old_letters_guessed):
    """Checks the validation of user's input, e.g one English letter, not entered
    before
    :param letter_guessed: user input
    :param old_letters_guessed: previous inputs
    :type letter_guessed: string
    :type old_letters_guessed: list
    :return: True if input is valid, False if not.
    :rtype: boolean
    """
    if letter_guessed.lower().isalpha() and len(letter_guessed) == 1 and letter_guessed.lower() not in old_letters_guessed:
        return True
    else:
        return False 

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """Checks validation of user's input (as in previous task).
    if so, adds it to "old_letters_guessed" and returns True. Otherwise returns
    False.
    :param letter_guessed: user's input
    :param old_letters_guessed: previous (valid) inputs
    :type letter_guessed: string
    :type old_letters_guessed: list
    :return: True if input is valid, False if not.
    :rtype: boolean
	"""
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed.lower())
        return True
    else:
        old_letters_guessed.sort()
        sorted_list = " -> ".join(old_letters_guessed)
        print("X\n" + sorted_list)
        return False
    
def choose_word(file_path, index):
    """Picks one word from a list of words, read from a file, according to a given index in the list
    :param: file_path: the path of the file that contains a word list
    :param: index: the position of the word to be picked
    :type: file_path: string
    :type: index: int
    :return: picked word
    :rtype: tuple
    """
    f = open(file_path, "r")
    words_list = f.read()
    f.close()
    words_list = words_list.split(" ")
    return words_list[int(index)%len(words_list)-1]

def print_starting_menu():
    """Print starting menu as ASCI picture
    :return: ASCI picture
    :rtype: string
    """
    return print('''
    _    _
   | |  | |
   | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
   |  __  |/ _' | '_ \ / _' | '_ ' _ \ / _' | '_ \\
   | |  | | (_| | | | | (_| | | | | | | (_| | | | |
   |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |
                       |___/
    ''')

MAX_TRIES = 6

def hangman(secr_word):
    """Main logic of the game using all previous functions
    :param secr_word: the word to be guessed
    :type: secr_word: string"""
    num_of_tries = 1
    old_letters_guessed = []
    print("")
    print("Let's start!\n")
    print_hangman(num_of_tries)
    while (num_of_tries <= MAX_TRIES):
        print(show_hidden_word(secr_word, old_letters_guessed))
        inp = input("Guess a letter: ")
        is_true = try_update_letter_guessed(inp, old_letters_guessed)
        while(is_true == False):
            inp = input("Guess a letter: ")
            is_true = try_update_letter_guessed(inp, old_letters_guessed)
        if inp.lower() not in secr_word and is_true == True:
            num_of_tries += 1
            print(":(")
            print_hangman(num_of_tries)
        if check_win(secr_word, old_letters_guessed):
            print(show_hidden_word(secr_word, old_letters_guessed) + "\nWIN")
            break
    if num_of_tries > MAX_TRIES:
        print(show_hidden_word(secr_word, old_letters_guessed) + "\nLOSE")
    return

def main():
    print_starting_menu()
    print(MAX_TRIES)
    secret_word = choose_word(input("Enter file path: "), input("Enter  index: "))
    hangman(secret_word)

if __name__ == "__main__":
    main()        

