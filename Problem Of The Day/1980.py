class Solution:
    #Read Cantors Diagonalization from notes to understand this
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        final_num = ''
        for i in range(len(nums)):
            if nums[i][i] == '0':
                final_num+='1'
            else:
                final_num+='0'
        return final_num