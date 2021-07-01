# move all the the instances of given number to end inplace
# approach1: O(nlogn): sort the array and find the count of instances and move to end.(sliding window)
# approach2: O(n): two pointers
def move_element_to_end(arr, ele):
    l, r = 0, len(arr)-1
    while l<r:
        while l<r and arr[r] == ele:
            r-=1
        if arr[r]==ele:
            arr[l], arr[r]= arr[r], arr[l]
        l+=1
    return arr







