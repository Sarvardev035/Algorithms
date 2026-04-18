class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_from_centers(l, r):

            while l >=0 and r<len(s) and s[l] == s[r]:
                l = l - 1
                r = r + 1
            
            # because the loop is ended so 'l' is outbound and 'r' here is exclusive so it does not matter.
            # here we have captured the palindromic substring

            #returns the string but is costly, later i have to check the string lenght.
            # return s[l+1: r]

            # better way is to return the indexes
            return l+1,r


        longest_l = 0 
        longest_r = 0 
        for i, c in enumerate(s):

            # for odd pal
            l_o, r_o = expand_from_centers(i, i)

            # for even pal
            # systematic assumption: the center consist of two characters
            l_e, r_e = expand_from_centers(i, i+1)

            # check if odd one is longest or even one
            if r_o - l_o > longest_r - longest_l:
                longest_l = l_o
                longest_r = r_o

            if r_e - l_e > longest_r - longest_l:
                longest_l = l_e
                longest_r = r_e
        
        return s[longest_l : longest_r]