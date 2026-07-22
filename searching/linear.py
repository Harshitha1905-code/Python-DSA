arr=list(map(int,input().split()))#[10, 25, 7, 40, 15]
target=int(input())#40
for i in range(len(arr)):#5#2#3#4
    if arr[i]==target:#15==60
        print("Element found at index",i)#Element found at index 3
        break
else:
    print("Element not found")#0(1)

#using functions
def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1
arr=list(map(int,input().split()))
target=int(input())
result=linear_search(arr,target)
print(result)
