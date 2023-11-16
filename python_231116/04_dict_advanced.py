son_dict = {
    'name': '손흥민',
    'age': 29,
    'address': ['대한민국', '영국', '독일']
}

print(son_dict['name']) # 값 가져오기
son_dict['job'] = 'football player' # 데이터 추가
son_dict['name'] = 'son' # 데이터 수정
del son_dict['address']

print(son_dict)