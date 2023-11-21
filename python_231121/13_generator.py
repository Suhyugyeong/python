#제너레이터...?
#이게 왜 필요한건데???

def get_natural_num():
    n =  0
    while True:
        n += 1
        yield n

n_num_generator = get_natural_num()

for i in range(10):
    print(next(n_num_generator))