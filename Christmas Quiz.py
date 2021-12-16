import json
import os

class Quiz:
    def __init__(self):
        self.allQuestions = []
        self.score = 0
        self.options = {1 : self.runQuiz,
                        2 : self.addQuestion,
                        3 : self.removeQuestion,
                        4 : self.saveQuestionsToFile,
                        5 : self.loadQuestionsFromFile
        }
        print("\n>----< WELCOME TO THE XMAS QUIZ >----<")

    def runQuiz(self):
        self.score = 0
        questionNumber = 1
        if(len(self.allQuestions) == 0):
            print("\nNo Questions currently in the quiz")
            return
        for x in self.allQuestions:
            print("Question ", questionNumber, ": ", x.question)
            questionNumber += 1
            optionsNumber = 1
            for y in x.options:
                print("\n",optionsNumber,": ", y)
                optionsNumber += 1
            answer = 0
            while not 0 < answer <= (len(x.options)):
                try:
                    answer = int(input("\nType the number of the answer you think is correct "))
                except:
                    print("That's not between 1 and ", (len(x.answers) + 1))
            if(answer == x.answer):
                self.score += 1
                print("\nGreat Job! That was correct!")
            else:
                print("I'm afraid that was incorrect. The correct answer was : ", x.options[(x.answer - 1)])
        print("\nYou've reached the end of the quiz!\nYour score was ", self.score,"/",len(self.allQuestions))

    def addQuestion(self):
        question = input("\nWhat is the question? ")
        options = []
        while True:
            tempOption = input("\nWhat are the question options? (Type 'x' when you are happy with the options) ")
            if((tempOption == "x" or tempOption == "X")):
                if(len(options) > 0):
                    break
            else:
                options.append(tempOption)
        answer = 0
        while not 0 < answer <= (len(options)):
            try:
                answer = int(input("\nType the number of the correct answer "))
            except:
                print("That's not between 1 and ", (len(options) + 1))      
        newQuestion = Question(question, options,answer)
        self.allQuestions.append(newQuestion)

    def removeQuestion(self):
        if(len(self.allQuestions) == 0):
            print("\nNo questions to remove")
            return
        questionNumber = 1
        for x in self.allQuestions:
            print("\n",questionNumber," : ",x.question)
            questionNumber += 1
        while True:
            try:
                choice = int(input("\nType the number of the question you want to remove (type '0' to return to menu) "))
                if(choice == 0):
                    return
                else:
                    choice -= 1                    
                    print("\nDeleted question ", self.allQuestions[choice].question)
                    self.allQuestions.pop(choice)
            except:
                print("\nThat's not one of the options")

    def saveQuestionsToFile(self):
        if(os.path.isfile(os.path.join(os.path.dirname(__file__),'christmasQuestions.txt'))):
            answer = ""
            while answer != 'n' and answer != 'y':
                answer = input("\nThere are already questions saved, overwrite them? (y/n) ")
                answer = answer.lower()
            if(answer == 'n'):
                return
        d = dict()
        d['Questions'] = []
        for b in self.allQuestions:
            d['Questions'].append({
                'question': b.question,
                'options': b.options,
                'answer': b.answer
            })
        with open(os.path.join(os.path.dirname(__file__),'christmasQuestions.txt'), 'w') as outfile:        
            json.dump(d, outfile)
        print("\n\t[Saved ",len(self.allQuestions)," questions]")

    def loadQuestionsFromFile(self):
        if(len(self.allQuestions) > 0):
            answer = ""
            while answer != 'n' and answer != 'y':
                answer = input("\nThere are already loaded questions, overwrite them? (y/n) ")
                answer = answer.lower()
            if(answer == 'n'):
                return
            else:
                self.allQuestions.clear()
        with open(os.path.join(os.path.dirname(__file__),'christmasQuestions.txt')) as json_file:
            data = json.load(json_file)
            for p in data['Questions']:
                newQuestion = Question(p['question'], p['options'], p['answer'])
                self.allQuestions.append(newQuestion)
        print("\n\t[Loaded ",len(self.allQuestions)," questions]")

class Question:
    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer
    def getQuestion(self):
        return self.question
    def getAnswer(self):
        return self.answer

quizInstance = Quiz()

while True:
    try:
        choice = int(input("\nWhat do you want to do in your quiz? \n1 - run the quiz\n2 - add a question\n3 - delete questions\n4 - save to file\n5 - load from file\n6 - exit\t"))    
        if(choice == 6):
            break
        else:
            quizInstance.options[int(choice)]()
    except:
        print("\nThat's not a number between 1 and 6")
