import copy

movie = ['서울의봄', '싱글인서울']
trend = ['슬릭백', '스모크', movie] # ['슬릭백', '스모크', ['서울의봄', '싱글인서울']]

my_trend = copy.deepcopy(trend) # 깊은 복사
# my_trend = trend[:] # 얇은 복사

print(trend == my_trend)
print(trend is my_trend)

trend.append('이두나')
movie.append('독전2')
print(trend)
print(my_trend)