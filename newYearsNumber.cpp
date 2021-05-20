//Program to find if the number is constructed by using the 2020 and 2021
#include <bits/stdc++.h>
using namespace std;

bool checkRequire(int num){
    //set the 2 years 2020 and the 2021
    int a=2020;
    int b=2021;

    //set a coumt which will take care of the num
    int count;

    //for loop for the 2020 which subtract the 2020 from the number and set it in the count
    for (int i=0;i*a<=num;i++){
        count=num-i*a;

        // each time check if the 2021 is divisible or not if then return true
        if(count%b==0){
            return true;
        }
    }
    // if count is 0 means all thet number completed in the number
    return (count==0)?true:false;
    
}

int main(){
    int n;
    cin>>n;
    for (int i=0;i<n;i++){
        int num;
        cin>>num;
        if(checkRequire(num)){
            cout<<"YES"<<endl;
        }
        else{
            cout<<"NO"<<endl;
        }
        

    }
    return 0;
}