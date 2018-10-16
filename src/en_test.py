# -*- coding: utf-8 -*-

import random
import json
import config

__author__ = "dsm_helper"

enter_year = input("입학년도를 입력해주세요 ex) 2017 >> ")
semester = input("학기를 입력해주세요 ex) 1st >> ")
file_name = input("파일명을 입력해주세요 ex) 01 >> ")

with open(f'../data/dsm{enter_year}/{semester}/{file_name}.json', 'r', encoding="UTF8") as f:
    words = json.load(f)

check = True
count = 0

while True:
    if len(words) == 0:
        break

    if check:
        answer, meaning = random.choice(list(words.items()))
        check = False
        print(meaning)

    question = input("I think.. >> ")

    if question == answer:
        check = True
        count = 0
        words.pop(answer)
        print(config.CORRECT_MESSAGE.format(count=len(words)))
    elif question != answer:
        print(config.TRY_AGAIN_MESSAGE)
        count += 1

    if count == 5:
        print(config.FIRST_CHARACTER_HINT.format(answer=answer))
    if count == 7:
        print(config.LENGTH_HINT.format(answer=answer))
    if count == 10:
        print(config.FAILED_MESSAGE.format(answer=answer))
        words.pop(answer)
        check = True

    if question == "exit":
        print(config.EXIT_MESSAGE)
        exit(1)

print(config.END_MESSAGE)
