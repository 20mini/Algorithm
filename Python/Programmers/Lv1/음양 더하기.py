#https://school.programmers.co.kr/learn/courses/30/lessons/76501?language=python3

def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        answer+=absolutes[i] if signs[i] else -absolutes[i]
    return answer