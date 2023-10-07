// Problem and Solution Link : https://github.com/MAZHARMIK/Interview_DS_Algo/blob/master/Arrays/Intervals_Based_Qn/Meeting%20Rooms.cpp

class Solution {
public:
     static bool myFunction(Interval& i1, Interval& i2) {
        return i1.start < i2.start;
        
     }
    bool canAttendMeetings(vector<Interval> &intervals) {
        if(intervals.size() == 0)
            return true;
        sort(intervals.begin(), intervals.end(), myFunction);
        
        Interval prevInterval = intervals[0];
        for(int i = 1; i<intervals.size(); i++) {
            int currInterval_start = intervals[i].start;
            if(currInterval_start < prevInterval.end) {
                return false;
            } else {
                prevInterval = intervals[i];
            }
        }
        return true;
    }
};