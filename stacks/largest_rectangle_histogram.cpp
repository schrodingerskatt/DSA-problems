// Problem Link : https://leetcode.com/problems/largest-rectangle-in-histogram/

class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        
    int maxArea = 0;
    stack<pair<int,int>>st;

    for(int i = 0; i < heights.size(); i++){
    int start = i;
    while(!st.empty()&&st.top().second > heights[i]){
    auto topmost = st.top();
    st.pop();
    int index = topmost.first;
    int ele = topmost.second;
    maxArea = max(maxArea, ele*(i-index));
    start = index;
    }
    st.push({start,heights[i]});
    }
    while(!st.empty()){
        int index = st.top().first;
        int ele = st.top().second;
        st.pop();
        maxArea = max(maxArea, ele*(static_cast<int>(heights.size()) - index));
    }
    return maxArea;
    }
};