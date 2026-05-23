class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []

        while len(strs) > 0:
            temp = [strs.pop(0)]
            temp2 = []
            for i in range(len(strs)):
                if len(strs[i]) == len(temp[0]):
                    if self.isAnagram(strs[i], temp[0]):
                        temp.append(strs[i])
                    else:
                        temp2.append(strs[i])
                else:
                    temp2.append(strs[i])
            result.append(temp)
            strs = temp2
        return result

    def isAnagram(self, str1, str2):
        count_1 = {}
        count_2 = {}

        for s in str1:
            if s in count_1:
                count_1[s] += 1
            else:
                count_1[s] = 1
        for s in str2:
            if s in count_2:
                count_2[s] += 1
            else:
                count_2[s] = 1

        return count_1 == count_2

