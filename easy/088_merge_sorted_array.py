# Time: O(M+N)
# Space: O(M+N)

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        arr = [0]*(m+n)
        i = 0
        j = 0
        k = 0
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                arr[k] = nums1[i]
                k+=1
                i+=1
            else:
                arr[k] = nums2[j]
                k+=1
                j+=1
        while i < m:
            arr[k] = nums1[i]
            k+=1
            i+=1
        while j < n:
            arr[k] = nums2[j]
            k+=1
            j+=1
        # if i>= m:
        #     arr[k:] = nums2[j:]
        # elif j>= n:
        #     arr[k:] = nums1[i:m]
        nums1[:] = arr[:]