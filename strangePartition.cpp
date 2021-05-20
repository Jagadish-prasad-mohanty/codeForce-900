#include <bits/stdc++.h>
using namespace std;

pair<int,int> getMaxMin(long long int arr[],long long int n, long long int x){
    long long int maxm=0,minm=0;

    for(long long int i=0;i<n;i++){
        minm+=arr[i];
        maxm+=arr[i]/x;
        if(arr[i]%x) maxm++;
    }
    long long int bu=minm;
    minm/=x;
    if(bu%x) minm++;
    return make_pair(minm,maxm);
}

int main(){
    int t;
    cin>>t;
    while(t--){
        long long int n,x;
        cin>>n>>x;
        long long int arr[n];
        for (long long int i=0;i<n;i++){
            cin>>arr[i];
        }
        pair<int,int> res=getMaxMin(arr,n,x);
        cout<<res.first<<" "<<res.second<<endl;
    }
    return 0;
}