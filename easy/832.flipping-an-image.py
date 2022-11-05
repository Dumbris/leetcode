class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        R = len(image)
        C = len(image[0])
        for r in range(R):
            #print(r)
            for c in range((C+1)//2):
                #print(c)
                image[r][c], image[r][C-c-1] = image[r][C-c-1]^1, image[r][c]^1
        return image
        