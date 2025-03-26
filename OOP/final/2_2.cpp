#include <iostream>
using namespace std;

class DynamicArray {
    public:
        int* arr;
        int size;
        DynamicArray(int size) {    
            arr = new int[size];
            for (int i = 0; i < size ; i++) {
                arr[i] = 0;
            }
        }
        int operator[](int index) {
            if (index >= size || index < 0) {
                return;
            }
            return arr[index];
        }
        ~DynamicArray() {
            delete[] arr;
        }
};