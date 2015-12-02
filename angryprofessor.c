#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    int test,n,k,a[1000],i,flag;
    scanf("%d",&test);
    while(test!=0){
        scanf("%d%d",&n,&k);
        flag=0;
    for(i=0;i<n;i++)
        scanf("%d",&a[i]);
    for(i=0;i<n;i++)
        {
        if(a[i]<=0){
            flag++;
        }
        if(flag==k)
            break;
           
    }
        if(flag==k)
            printf("NO\n");
        else
            printf("YES\n");
        test--;
    }
    return 0;
}
