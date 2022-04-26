def default_score(c1, c2):
    return 1 if c1 == c2 else -1
class LocalAlignmentCalculator():
    def __init__(self, S, T, g, score = default_score):
        self.S = S
        self.T = T
        self.g = g
        self.score = score
        
    def calculate(self):
        L = [[0 for _ in range(len(self.T) + 1)] for _ in range(len(self.S) + 1)]
        ans = 0
        for i in range(1, len(self.S) + 1):
            for j in range(1, len(self.T) + 1):
                L[i][j] = max(
                    L[i-1][j-1] + self.score(self.S[i-1], self.T[j-1]),
                    L[i][j-1] - self.g,
                    L[i-1][j] - self.g,
                    0
                )
                ans = max(ans, L[i][j])
        print(L)
        return ans

if __name__=='__main__':
    cal = LocalAlignmentCalculator(["hi", "hello", "this", "is", "kien"], ["hi", "hello", "trin", "is", "kien"], 1)
    print(cal.calculate())
    
    