# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        def mergeSortB(pairs, s, e):
            if e - s + 1 <= 1:
                return pairs
            
            m = math.floor((s+e)/2)
            mergeSortB(pairs, s, m)
            mergeSortB(pairs, m+1, e)

            merge(pairs, s, m, e)
            return pairs

        def merge(pairs, s, m, e):
            Left = pairs[s:m+1]
            Right = pairs[m+1:e+1]

            i = 0
            j = 0
            k = s

            while i < len(Left) and j < len(Right):
                if Left[i].key <= Right[j].key:
                    pairs[k] = Left[i]
                    i += 1
                else:
                    pairs[k] = Right[j]
                    j += 1
                k += 1

            while i < len(Left):
                pairs[k] = Left[i]
                i += 1
                k += 1
            while j < len(Right):
                pairs[k] = Right[j]
                j += 1
                k += 1
            return pairs

        return mergeSortB(pairs, 0, len(pairs)-1)