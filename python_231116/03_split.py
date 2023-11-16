# split() : 문자열 쪼개기
# (특정 문자를 기준으로 문자열을 나누어 리스트로 반환!)
"2023-11-16".split("-")
"2023 11 16".split()

YYYY, MM, DD = [int(i) for i in input().split()]