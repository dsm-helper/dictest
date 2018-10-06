# -*- coding: utf-8 -*-

import random
import json

select = input("Input words file name >> ")

with open(f'./words/{select}.json', 'r', encoding="UTF8") as f:
    words = json.load(f)

check = True
count = 0

while True:
    if len(words) == 0:
        break

    if check:
        temp = random.choice(list(words.items()))
        check = False
        print(temp[1])

    question = input("I think.. >> ")

    if question == temp[0]:
        print(f"정답! {len(words)-1}문제 남았습니다!")
        check = True
        count = 0
        words.pop(temp[0])
    elif question != temp[0]:
        print("다시 생각해~")
        count += 1

    if count == 5:
        print(f"힌트 드릴게요.. 첫 번째 글자는 {temp[0][0]}입니다.")
    if count == 7:
        print(f"아직도 못 맞추셨어요? 단어의 길이는 {len(temp[0])}입니다.")
    if count == 10:
        print(f"안타깝네요.. 정답은 {temp[0]} 였습니다.")
        words.pop(temp[0])
        check = True

    if question == "exit":
        print("Bye~~")
        exit(1)

print("끝!!")
