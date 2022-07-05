class Solution:
     def solve(self, nums):
      res = {}
      for i in nums:
         try:
            res[i] += 1
         except:
            res[i] = 1
      for k, v in res.items():
         if k == v:
            return True
      return False