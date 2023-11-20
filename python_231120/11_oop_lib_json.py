import json

son_dict = {
    'name': 'SON',
    'age': 29,
    'address': ['KOR', 'ENG', 'GER']
}
son_json = json.dumps(son_dict)
print(type(son_json))

lee_json = '{"name": "LEE", "age": 25, "address": ["KOR"]}'
lee_dict = json.loads(lee_json)
print(type(lee_dict))
