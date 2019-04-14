def ext(Arr, div=None):
    if (div == None):
        div = []
    Arr.sort()
    for i in range(0, len(Arr)):
        for j in range(i + 1, len(Arr)):
            res = Arr[j] / Arr[i]
            if (res not in Arr) and (res not in div):
                div.append(res)
    if(len(div) != 0):
        Arr = Arr + div
        return ext(Arr, [])
    else:
        length = len(Arr)
        return length, Arr


Arr = [2, 56, 87, 24, 256]
a, b = ext(Arr)
print a, b
