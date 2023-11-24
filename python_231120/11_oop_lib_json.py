import json
#JSON 형식의 데이터를 python 데이터 구조로 변환

son_dict = {
    'name': 'SON',
    'age': 29,
    'address': ['KOR', 'ENG', 'GER']
}

son_json = json.dumps(son_dict)
#dumps => dump string : 파이선 문자열로 덤프한다.
print(type(son_json)) #<class 'str'>

lee_json = '{"name": "LEE", "age": 25, "address": ["KOR"]}'
lee_dict = json.loads(lee_json)
#load string : JSON문자열을 파싱하여 파이선 데이터 구조로 변환함
print(type(lee_dict)) #<class 'dict'>
