#include <iostream>
using namespace std;

int main(){
    int t, n, m;
    cin >> t;
    for(int k = 0; k < t; k++){
        cin >> n >> m;
        int number = 0;
        int sub = m - n;
        for(int i = m; i >= sub; i--){
            number += i;
        }
        number = number - m;
        cout << number << endl;
    }

    return 0;
}

/* 12918 - Lucky Thief
https://onlinejudge.org/external/129/12918.pdf */