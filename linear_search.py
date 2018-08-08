"""
Linear search runs in at worst linear time and makes at most n comparisons, 
where n is the length of the list.
"""

# Python code for linearly search x in arr[].  If x
# is present then return its  location,  otherwise 
# return -1
def search(arr, x):
 
    for i in range(len(arr)):
 
        if arr[i] == x:
            return i
 
    return -1