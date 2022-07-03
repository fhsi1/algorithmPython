class Solution:
    def solve(self, strs):
        result = list()
        tmp = list()
        for i in strs:
            if i == "red":
                result.append(i)
            else:
                tmp.append(i)
        
        for i in tmp:
            if i == "green":
                result.append(i)
            else:
                continue
        
        for i in tmp:
            if i == "blue":
                result.append(i)

        return result