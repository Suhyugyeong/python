def solution(record):
    answer = []
    user_info = {}
    for i in record:
        command, uid, *_ = i.split()
        if command == "Enter":
            nickname = i.split()[2]
            user_info[uid] = nickname
        elif command == "Leave":
            pass
        elif command == "Change":
            nickname = i.split()[2]
            user_info[uid] = nickname
    
    for i in record:
        command, uid, *_ = i.split()
        if command == "Enter":
            answer.append(user_info[uid] + "님이 들어왔습니다.")
        elif command == "Leave":
            answer.append(user_info[uid] + "님이 나갔습니다.")
    return answer

record = [
    "Enter uid1234 Muzi",
    "Enter uid4567 Prodo",
    "Leave uid1234",
    "Enter uid1234 Prodo",
    "Change uid4567 Ryan"]

print(solution(record))
