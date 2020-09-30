"""
SET q_count TO 1
SET q_types TO ['sub', 'add']
SET correct_ans TO 0

generateQ():
  SET q_type TO random choice in q_types
  IF q_type == 'sub'
    num1 = random integer between 0,10
    num2 = random integer between 0,10
    question = str (num1 + num2)
    DISPLAY question
  ELSE IF q_type == 'add':
    num1 = random integer between 0,10
    num2 = random integer between 0,10
    question = str (num1 + num2)
    DISPLAY question

checkAns():
  <convert users answer to integer>
  IF user answer is == to correct answer THEN
    DISPLAY 'correct!'
    increment correct_ans
  ELSE
    DISPLAY 'incorect'

loop while q_count is <= 4:
  increment q_count
  DISPLAY ("Question {0}:").format(q_count)
  generateQ()
  RECIEVE answer FROM USER
  checkAns()

IF q_count == 4 THEN 
  DISPLAY correct_ans
"""

import random

q_count = 0
q_types = ['sub', 'add']
correct_answers = 0
user_answer = None

def generateQuestion():
  global q_type
  global num1
  global num2
  q_type = random.choice(q_types)
  if q_type == 'sub':
    num1 = random.randint(1,10)
    num2= random.randint(1,10)
    question = str(num1) + ' - ' + str(num2)
    print(question)
  else:
    num1 = random.randint(1, 10)
    num2= random.randint(1,10)
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
  print(f"Question {q_count}: ")
  generateQuestion()
  user_answer = int(input("Your answer: "))
  checkAns()

if q_count == 5:
  print(f"\nYou got {correct_answers} questions(s) correct.")