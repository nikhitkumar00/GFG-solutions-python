# {
# Driver Code Starts


# } Driver Code Ends
def reverse(S):

    l = [i for i in S]
    out = ""

    while l:
        out += l.pop()

    return out


# {
# Driver Code Starts.
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        str1 = input()
        print(reverse(str1))
# } Driver Code Ends
