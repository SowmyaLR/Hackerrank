#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <assert.h>
void insertionSort(int ar_size, int *  ar) {
    int i,j,k,temp;
for( i = 0 ;i < ar_size ; i++ ) {
    /*storing current element whose left side is checked for its 
             correct position .*/

       temp = ar[ i ];    
       j = i;

       /* check whether the adjacent element in left side is greater or
            less than the current element. */

          while( temp < ar[ j -1] && j > 0 ) {

           // moving the left side element to one position forward .
                ar[ j ] = ar[ j-1];   
                j= j - 1;

           }
         // moving current element to its  correct position.
           ar[ j ] = temp; 
    if(i!=0){
    for(k=0;k<ar_size;k++)
        printf("%d ",ar[k]);
        printf("\n");}
     }  

}
int main(void) {
   
   int _ar_size;
scanf("%d", &_ar_size);
int _ar[_ar_size], _ar_i;
for(_ar_i = 0; _ar_i < _ar_size; _ar_i++) { 
   scanf("%d", &_ar[_ar_i]); 
}

insertionSort(_ar_size, _ar);
   
   return 0;
}
