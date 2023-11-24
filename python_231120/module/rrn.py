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
        #주민번호 3,4는 20년대생이니까...
    else:
        year = '19' + year
    return int(year), int(month), int(day)

def hidden_rrn(data):
    import re
    if len(data) == 14 and re.match("^\d{6}-\d{7}", data):
        #정규표현식으로 data가 해당 조건과 일치하는지 검사..
        data = data[:8] + "******"
        return data 
    else:
        raise Exception("주민번호 형식이 잘못되었습니다.")
    #raise는 개발자가 직접 예외를 일으킨다..
    
        
if __name__ == "__main__":
#이 부분은 스크립트가 직접 실행될 때 (모듈이 아닌 경우) 아래의 코드 블록을 실행하라는 것을 나타냅니다.
#이는 보통 모듈로 사용될 때에는 실행되지 않고, 직접 실행될 때만 실행되게끔 하는 관습적인 코드입니다.
    try:
        data = input("주민번호를 입력하세요").replace(" ", "-")
        print(hidden_rrn(data))
        print(gender(data))
        print(birth(data))
    except Exception as e:
        print(e)