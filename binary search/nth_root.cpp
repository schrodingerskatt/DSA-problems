// Question Link : https://www.codingninjas.com/studio/problems/nth-root-of-m_1062679

int root(int mid, int n, int m){

long long ans = 1;
for(int i = 1; i <=n; i++){
ans = ans*mid;
if(ans > m) return 2;
}
if(ans == m) return 1;
return 0;

}

int NthRoot(int n, int m) {
  
  int low = 1, high = m;

  while(low <= high){
  int mid = low + (high - low)/2;
  int nth_root = root(mid,n,m);
  if (nth_root == 1) {
    return mid;
  } else if (nth_root == 0)
    low = mid + 1;
  else high = mid - 1;
  }
  return -1;
}