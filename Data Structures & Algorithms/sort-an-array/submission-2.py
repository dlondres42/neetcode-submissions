# implementar merge sort recursivamente
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums) - 1
        self.mergeSort(nums, l, r)

        return nums

    def mergeSort(self, nums, l, r):
        if l >= r:
            return nums
        
        mid = (l + r) // 2
        self.mergeSort(nums, l, mid)
        self.mergeSort(nums, mid + 1, r)
        self.merge(nums, l, mid, r)


    def merge(self, nums, l, mid, r):
        l_array = nums[l:mid + 1]
        r_array = nums[mid + 1:r + 1]
        
        i = 0 # l_array pointer
        j = 0 # r_array pointer
        k = l # k inicializado ao comeco do array
        while i < len(l_array) and j < len(r_array):
            if l_array[i] <= r_array[j]:
                nums[k] = l_array[i]
                i += 1
                k += 1
            else:
                nums[k] = r_array[j]
                j += 1
                k += 1

        if i < len(l_array): nums[k:r + 1] = l_array[i:]
        if j < len(r_array): nums[k:r + 1] = r_array[j:]
