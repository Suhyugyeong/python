#재귀적인 방식과 메모이제이션을 사용하여 파스칼의 삼각형을 생성하는 클래스 Solutuon을 정의
class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        # 탑다운! 재귀! 메모이제이션!
        
        if numRows ==  1:
            return [[1]]
        triangle = self.generate(numRows-1)
        # 이전까지의 파스칼의 삼각형 가져오기 (triangle)
        prev = triangle[-1]
        # 이전까지의 파스칼의 삼각형에서 가장 마지막 줄 가져오기 (prev)
        new_row = []
        new_row.append(1)
        for i in range(1, len(prev)): 
            new_row.append(prev[i-1] + prev[i])
            #새로운 행을 생성
            #첫번째 값은 항상 1, 그 후로는 이전 행의 두값씩 더해 새로운 행을 만듦
        new_row.append(1)
        triangle.append(new_row)
        return triangle
    
    # 바텀업 방식과 유사한 결과를 얻지만, 재귀적인 방식으로 구현되어 있습니다.