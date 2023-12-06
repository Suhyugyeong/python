from datetime import datetime, timedelta

def solution(today, terms, privacies):
    today_date = datetime.strptime(today, "%Y.%m.%d")
    to_destroy = []

    for idx, (collection_date, term) in enumerate(zip(privacies, terms), start=1):
        collection_date = datetime.strptime(collection_date, "%Y.%m.%d")
        expiration_date = collection_date + timedelta(days=int(term) - 1)

        if today_date > expiration_date:
            to_destroy.append(idx)

    return to_destroy

# 예시
today = "2022.05.19"
terms = ["6", "12", "3", "3"]
privacies = ["2021.05.02", "2021.07.01", "2022.02.19", "2022.02.20"]

result = solution(today, terms, privacies)
print(result)
