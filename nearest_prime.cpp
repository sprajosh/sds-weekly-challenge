#include <iostream>
#include <math.h>
using namespace std;

bool isprime(unsigned long long int num){
    bool prime = true;
    for (int i=2; i<int(sqrt(num))+1; ++i){
        if (num % i == 0){
            prime = false;
            break;
        }
    }
    return prime;
}

unsigned long long int larger(unsigned long long int num){
    bool found = false;
    if (num%2 == 0)
        num+=1;
    while (!found){
        if(isprime(num))
            return num;
        else
            num+=2;
    }

}

unsigned long long int smaller(unsigned long long int num){
    bool found = false;
    if (num%2 == 0)
        num-=1;
    while (!found && num > 0){
        if(isprime(num))
            return num;
        else
            num-=2;
    }
}

int main(){
    unsigned long long int num;
    cin>>num;
    cout<<larger(num+1)<<"\t"<<num<<"\t"<<smaller(num-1);
    return 0;
}