import time # 시간과 관련한 모듈

# 시간을 초단위(UTC)로 반환
print(time.time())

# 연월일시분초 형태로 변환
print(time.localtime())

# 시간을 요일, 월, 일, 시, 분, 초, 연도 순서의 문자열로 반환
print(time.asctime())

# sleep 만큼 딜레이
print('10까지 세기')
time.sleep(10)
print('지금')