import math


class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        a_len = len(a)
        b_len = len(b)

        # compute min no. of string length needed to start comparing with 'b'
        no_of_repeats_req = math.ceil(b_len / a_len)

        # new string to compare from
        new_a_str = ""

        # build the new string
        for i in range(0, no_of_repeats_req):
            new_a_str += a

        new_a_str_len = len(new_a_str)

        # compare all the substrings of string 'b' length in the new string
        for i in range(0, new_a_str_len - b_len + 1):
            sub_str = new_a_str[i: i + b_len]
            if b == sub_str:
                return no_of_repeats_req
        
        # add one more copy of string 'a' to new string 
        new_a_str += a
        new_a_str_len = len(new_a_str)
        no_of_repeats_req += 1

        # again do the similar test
        for i in range(0, new_a_str_len - b_len + 1):
            sub_str = new_a_str[i: i + b_len]
            if b == sub_str:
                return no_of_repeats_req
        
        # by this time we checked all possible subtrings combinations, hence no solution exists
        return -1



