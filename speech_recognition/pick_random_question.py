#! /usr/bin/env python

import csv
import random
from termcolor import colored
from collections import OrderedDict

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

answering = OrderedDict()

with open("speech_recognition_questions.csv") as f:
    reader = csv.DictReader(f, delimiter=";")

    questions = list(reader)
    random.shuffle(questions)

    for direct in range(5):
        question_index = direct + 1
        q = questions.pop()
        dict_key = "{0}: {1}".format(question_index, q["Question"])

        print "Stand in FRONT of the robot "
        print bcolors.OKGREEN + "Question {0}: {1}.   ----> {2}".format(question_index, q["Question"], q["ANSWER"]) + bcolors.ENDC
        key = raw_input("Correct answer? " + colored("c = correct", 'green') + ", " + colored("i = incorrect: ", 'red')).strip()

        if key == "c":
            answering[dict_key] = 10
        elif key == "i":
            answering[dict_key] = 0
        else:
            print "Key not allowed"


        print answering
        print "-" * 20
        print

    print "#" * 20

    for indirect in range(5):
        question_index = indirect + 1
        q = questions.pop()

        dict_key = "{0}: {1}".format(question_index, q["Question"])

        print "Step BEHIND the robot."

        print bcolors.OKGREEN + "Question {0}: {1}.   ----> {2}".format(question_index, q["Question"], q["ANSWER"]) + bcolors.ENDC
        # key = raw_input("Correct answer? c = correct, i = incorrect, r = repeat: ")
        key = raw_input("Correct answer? " + colored("c = correct", 'green') + ", " + colored("i = incorrect: ", 'red') + ", " + colored("r = repeat: ", 'blue')).strip()
        if key == "c":
            answering[dict_key] = 20
        elif key == "i":
            answering[dict_key] = 0
        elif key == "r":
            print bcolors.OKGREEN +"Question {0}, 2nd attempt: {1}.   ----> {2}".format(question_index, q["Question"], q["ANSWER"]) + bcolors.ENDC
            # key = raw_input("Correct answer in 2nd attempt? c = correct, i = incorrect: ")
            key = raw_input("Correct answer in 2nd attempt? " + colored("c = correct", 'green') + ", " + colored("i = incorrect: ", 'red')).strip()
            if key == "c":
                answering[dict_key] = 10
            elif key == "i":
                answering[dict_key] = 0
            else:
                print "Key not allowed"
        else:
            print "Key not allowed"

        print answering
        print "-" * 20
        print

    for question, score in answering.iteritems():
        print question, score

    total_score = sum(answering.values())
    print "TOTAL SCORE: {0}".format(total_score)