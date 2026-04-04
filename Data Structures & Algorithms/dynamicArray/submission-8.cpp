#include <vector> 
class DynamicArray {
public:
    vector<int> da;

    int cap = 1;
    int pointer = 0;

    DynamicArray(int capacity) {
        cap = capacity;
    }

    int get(int i) {
        return da[i];
    }

    void set(int i, int n) {
        da[i] = n;
    }

    void pushback(int n) {
        if (pointer == cap){
            resize();

        }
        da.push_back(n);
        pointer++;
    }

    int popback() {
        pointer--;
        int r = da.back();
        da.pop_back();
        return r;
    }

    void resize() {
        cap = cap*2;
    }

    int getSize() {
        return pointer;
    }

    int getCapacity() {
        return cap;
    }
};
