def checkProgression(arr):
    arr.sort()

    if len(arr) <=2:
        return True
    
    d = arr[1] - arr[0]

    for i in range(2, len(arr)):
        if arr[i] - arr[i - 1] != d:
            return False
        else:
            return True
        

#test cases
if __name__ == "__main__":
    tests = [
        ([3, 5, 1], True),
        ([1, 2, 4], False),
        ([1, 3, 5], True)
    ]


    

