#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int i,j,k,n;
    scanf("%d",&n);
    for(i=0;i<n;i++)
        {
        for(j=i;j<n-1;j++)
            printf(" ");
        for(k=0;k<=i;k++)
            printf("#");
        printf("\n");
    }

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
    return 0;
}
