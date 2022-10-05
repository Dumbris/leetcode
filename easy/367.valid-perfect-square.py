class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        def binary_search(low, high, x):
        # Check base case
            if high >= low:

                mid = (high + low) // 2
                #print(mid)

                # If element is present at the middle itself
                if mid*mid == x:
                    return True

                # If element is smaller than mid, then it can only
                # be present in left subarray
                elif mid*mid > x:
                    return binary_search(low, mid - 1, x)

                # Else the element can only be present in right subarray
                else:
                    return binary_search(mid + 1, high, x)

            else:
                # Element is not present in the array
                return False
 
        # Test array
        #arr = list(range(0,num+1))
        
 
        # Function call
        result = binary_search(0, num, num)
        
        return result
        