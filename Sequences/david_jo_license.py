# David Jo. Assignment 4 "Sequences" Part 1
# Program prupose: To use lists to create a program that tells students whether or not they passed theirwritten driver's license exam

def main():

    answer_key = ["A", "C", "A", "A", "D", "B", "C", "A", "C", "B", "A", "D", "C", "A", "D", "C", "B", "B", "D", "A"]

    questions_answered_incorrectly = []
    student_answers = ["No_answer"] * len(answer_key)
    num_correct_student_answers = 0

    for i in range(len(answer_key)):
        student_answers[i] = input(f"Enter your answer for question {i+1}: ")
        if student_answers[i] == answer_key[i]:
            num_correct_student_answers += 1
        else:
            questions_answered_incorrectly.append(i+1)

    print("Number of correct answers: ", num_correct_student_answers)
    print("Number of incorrect answers: ", len(answer_key) - num_correct_student_answers)
    if num_correct_student_answers >= 15:
        print("You passed the exam!")
    else:
        print("You did not pass the exam.")

    print(f"Questions answered incorrectly: {questions_answered_incorrectly}")



if __name__ == "__main__":
    main()