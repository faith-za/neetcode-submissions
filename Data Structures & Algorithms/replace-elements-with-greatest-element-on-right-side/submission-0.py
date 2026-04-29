
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for idx, num in enumerate(arr):
            new_arr = arr[idx+1:len(arr)]
            
            if idx == len(arr)-1:
                max_num = -1
            else:
                max_num = max(new_arr)
                
            arr[idx] = max_num
        return arr

