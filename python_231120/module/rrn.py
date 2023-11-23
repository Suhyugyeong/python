def gender(data):
    gender_num = int(data[7])
    if gender_num % 2 == 0:
        return '여자'
    else: 
        return '남자' 
    
def birth(data):
    year = data[:2]
    month = data[2:4]
    day = data[4:6]
    gender_num = int(data[7])
    if gender_num > 3:
        year = '20' + year
    else:
        year = '19' + year
    return int(year), int(month), int(day)

def hidden_rrn(data):
    import re
    if len(data) == 14 and re.match("^\d{6}-\d{7}", data):
        data = data[:8] + "******"
        return data 
    else:
        raise Exception("주민번호 형식이 잘못되었습니다.")
        
if __name__ == "__main__":
    try:
        data = input("주민번호를 입력하세요").replace(" ", "-")
        print(hidden_rrn(data))
        print(gender(data))
        print(birth(data))
    except Exception as e:
        print(e)