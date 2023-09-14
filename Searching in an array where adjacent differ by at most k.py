def search(arr, n, x, k):
    return arr.index(x) if x in arr else -1


n, k = map(int, input().split())
arr = list(map(int, input().strip().split()))
x = int(input())
ans = search(arr, n, x, k)
print(ans)
