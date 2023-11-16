son_dict = {
    'name': '손흥민',
    'age': 29,
    'address': ['대한민국', '영국', '독일']
}

print(son_dict.keys()) # key만을 모아서 반환
print(son_dict.values()) # value만을 모아서 반환
print(son_dict.items()) # key와 value를 튜플로 묶어서 반환

print(son_dict.get('name')) # 키가 name인 value 반환
print(son_dict.get('job')) # 키가 job인 value 반환(없어서 None)
print(son_dict.get('job', '무직')) # 키가 job인 value 반환(없어서 '무직')
print('address' in son_dict) # 키 address 존재 유무

for k, v in son_dict.items():
    print(f"Key : {k}, Value: {v}")
    
son_dict.clear()
print(son_dict)