#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

int main()
{
    //Euler published the remarkable quadratic formula:
    //n² + n + 41
    //It turns out that the formula will produce 40 primes
    //for the consecutive values n = 0 to 39
    //However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41
    //is divisible by 41, and certainly when n = 41,
    //41² + 41 + 41 is clearly divisible by 41.
    //Using computers, the incredible formula  n²  79n + 1601
    //was discovered, which produces 80 primes for the
    //consecutive values n = 0 to 79.
    //The product of the coefficients, 79 and 1601, is 126479.
    //Considering quadratics of the form:
    //n² + an + b, where |a|  1000 and |b|  1000
    //
    //where |n| is the modulus/absolute value of n
    //e.g. |11| = 11 and |4| = 4
    //Find the product of the coefficients, a and b,
    //for the quadratic expression that produces
    //the maximum number of primes for consecutive
    //values of n, starting with n = 0.

    
    int a, b, n, current_length=0, greatest_length=0;
    
    cout << "enter a range from 1 to 10,000: ";
    cin >> a >> b;
    //cout << a << " " << b << endl;
    
    for (int i=a; i>=a && i<=b; ++i) {
        n = i;
        //cout << "n is " << n << ": ";
        current_length = 1;
        while (n != 1) {
              if (n % 2 == 0) {
                    n /= 2;
                    //cout << n << " ";
                    ++current_length;
              }
              else {
                   n = (3*n + 1);
                   //cout << n << " ";
                   ++current_length;
              }
        }
        //cout << endl;
        if (current_length > greatest_length) greatest_length = current_length;
    }
    cout << a << " " << b << " " << greatest_length << endl;
    
    
    system("pause");
} 	
