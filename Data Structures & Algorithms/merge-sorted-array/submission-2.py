class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        while i >= 0 and  j >= 0:
            if nums1[i] > nums2[j]:
                print(f"nums 1 copiado, i = {i}")
                nums1[i + n] = nums1[i]
                i -= 1
            else:
                print(f"nums 2 copiado, i + n = {i + n},j = {j}, nums2[j] = {nums2[j]}")
                nums1[i + n] = nums2[j]
                n -= 1
                j-= 1
            

        if j >= 0:
            nums1[0:j + 1] = nums2[0:j + 1]
