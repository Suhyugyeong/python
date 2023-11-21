
# https://school.programmers.co.kr/
# 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
# 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
# 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
# 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
# 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
# 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
#      만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
# 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.

import re

def process_new_id(new_id):
    # 1단계: 대문자를 소문자로 변환
    new_id = new_id.lower()

    # 2단계: 허용된 문자 이외의 문자 제거
    new_id = re.sub(r'[^a-z0-9-_.]', '', new_id)

    # 3단계: 연속된 마침표를 하나로 치환
    new_id = re.sub(r'\.{2,}', '.', new_id)

    # 4단계: 처음과 끝의 마침표 제거
    new_id = new_id.strip('.')

    # 5단계: 빈 문자열이면 "a" 대입
    if not new_id:
        new_id = 'a'

    # 6단계: 길이가 16자 이상이면 초과 부분 제거 및 마침표 제거
    if len(new_id) >= 16:
        new_id = new_id[:15].rstrip('.')

    # 7단계: 길이가 2자 이하면 마지막 문자 반복
    while len(new_id) <= 2:
        new_id += new_id[-1]

    return new_id

# 테스트
new_id = "ABC_..Def"
result = process_new_id(new_id)
print(result)
