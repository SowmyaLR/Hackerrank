#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    string str;
    int test,count;
    cin>>test;
    while(test--)
        {
        count=0;
        cin>>str;
        int i;
        int len = str.size();
        for(i=0;i<len-1;i++)
            {
            if(str[i]==str[i+1])
                count++;
        }
        cout<<count<<endl;
    }
    return 0;
}
