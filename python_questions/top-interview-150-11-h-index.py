class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        N = len(citations)
        h = N
        if citations[-1] == 0:
            h = 0
        else:
            for x in citations:
                if x >= N:
                    h = N
                    break
                else:
                    N = N - 1
        
        return h

        