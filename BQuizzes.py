import shelve
import random
import os
quizNum = 0
while quizNum < 50:
  shelfFile = shelve.open('uscapitals')  # open file containing dictionary of US Capitals
  capitals = shelfFile['capitals']  # stored dictionary

  # .txt file names (you can modify if you wish, but careful how you do it)
  quizname = 'quiz' + str(quizNum) + '.txt'
  keyfile = 'key' + str(quizNum) + '.txt'

  # 1. Open 2 files that you will write to, a quiz and an answer key file
  quiz = open('quizname', 'w')
  key = open('keyfile', 'w')
  
  # 2. Write headings on both files
  quiz.write("Name: \nDate: \nCapitals Quiz\n")
  key.write("Capitals Quiz Answer Key\n")

  # the following creates a list of states, and then puts them in a random order
  states = list(capitals.keys())
  random.shuffle(states)  # reorder states for each quiz

  for questionNum in range(50):  # loop through each of the 50 states
    mcoptions = []
    correct = capitals[states[questionNum]]  # find correct capital from capitals dictionary; states[questionNum] is current state

    # create a list of possible wrong answers for the state
    wrong = list(capitals.values())  # start with all capitals
    
    # 3. Wrong currently contains all 50 capitals. You will need to remove the correct capital from that list.
    wrong.remove(correct)

    # 4. A multiple choice quiz generally as a couple of wrong choices along with the correct choice. Create a list of multiple choice options. Start by randomly selecting 3 or 4 (or more, if you wish) wrong choices
    wrongchoice1 = random.sample(wrong, 3)
    mcoptions.extend(wrongchoice1)

    # 5. Add the correct answer to your list of multiple choice options.
    mcoptions.append(correct)



    # 6. Make sure you shuffle the options for the multiple choice (otherwise, the correct answer will always be the last choice)
    random.shuffle(mcoptions)


    # 7. Write the question to the quiz (It should at least include the state itself and possibly the questions number)
    # Reminder: states[questionNum] is the current state
    question = (str(questionNum+1), '. What is the capital of ', states[questionNum], '?')
    question1 = ''
    for item in question:
      question1 = question1 + item
    quiz.write(question1 + "\n")


    # 8. Write the answer choices to the quiz. Choices are usually labeled A, B, C, D. It can be done with a loop (which is much easier), but doesn't have to be.
    mcoption0 = str(mcoptions[0])
    mcoption1 = str(mcoptions[1])
    mcoption2 = str(mcoptions[2])
    mcoption3 = str(mcoptions[3])
    op1=("a. " + mcoption0)
    op2=("b. " + mcoption1)
    op3=("c. " + mcoption2)
    op4=("d. " + mcoption3)

    quiz.write(op1 + "\n")
    quiz.write(op2 + "\n")
    quiz.write(op3 + "\n")
    quiz.write(op4 + "\n")
    

    # 9. Write the correct answer to the answer key file. 
    newnum = questionNum + 1
    newnumstr = str(newnum)
    finalnumstr = newnumstr + ". "
    key.write(finalnumstr)
    key.write(correct+ "\n")
    


  # 10. After completely writing both the quiz and the answer key, make sure to close both files.
  quiz.close()
  key.close()
  quizNum = quizNum + 1

  os.rename('quizname', 'quizname' + str(quizNum) )
  os.rename('keyfile', 'keyfile' + str(quizNum) )

  # Hopefully you were able to generate one 50 question quiz. Can you modify this to generate multiple 50 question quizzes (hint: it does involve a loop)
