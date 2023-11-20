def gender(data):
    data = data.replace(" ", "").replace("-", "")
    gender_num = int(data[6])
    if gender_num % 2 == 0:
        return '여자'
    else: 
        return '남자' 
    
def birth(data):
    data = data.replace(" ", "").replace("-", "")
    year = data[:2]
    month = data[2:4]
    day = data[4:6]
    gender_num = int(data[6])
    if gender_num > 3:
        year = '20' + year
    else:
        year = '19' + year
    return int(year), int(month), int(day)

if __name__ == "__main__":
    data = input("주민번호를 입력하세요")
    print(gender(data))
    print(birth(data))