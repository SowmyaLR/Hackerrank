#include<iostream>

using namespace std;


int main(){
    long int a[5],sum = 0,b[5],i,j;
    for(i=0;i<5;i++){
        cin>>a[i];
    }

    for(i=0;i<5;i++){
        sum=0;
        for(j=0;j<5;j++){
            if(j!=i){
                sum+=a[j];
            }
        }
        b[i] = sum;
    }
    for(i=0;i<5;i++){
        for(j=0;j<5;j++){
            if(b[i]<b[j]){
                b[i]^=b[j];
                b[j]^=b[i];
                b[i]^=b[j];
            }
        }
    }
    cout<<b[0]<<" "<<b[4];

    return 0;
}

