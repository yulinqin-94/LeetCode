class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1
        B = nums2
        Ai = 0
        Bi = 0
        Aj = len(A) - 1
        Bj = len(B) - 1
        count = len(A) + len(B)
        if len(A)==0 and len(B)!=0:
            C = B
        elif len(B)==0 and len(A)!=0:
            C = A
        elif len(B)==0 and len(A)==0:
            res = None
            return res
        else:
            while Ai<=Aj and Bi<=Bj and count>2 and len(A)!=0 and len(B)!=0:
                if A[Ai] <= B[Bi]:
                    Ai += 1
                    count -= 1
                else:
                    print(B[Bi])
                    Bi += 1
                    count -= 1
                if A[Aj] >= B[Bj]:
                    Aj -= 1
                    count -= 1
                else:
                    print(B[Bj])
                    Bj -= 1
                    count -= 1
            if Ai == Aj and Bi == Bj:
                res = (A[Ai] + B[Bi])/2
                return res
            elif Ai <= Aj or Bi <= Bj:
                if Ai <= Aj:
                    C = A[Ai:Aj+1]
                elif Bi <= Bj:
                    C = B[Bi:Bj+1]
        if len(C)%2 == 0:
            res = (C[int(len(C)/2 - 1)] + C[int(len(C)/2)])/2
        else:
            res = C[int((len(C)-1)/2)]
        return res