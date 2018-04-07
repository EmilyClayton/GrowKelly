import os
import string

def readFile(path):
    with open(path, "rt") as f:
        return f.read()
        
def validEntry(entry, type):
    entry = entry.replace(" ", "")
    notValid = 0
    for num in entry.split(","):
        if num.isdigit():
            if int(num) in (list(range(1, 7)) + list(range(8, 12)) + list(range(13, 16))):
                continue
        num = num.lower()
        if num == "final":
            continue
        notValid += 1
    if notValid != 0:
        return False
    else:
        createWeeks(entry, type)
        return True
        
def createWeeks(entry, type):
    for num in entry.split(","):
        if num.isdigit():
            if type == "Week":
                Week(num)
            elif type == "Midterm":
                Midterm(num)
        num = num.lower()
        if num == "final":
            Midterm("final")

class Weeks(object):
    all = []
    def __init__(self, number):
        self.number = number
        self.path = "Week%d.txt" % self.number
        self.contents = readFile(self.path)
        Weeks.all.append(self)
        
    def getQuestions(self):
        contents = readFile(self.path)
        count = contents.replace('\n', '')
        questions = []
        for phrase in range(len(count.split("&"))):
            if phrase % 5 == 0:
                 questions.append(count.split("&",phrase))
        return questions
        
    def getWrong(self):
        contents = readFile(contents)
        count = contents.split("\n")
        length = len(count[0])
        wrong = []
        for phrase in count.split("&"):
            group = []
            for number in range(2):
                if phrase % (length + 1) != 0 and phrase % (length + 1) != 0:
                    group.append(phrase)
            wrong.append(group)
        return wrong
        
    def getCorrect(self):
        contents = readFile(contents)
        correct = []
        count = contents.split("\n")
        length = len(count[0])
        for phrase in count.split("&"):
            if phrase % (length + 2) != 0:
                 correct.append(phrase)
        return correct

class Midterm(object):
    all = []
    def __init__(self, midterm):
        self.midterm = midterm
        if self.midterm == 1:
            self.weeks = list(range(1, 7))
        elif self.midterm == 2:
            self.weeks = list(range(8, 12))
        elif self.midterm == "final":
            self.weeks = list(range(1, 7)) + list(range(8, 12)) + list(range(13, 15))
        Midterm.all.append(self)
            
    def getQuestions(self):
        midtermQuestions = []
        for week in Week.all:
            if week.number in self.weeks:
                midtermQuestions.append(week.getQuestions())
        return midtermQuestions
    
    def getWrong(self):
        wrong = []
        for week in Week.all:
            if week.number in self.weeks:
                wrong.append(week.getWrong())
        return wrong
        
    def getCorrect(self):
        correct = []
        for week in Week.all:
            if week.number in self.weeks:
                correct.append(week.getCorrect())
        return correct