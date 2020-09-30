import random

q_count = 0
q_types = ['sub']
correct_answers = 0
user_answer = None

def generateQuestion():
  global q_type
  global num1
  global num2
  q_type = random.choice(q_types)
  if q_type == 'sub':
    num1 = 7
    num2 = 2
    question = str(num1) + ' - ' + str(num2)
    print(question)
  else:
    num1 = 7
    num2 = 2
    question = str(num1) + ' + ' + str(num2)
    print(question)

def checkAns():
  global correct_answers
  if q_type == 'sub':
    correct_ans = num1 - num2
    if user_answer == correct_ans:
      print("Correct!\n")
      correct_answers = correct_answers + 1
    else:
      print("Incorrect\n")
  else:
    correct_ans = num1 + num2
    if user_answer == correct_ans:
      print("Correct!\n")
      correct_answers = correct_answers + 1
    else:
      print("Incorrect\n")

# main
while q_count < 5:
  q_count = q_count + 1
  print("Question {}: ".format(q_count))
  generateQuestion()
  user_answer = int(input("Your answer: "))
  checkAns()

if q_count == 5:
  print("\nYou got {} questions(s) correct.".format(correct_answers))