from collections import Counter

def smallestWindow(s, t):
    if len(t) > len(s):
        return "-1"

    # Count characters in t
    t_count = Counter(t)
    window_count = Counter()

    required = len(t_count)  # Unique characters in t
    formed = 0  # Matched characters

    left = 0  # Left pointer
    min_len = float('inf')  # Minimum length
    min_start = 0  # Start index

    # Expand window with right pointer
    for right in range(len(s)):
        char = s[right]
        window_count[char] += 1
        
        # Match condition
        if char in t_count and window_count[char] == t_count[char]:
            formed += 1
        
        # Shrink window with left pointer
        while left <= right and formed == required:
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_start = left

            window_count[s[left]] -= 1
            if s[left] in t_count and window_count[s[left]] < t_count[s[left]]:
                formed -= 1
            left += 1
    
    # Return result or "-1"
    if min_len == float('inf'):
        return "-1"
    return s[min_start:min_start + min_len]

# Test the function
if __name__ == "__main__":
    s = "heytherethisisreallycoldnow"
    t = "toc"
    print(smallestWindow(s, t)) 