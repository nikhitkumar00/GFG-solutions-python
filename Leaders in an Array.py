def leaders(A,N):
    st = []
    maxx = 0
    for i in range(N-1,-1,-1):
        if A[i] >= maxx:
            st.insert(0,A[i])
        maxx = max(maxx,A[i])
    return st

n = 6
A = [6,5,4,3,2,1]
print(leaders(A,n))