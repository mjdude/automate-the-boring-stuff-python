#! python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key

import random

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
            'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
            'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
            'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
            'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
            'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
            'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
            'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
            'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
            'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
            'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
            'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
            'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
            'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

for quizNum in range(35):
    # Each quiz , what is the capital of random <state>
    # is it random selection of 4 capitals
    # TODO: Create the quiz and answer key files.
    quizFile = open('quiz %s.txt' % quizNum, 'a')
    answerFile = open('answer %s.txt' % quizNum, 'a')

    # TODO: Write out the header for the quiz.
    quizFile.write('Quiz %s ' % quizNum)

    # TODO: Shuffle the order of the states.
    states = list(capitals.keys())
    random.shuffle(states)

    # TODO: Loop through all 50 states, making a question for each.
    for questionNum in range(50):
        question = 'What is the capital of ' + states[questionNum] + '\n'
    
    # TODO: Create right and wrong answers for each
        capitalList = list(capitals.values())
        rightAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        # remove correct answer as not to select it
        del wrongAnswers[wrongAnswers.index(rightAnswer)]

        wrongAnswers = random.sample(wrongAnswers,3)
        answersOptions = wrongAnswers + [rightAnswer]

        random.shuffle(answersOptions)       

    # TODO: Write the question and answer options to the quiz file.

        quizFile.write(question)
        for i in range(4):
            answer = '%s. %s \n' % ('ABCD'[i] , answersOptions[i])
            quizFile.write(answer)
        
    # TODO: Write the answer key to a file.
        answerFile.write('Answer for %s is %s \n' % (questionNum , rightAnswer))

    quizFile.close()
    answerFile.close()

    
