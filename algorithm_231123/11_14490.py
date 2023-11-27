def baek_dae_yeol(n, m):
    # 최대공약수(greatest_common_divisor) 구하기
    def gcd(a, b):
        # if a < b:
        #     a, b = b, a
        while b != 0:
            a, b = b, a % b
        return a
    n_m_gcd = gcd(n, m)
    print(f"{n//n_m_gcd}:{m//n_m_gcd}")
    
import sys
N, M = [int(i) for i in sys.stdin.readline().split(":")]
baek_dae_yeol(N, M)

# 숙제