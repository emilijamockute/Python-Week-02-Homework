from random import randint


def main():
    correct = 0

    questions = 0

    for questions in range(10):
        num_1 = randint(1, 10)
        num_2 = randint(1, 10)
        questions += 1

        print("Q", questions, ":", num_1, "X", num_2, "?")
        answer = int(input("Student Answer: "))

        if answer == num_1 * num_2:
            print("Answer: ", num_1 * num_2, "Status: CORRECT")
            correct += 1

        else:
            print("Answer: ", num_1 * num_2, " Status: WRONG")

    if correct >= 7:
        print("Test passed")
    else:
        print("Test failed try again!!!")

    print("The number of points received are", correct, "out of", questions)


main()