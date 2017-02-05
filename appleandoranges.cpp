#include<iostream>
using namespace std;
int main(){
  int s,t,a,b,m,n;
  cin>>s>>t>>a>>b>>m>>n;
  int apples[m],oranges[n],apple_cover = 0, orange_cover = 0;
  int i,j;
  for(i=0;i<m;i++){
  cin>>apples[i];
  }
  for(i=0;i<n;i++){
  cin>>oranges[i];
  }

  for(i=0;i<m;i++){
     if((apples[i]+a)>=s&&(apples[i]+a)<=t){
        cout<<apples[i] + a<<" ";
        apple_cover++;
     }
  }

  for(i=0;i<n;i++){
    if((oranges[i]+b)>=s&&(oranges[i]+b)<=t){
        cout<<oranges[i]+b<<" ";
        orange_cover++;
     }
  }
  cout<<apple_cover<<endl;
  cout<<orange_cover<<endl;

}
