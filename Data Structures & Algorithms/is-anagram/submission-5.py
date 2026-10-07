class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Gate clause to check for length at the start and remove extra work
        if len(s) != len(t):
            return False

        # Init a single array for counting all chars
        counts = [0] * 26

        # Iterate thru both strings; inc for occurence in s and dec for t.
        for a, b in zip(s,t):
            counts[ord(a) - ord('a')] += 1
            counts[ord(b) - ord('a')] -= 1

        # if counts is a list of all 0s (False) they are anagrams.
        return not any(counts)