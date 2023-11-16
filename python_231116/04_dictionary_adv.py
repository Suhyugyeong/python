park_dict = {
    "name" : "박명수",
    "age" : 50,
    "address" : ["대한민국", "군산출생", "서울거주"]
}

print(park_dict["name"])
park_dict["job"] = "comedian" #추가
park_dict["name"] = "박거성" #데이터  수정
del park_dict["address"]
print(park_dict)