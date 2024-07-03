"""
Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.
The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.
"""
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

        