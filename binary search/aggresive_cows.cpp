// Questions : https://www.codingninjas.com/studio/problems/aggressive-cows_1082559?utm_source=youtube&utm_medium=affiliate&utm_campaign=codestudio_Striver_BinarySeries&leftPanelTab=0

int aggressiveCows(vector<int> &stalls, int k)
{
   sort(stalls.begin(), stalls.end());
   int n = stalls.size();

   int low = 1;
   int high = stalls[n-1] - stalls[0];

   while(low <= high){
   
   int mid = low + (high - low)/2;
   int start = stalls[0];
   int cnt = 1;
   for(int i = 1; i < n; i++){
    if(stalls[i] - start >= mid){
        cnt++;
        start = stalls[i];
    }
   }
   if(cnt >= k) low = mid + 1;
   else high = mid - 1;
   }
   return high;
}