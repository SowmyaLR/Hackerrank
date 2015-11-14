#include <iostream> 
#include <cstring> 
using namespace std; 
 
int main() 
{ 
  char str[10000],r[10000]; 
  char *start, *end; 
  int len; 
  char t;
	bool flag;
    int test,i,j,d1,d2; 
  cin>>test;

while(test--)
        {
        flag = true;
        cin>>str;
       len = strlen(str); 
strcpy(r,str);
  start = str; 
  end = &str[len-1]; 
 
  while(start < end) { 
    // swap chars 
    t = *start; 
    *start = *end; 
    *end = t; 
 
    // advance pointers 
    start++; 
    end--; 
  } 
 
 
  //cout << "Reversed: " << str << "\n"<<r<<"\n"; 
        for(i=1;i<=len-1;i++)
            {
		//cout<<str[i]-str[i-1]<<" "<<r[i]-r[i-1]<<"\n";
	d1 = str[i]-str[i-1];
	d2 = r[i]-r[i-1];
	d1 = d1>0?d1:-d1;
	d2 = d2>0?d2:-d2;
	
            if(d1!=d2)
                {
		//cout<<str[i]-str[i-1]<<" "<<r[i]-r[i-1]<<"\n";
                flag = false;
                break;
            }
	
        }
        if(flag)
            cout<<"Funny\n";
        else
            cout<<"Not Funny\n";
    }


  //cout << "Original: " << str << "\n"; 
   
  
  return 0; 
}
