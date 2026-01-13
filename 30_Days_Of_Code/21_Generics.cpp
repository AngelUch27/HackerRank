// https://www.hackerrank.com/challenges/30-generics/problem?isFullScreen=true
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

template <typename T>
void printArray(const vector<T>& arr) {
    for (const auto& item : arr) {
        cout << item << endl;
    }
}

int main() {
    int n; 
    if (!(cin >> n)) return 0;
    vector<int> vi(n);
    for (int i = 0; i < n; ++i) cin >> vi[i];

    int m; 
    if (!(cin >> m)) return 0;
    vector<string> vs(m);
    for (int i = 0; i < m; ++i) cin >> vs[i]; // "Jenny's" se lee bien con >>

    printArray(vi);
    printArray(vs);
    return 0;
}
