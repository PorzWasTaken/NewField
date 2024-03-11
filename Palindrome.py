class Solution(object):
    def isPalindrome(self, x):
        # Check for negative numbers and numbers ending with 0
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        
        # Initialize a variable to store the reversed second half of the number
        reversed_half = 0
        
        # Reverse the second half of the number
        while x > reversed_half:
            # Take the last digit of x and append it to the end of reversed_half
            reversed_half = (reversed_half * 10) + (x % 10)
            # Remove the last digit from x
            x = x // 10
        
        # Check if the reversed second half equals the first half of the number
        # If the number has odd length, compare x with reversed_half // 10 to ignore the middle digit
        return x == reversed_half or x == reversed_half // 10

        # Initially, reversed_half = 0
        # 1st iteration: reversed_half = (0 * 10) + (12321 % 10) = 1, x = 1232
        # 2nd iteration: reversed_half = (1 * 10) + (1232 % 10) = 12, x = 123
        # 3rd iteration: reversed_half = (12 * 10) + (123 % 10) = 123, x = 12
        # 4th iteration: reversed_half = (123 * 10) + (12 % 10) = 1232, x = 1
        # 5th iteration: reversed_half = (1232 * 10) + (1 % 10) = 12321, x = 0

        # Since x (0) is no longer greater than reversed_half (12321), the loop terminates

        # At this point, reversed_half contains the reversed second half of the original number (12321)
