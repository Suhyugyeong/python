#주어진 숫자 배열을 조합하여 만들 수 있는 가장 큰 수를 문자열로 반환하는 함수
class Solution:
    def largest_number(self, nums: list[int]) -> str:
        nums = [str(i) for i in nums]        
        #숫자를 문자열로 변환
        nums.sort(key=lambda x:(x*9), reverse=True)
        #각 숫자를 9번 반복한 문자열을 비교기준으로 사용하여 내림차순으로 정렬
        #reverse=True를 통해 정렬된 결과를 역순으로 반환(sort함수는 원래 오름차순이니께 내림차순)
        # nums = ''.join(nums)
        # if nums[0] == '0':
        #     return '0'
        # else:
        #     return nums
        return str(int(''.join(nums)))
    #문자열로 변환한 이유는 앞에 여러 개의 '0'이 있을 수 있기 때문
    #이를 방지하기 위해 정수로 변환한 후 다시 문자열로 반환합니다.
    
sol = Solution()
nums = [3,30,34,5,9]
result = sol.largest_number(nums)
print(result) #9534330