from collections import defaultdict

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:

        R = len(img1)
        C = len(img1[0])
        
        
        def convert(img):
            coords = {}
            for r in range(R):
                for c in range(C):
                    if img[r][c] == 1:
                        coords[(r,c)] = 1
            return coords
        
        
        coords1 = convert(img1)
        coords2 = convert(img2)
        
        def BF(coords1, coords2):
            _max = 0
            for r in range(R):
                for c in range(C):
                    lmax1 = 0
                    lmax2 = 0
                    lmax3 = 0
                    lmax4 = 0                    
                    for k,_ in coords1.items():
                        #print(k)
                        if (k[0]+ r, k[1] + c) in coords2:
                            lmax1 += 1
                        if (k[0] - r, k[1] - c) in coords2:
                            lmax2 += 1                     
                        if (k[0] + r, k[1] - c) in coords2:
                            lmax3 += 1                     
                        if (k[0] - r, k[1] + c) in coords2:
                            lmax4 += 1                                                 
                        _max = max(lmax1, lmax2, lmax3, lmax4, _max)
            return _max
        
        return BF(coords1, coords2)