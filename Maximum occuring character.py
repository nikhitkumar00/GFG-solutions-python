# User function Template for python3


class Solution:

    # Function to find the maximum occurring character in a string.
    def getMaxOccurringChar(self, s):

        dic = {}
        maxx = 0

        for i in s:

            if i in dic:
                dic[i] += 1

            else:
                dic[i] = 1

            maxx = max(maxx, dic[i])

        out = [char for char, freq in dic.items() if freq == maxx]

        return min(out)


# {
# Driver Code Starts
# Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        s = str(input())
        print(Solution().getMaxOccurringChar(s))
# } Driver Code Ends
