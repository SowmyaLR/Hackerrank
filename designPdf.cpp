#include<iostream>
#include<vector>

using namespace std;
int computeHash(char c){
    return c - 'a';
}

int main(){
    vector<int> h(26);
    int i,len,area = 1,j;
    for(int h_i = 0; h_i < 26; h_i++){
       cin >> h[h_i];
    }
    string word;
    cin >> word;
    len = word.size();
    for(i=0;i<len;i++){
        j = computeHash(word[i]);
        if(h[j]>area){
            area = h[j];
        }

    }
    cout<<area*len;
    return 0;
}
