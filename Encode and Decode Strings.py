class Solution:
    def encode(self, s):
        return "▓".join(s)

    def decode(self, s):
        return s.split("▓")



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    tc = int(input())  # Number of test cases

    for _ in range(tc):
        input_str = input().split(' ')

        obj = Solution()
        encoded_string = obj.encode(input_str)
        decoded_strings = obj.decode(encoded_string)

        # Printing the decoded strings
        print(" ".join(decoded_strings))
        print("~")

# } Driver Code Ends