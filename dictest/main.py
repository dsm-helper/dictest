# -*- coding: utf-8 -*-

import random
import json
import config

__author__ = "dsm_helper"


def get_quiz_data_from_input():
    return input("입학년도를 입력해주세요 ex) 2017 >> "), input("학기를 입력해주세요 ex) 1st >> "), input("파일명을 입력해주세요 ex) 01 >> ")


def get_words_by_info(enter_year, semester, file_name):
    try:
        with open(f'../data/dsm{enter_year}/{semester}/{file_name}.json', 'r', encoding="UTF8") as f:
            words = json.load(f)
        return words
    except Exception as e:
        print("잘못된 입력입니다. 다시 확인해주세요.")
        print(e)
        exit(1)

if __name__ == "__main__":

    enter_year, semester, file_name = get_quiz_data_from_input()

    check = True
    count = 0
    words = get_words_by_info(enter_year, semester, file_name)

    def finish_quiz():
        print(config.EXIT_MESSAGE)
        exit(1)

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
            finish_quiz()

    print(config.END_MESSAGE)
