# IPND Stage 2 Final Project by Christoph

# Fill-in-the-Blanks Game!

# game groundwork for difficulty, senctences and answers:

welcome = "Hello! This is a nice quiz game!" + "\n\n" + "In a first step, please choose the game difficulty (easy, medium or hard)."
difficulty = ["easy", "medium", "hard"]
sentence_message = "Your quiz sentence is as follows. Good luck!!!"
error_difficulty = "Please choose only between 'easy', 'medium' or 'hard'."
error_max_answers = "Pleasy choose an integer number greater as zero."
# sentences are stored in lists for accessability. If quiz sentences would be entered as string, lists could be easily derived using the split() method.
sentence_A = ["A common first thing to do in a language is display 'Hello ", "__1__",
             " !' In ", "__2__",
             " this is particularly easy; all you have to do is type in: ", "__3__",
             " 'Hello ", "__1__",
             "'! Of course, that isn't a very useful thing to do. However, it is an example of how to output to the user using the ", "__3__",
             " command, and produces a program which does something, so it is useful in that capacity. It may seem a bit odd to do something in a Turing complete language that can be done even more easily with an ", "__4__",
             " file in a browser, but it's a step in learning ", "__2__",
             " syntax, and that's really its purpose."]
sentence_B = ["A ", "__1__",
             " is created with the def keyword. You specify the inputs a ", "__1__",
             " takes by adding ", "__2__",
             " separated by commas between the parentheses. ", "__1__",
             "s by default return ", "__3__",
             " if you don't specify the value to return. ", "__2__",
             " can be standard data types such as string, integer, dictionary, tuple, and ", "__4__",
             " or can be more complicated such as objects and lambda functions."]
sentence_C = ["When you create a ", "__1__",
             ", certain ", "__2__",
             "s are automatically generated for you if you don't make them manually. These contain multiple underscores before and after the word defining them. When you write a ", "__1__",
             ", you almost always include at least the ", "__3__",
             " ", "__2__",
             " , defining variables for when ", "__4__",
             "s of the ", "__1__",
             " get made. Additionally, you generally want to create a ", "__5__",
             " ", "__2__",
             ", which will allow a string representation of the method to be viewed by other developers. You can also create binary operators, like ", "__6__",
             " and ", "__7__",
             ", which allow + and - to be used by ", "__4__",
             "s of the ", "__1__",
             ".  Similarly, ", "__8__",
             ", ", "__9__",
             " and ", "__10__",
             " allow ", "__4__",
             "s of the ", "__1__",
             " to be compared (with <, >, and ==)."]
senctences = [sentence_A, sentence_B, sentence_C]
answers_A = ["world", "Python", "print", "HTML"]
answers_B = ["function", "arguments", "None", "list"]
answers_C = ["procedure", "argument", "input", "calls", "comment", "plus", "minus", "smaller", "bigger", "equal"]
answers = [answers_A, answers_B, answers_C]
# answer positions are derived from the list sentences - here manually. Could also be easily done with a for loop searching the list sentences.
answer_positions_A = [[1, 7], [3, 13], [5, 9], [11]]
answer_positions_B =[[1, 3, 7], [5, 11], [9], [13]]
answer_positions_C = [[1, 5, 13, 25, 35], [3, 9, 17], [7], [11, 23, 33], [15], [19], [21], [27], [29], [31]]
answer_positions = [answer_positions_A, answer_positions_B, answer_positions_C]
# initial wrong answer counts set to zero
wrong_answer_count_A = [0, 0, 0, 0]
wrong_answer_count_B = [0, 0, 0, 0,]
wrong_answer_count_C = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
wrong_answer_count = [wrong_answer_count_A, wrong_answer_count_B, wrong_answer_count_C]
wrong_answer_message = "Wrong answer! Try again. Tries left: "
game_over_message = "Game over! Too many tries!"
right_answer_message = "Right answer!"
win_message = "Great work! You have won!!!"
thanks_message = "Thanks for playing! Hope you enjoyed it!"

# procedure to let the user choose the difficulty. Displays error message if input is not valid and repeats the promt until a right difficulty is chosen.
# Takes not input from other sources, as difficulty is raw_input by the user.
# Output is either an error message with a new prompt or the chosen difficulty.

def set_difficulty():
    global user_input_difficulty
    user_input_difficulty = raw_input("Game difficulty: ")
    while (user_input_difficulty != difficulty[0] and user_input_difficulty != difficulty[1] and user_input_difficulty != difficulty[2]) == True:
        print error_difficulty
        user_input_difficulty = raw_input("Game difficulty: ")
    return user_input_difficulty

# procedure to let the user choose the number of max. wrong answers. Displays error message if input is not valid and repeats the promt until a right input is chosen.
# Takes not input from other sources, as max answers is raw_input by the user.
# Output is either an error message with a new prompt or the chosen number of wrong answers (as integer).

def set_max_answers():
    global max_wrong_answers
    max_wrong_answers = raw_input("Set max. wrong answers: ")
    index = False
    while index == False:
        try:
            int(max_wrong_answers)  # I had to do this, because the method raw_input() delivers str by default.
        except ValueError:
            print error_max_answers
            max_wrong_answers = raw_input("Set max. wrong answers: ")
        else:
            while int(max_wrong_answers) <= 0:
                print error_max_answers
                max_wrong_answers = raw_input("Set max. wrong answers: ")
            index = True
    return max_wrong_answers

# procedure to return the quiz sentence regarding the chosen game difficulty.
# Input is the game difficulty chosen by the user in the set_difficulty() procedure.
# Output is the actual quiz sentence that is used troughout the game.
# Output is stored in global variables so that other procedures can uses theses values.

def sentence(user_input_difficulty):
    global quiz_sentence
    if user_input_difficulty == difficulty[0]:
        quiz_sentence = senctences[0]
    elif user_input_difficulty == difficulty[1]:
        quiz_sentence = senctences[1]
    elif user_input_difficulty == difficulty[2]:
        quiz_sentence = senctences[2]
    return quiz_sentence

# procedure to return the approriate answer set regarding the chosen game difficulty.
# Input is the game difficulty chosen by the user in the set_difficulty() procedure.
# Outputs are the actual answer set, the answer positions in the list sentences and the actual set of initial wrong answers.
# Outputs are stored in global variables so that other procedures can uses theses values.

def set_answers(user_input_difficulty):
    global answer_set
    global answer_positions_set
    global wrong_answer_count_set
    if user_input_difficulty == difficulty[0]:
        answer_set = answers[0]
        answer_positions_set = answer_positions[0]
        wrong_answer_count_set = wrong_answer_count[0]
    elif user_input_difficulty == difficulty[1]:
        answer_set = answers[1]
        answer_positions_set = answer_positions[1]
        wrong_answer_count_set = wrong_answer_count[1]
    elif user_input_difficulty == difficulty[2]:
        answer_set = answers[2]
        answer_positions_set = answer_positions[2]
        wrong_answer_count_set = wrong_answer_count[2]
    return answer_set
    return answer_positions_set
    return wrong_answer_count_set

# procedure to compare user input with the corresponding anwers.
# Input is difficulty on one side (this allows the choize of the right answer set) and the current number of the blank (necessary for comparing the user input with the answer set).
# Output are the quiz sentence with the correctly answered blank filled in. Returns error message if answer is not correct.
# Repeats until max_wrong_answers. Print game over message if limit of wrong answers is reached.

def check_answers(user_input_difficulty, number_of_blank):
    input_answer = raw_input("What should be substituted for __" + str(number_of_blank + 1) + "__: ")
    answer_set = set_answers(user_input_difficulty)
    index = 1
    while index <= int(max_wrong_answers):
        if input_answer == answer_set[number_of_blank]:
            return answer_set[number_of_blank]
            break
        else:
            if index < int(max_wrong_answers):
                print "\n\n" + wrong_answer_message + str(int(max_wrong_answers) - index) + "\n\n"
                input_answer = raw_input("What should be substituted for __" + str(number_of_blank + 1) + "__: ")
                wrong_answer_count_set[number_of_blank - 1] += 1
                index += 1
            else:
                print "\n\n" + game_over_message + "\n\n"
                break

# procedure to return the intermdiary sentence with the filled out blanks after a correct answer.
# Inputs are the numer ot the current blank and the correct answer, so that the current blank in the quiz sentence can be replaced by the correct answer.
# Output is the current quiz sentence.

def intermediary_sentence(number_of_blank, answers):
    replace_positions = answer_positions_set[number_of_blank]
    length_replace = len(replace_positions)
    index = 0
    while index < length_replace:
        position = replace_positions[index]
        quiz_sentence[position] = answers[number_of_blank]
        index += 1
    return quiz_sentence

# procedure to print out the number of wrong answers in a formatted table.
# Input is a list with the number of the wrong answers for each question.
# Ouput are a formatted table with two columns and a thank you message.

def table_wrong_answers(wrong_answer_count_set):
    print "Result for each Blank:" + "\n\n"
    print "Blank" + " | " + "# Wrong Answers"
    index = 0
    for blank in wrong_answer_count_set:
        print (" ")*(3 - len(str(index + 1))) + str(index + 1) + (" ")*3 + "|" + (" ")*8 + str(wrong_answer_count_set[index])
        index += 1
    return "\n\n" + thanks_message

# procedure to go through the questions and answers step by step.
# Input is the game difficulty chosen by the user. This input defines which answer set to use and triggers the check_answers procedure correctly.
# Outputs are a right answer message if the current question is answered correctly, the current quiz sentence with the last filled out blank and a win message and the wrong answer table if the game is completed successfully.
# Note that win message is only reached if the last blank is answered correctly. If the user needs to many tries the game over message is an output from the check_answers() procedure, the while loop breaks and the win message is never reached.

def questions_by_step(user_input_difficulty):
    index = 0
    answer_set = set_answers(user_input_difficulty)
    length_answer_set = len(answer_set)
    while index < length_answer_set:
        if check_answers(user_input_difficulty, index) == answer_set[index]:
            print "\n\n" + right_answer_message + "\n\n"
            intermediary_sentence(index, answer_set)
            print "Your sentence now states as follows:" + "\n\n" + "".join(quiz_sentence) + "\n\n"
            index += 1
        else:
            break
    else:
        print "\n\n" + win_message + "\n\n"
        return table_wrong_answers(wrong_answer_count_set)

# procedure for the gameplay
# Takes no input.
# Outputs are a welcome message, the after the user sets the difficulty, then after the user sets the max wrong answer count,
# then the quiz sentence is displayed and then the questions_by_stepprocedure is called with the further steps.

def play_game():
    print "\n\n" + welcome + "\n\n"
    # first prompt to be chosen by the user: game difficulty.
    print "You have chosen: " + set_difficulty() + "\n\n"
    # the the user sets the mx wrong answers count.
    print "You have " + str(set_max_answers()) + " answers for each question" + "\n\n"
    # then the initial quiz sentence is displayed.
    print sentence_message + "\n\n" + ''.join(sentence(user_input_difficulty)) + "\n\n"
    # this calls the questions_by_step procedure.
    return questions_by_step(user_input_difficulty)

# this lets the game begin.

print play_game()
