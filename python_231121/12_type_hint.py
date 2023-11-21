def is_even(num : int) -> bool:
    if num % 2 == 0:
        return True
    else:
        return False
    
print(is_even(1))
print(is_even(2))

#type hint 가 틀려도 오류는 안 나지만... 지양하자
#mypy로 오류를 잡아주긴한다..