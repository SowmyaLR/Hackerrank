#include<stdio.h>
int extract(int t,int r);
int main()
{
int num,rem,t,count,test;
    scanf("%d",&test);
 while(test!=0){
     scanf("%d",&num);
     t=num;
     count=0;
while(num!=0)
{
rem=num%10;
//printf("%d\n",rem);
count=count+extract(t,rem);
num=num/10;
}
printf("%d\n",count);
     test--;
 }
return 0;
}
int extract(int t,int r)
{
if(r!=0&&t%r==0)
	return 1;
return 0;
}
