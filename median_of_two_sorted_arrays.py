from typing import List


class Solution:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(nums1) > len(nums2):
            A, B = B, A
        l, r = (0, len(A)-1)
        t  = len(A)+len(B)
        h = t//2

        while True:
            i = (l + r) // 2
            j = h - i - 2
            al = A[i] if i >= 0 else float('-inf')
            bl = B[j] if j >= 0 else float('-inf')
            ar = A[i+1] if i+1 < len(A) else float('inf')
            br = B[j+1] if j+1 < len(B) else float('inf')
            if al <= br and bl <= ar:
                if t % 2 == 0:
                    return (max(al,bl)+min(ar,br))/2
                else:
                    return min(ar,br)
            else:
                if al > br:
                    r = i -1
                else:
                    l = i + 1


if __name__ == '__main__':
    s = Solution()
    nums1 = [1, 2, 3, 4]
    nums2 = [5, 6, 7]
    print(s.findMedianSortedArrays(nums1, nums2))