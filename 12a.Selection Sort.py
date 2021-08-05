def selectSort(this_arr):
    arrLength = range(0, len(this_arr)-1)
    print("given array is ", this_arr)
    for a in arrLength:
        lowestNum = a
        for x in range (a+1, len(this_arr)):
            if (this_arr[x] < this_arr[lowestNum]):
                # print("index value is ", lowestNum, " before changing")
                lowestNum = x
                # print("index value changed to ", lowestNum)
                # print(this_arr)
        if (lowestNum != a):
                this_arr[lowestNum], this_arr[a] = this_arr[a], this_arr[lowestNum]
                print("new array is ", this_arr)
                print("="*25)
    return this_arr
print(selectSort([21, 6, 84, 37, 23, 87, 34]))