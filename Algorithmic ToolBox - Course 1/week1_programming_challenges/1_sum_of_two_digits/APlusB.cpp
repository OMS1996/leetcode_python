#include <iostream>

int max_pairwise_product(vector<int>& numbers){

    prod = 0;

    for (int i = 0; i < ; ++i) {
        for (int j = 0; j < ; ++j) {
            temp = numbers[i]* numbers[j];
            if (temp >= prod){prod = temp}
        }
    }
    cout<<prod<<endl;
}

int main() {
    max_pairwise_product([1,2,3,4])
    return 0;
}