class MyQueue:
    def __init__(self):
        self.arr = []
    
    def push(self, x):
        self.arr.append(x)
     
    def pop(self): 
        return self.arr.pop(0) if self.arr else -1

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        s=MyQueue()
        q=int(input())
        q1=list(map(int,input().split()))
        i=0
        while(i<len(q1)):
            if(q1[i]==1):
                s.push(q1[i+1])
                i=i+2
            elif(q1[i]==2):
                print(s.pop(),end=" ")
                i=i+1
            elif(s.isEmpty()):
                print(-1)
                i=i+1
        print()