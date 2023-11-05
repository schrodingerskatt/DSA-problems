# problem link : https://leetcode.com/problems/number-of-valid-clock-times/

class Solution:
    def countTime(self, time: str) -> int:
        hh_1 = '?' if time[0] == '?' else int(time[0])
        hh_2 = '?' if time[1] == '?' else int(time[1])
        mm_1 = '?' if time[3] == '?' else int(time[3])
        mm_2 = '?' if time[4] == '?' else int(time[4])
        count_h = 0
        count_m = 0
        
        if hh_1 == '?' and hh_2 == '?':
            count_h = 24
        elif hh_1 != '?' and hh_2 =='?':
            if hh_1 == 2:
                count_h = 4
            else:
                count_h = 10
        elif hh_1 == '?' and hh_2 !='?':
            if hh_2 <= 3:
                count_h = 3
            else:
                count_h = 2
        
        if mm_1 == '?' and mm_2 =='?':
            count_m = 60
        elif mm_1 == '?' and mm_2 != '?':
            count_m = 6
        elif mm_1 != '?' and mm_2 =='?':
            count_m = 10
        if count_h == 0 and count_m == 0:
            return 1
        elif count_m == 0:
            return count_h
        elif count_h == 0:
            return count_m
        else:
            return count_m*count_h
        
