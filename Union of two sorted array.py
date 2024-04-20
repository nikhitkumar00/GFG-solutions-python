class Solution:

    def findUnion(self, arr1, arr2, n, m):

        i = 0
        j = 0
        k = 0
        out = []
        track = set()

        while i < n and j < m:
            if arr1[i] <= arr2[j]:
                if arr1[i] not in track:
                    track.add(arr1[i])
                    out.append(arr1[i])
                i += 1

            elif arr1[i] > arr2[j]:
                if arr2[j] not in track:
                    track.add(arr2[j])
                    out.append(arr2[j])
                j += 1

            k += 1

        while i < n:
            if arr1[i] not in track:
                track.add(arr1[i])
                out.append(arr1[i])
                k += 1
            i += 1

        while j < m:
            if arr2[j] not in track:
                track.add(arr2[j])
                out.append(arr2[j])
                k += 1
            j += 1

        return out

if __name__ == "__main__":
    test_cases = int(input())
    for cases in range(test_cases):
        n, m = map(int, input().strip().split())
        a = list(map(int, input().strip().split()))
        b = list(map(int, input().strip().split()))
        ob = Solution()
        li = ob.findUnion(a, b, n, m)
        for val in li:
            print(val, end=" ")
        print()
