#include <iostream>
using namespace std;

int mini(int a,int b){
    int min_num=(a<b) ? a : b;
    return min_num;
}

int main(){
    int x, y;
    cin >> x >> y;
    cout << mini(x,y) << endl;
}