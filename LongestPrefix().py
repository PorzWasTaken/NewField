# Define a list of strings
strs = ["flower", "flow", "flight"]

# Define a function to find the longest common prefix among a list of strings
def longestCommonPrefix(strs):
    # Get the length of the first string in the list
    l = len(strs[0])
    
    # Iterate through the list of strings starting from the second string
    for i in range(1, len(strs)):
        # Calculate the minimum length between the length of the first string and the current string being iterated
        length = min(l, len(strs[i]))
        
        # Compare the substrings of the first string and the current string
        while length > 0 and strs[0][0:length] != strs[i][0:length]:
            # If the substrings don't match, decrease the length and continue comparing
            length = length - 1
            
            # If the length becomes 0, there is no common prefix, so return 0
            if length == 0:
                return 0
