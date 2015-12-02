#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
void insertion(int n,int *ar)
    {
    int i,temp,j,count=0;
    for(i=0;i<n;i++)
        {
        temp = ar[i];
        j = i;
        while(temp<ar[j-1]&&j>0)
            {
            ar[j] = ar[j-1];
            j = j-1;
            count++;
        }
        ar[j] = temp;
    }
    printf("%d\n",count);
}

int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int i,n,array[1002];
    scanf("%d",&n);
    for(i=0;i<n;i++)
        scanf("%d",&array[i]);
    insertion(n,array);
    return 0;
}
