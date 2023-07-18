def findInt(arr):
    output=0
    for i in arr:
        output^=i
    return output

print(findInt(list(map(int,input().split()))))