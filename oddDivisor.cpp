#include <bits/stdc++.h>
using namespace std;

bool checkOddFactors(long long int num){
    while(num>1){
        if(num%2!=0){
            return true;
        }
        num/=2;
    }
    return false;
}

int main(){
    int n;
    cin>>n;
    for (int i=0;i<n;i++){
        long long int num;
        cin>>num;
        if(checkOddFactors(num)){
            cout<<"Yes"<<endl;
        }
        else{
            cout<<"No"<<endl;
        }
    }
    return 0;
}