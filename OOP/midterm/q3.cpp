#include <iostream>
#include <list>
#include <cstdlib>
using namespace std;

list<int> Recursive_merge(list<int>& list1, list<int>& list2, list<int> holder = {}) {
    if (list1.size() != 0 && list2.size() != 0) {
        if (list1.front() > list2.front()) {
            holder.push_back(list2.front());
            list2.pop_front();
            return Recursive_merge(list1,list2,holder);
        }
        else {
            holder.push_back(list1.front());
            list1.pop_front();
            return Recursive_merge(list1,list2,holder);
        }
    }
    else if (list1.size() == 0 && list2.size() != 0) {
        holder.push_back(list2.front());
        list2.pop_front();
        return Recursive_merge(list1,list2,holder);
    }
    else if (list2.size() == 0 && list1.size() != 0) {
        holder.push_back(list1.front());
        list1.pop_front();
        return Recursive_merge(list1,list2,holder);
    }
    else {
        return holder;
    }
}

int main() {
    srand(time(0));
    for (int i = 0; i < 10 ; i++) {
        int rando = rand() % 10;
        cout << rando << endl;
    }
    list<int> list1 = {1,2,7};
    list<int> list2 = {4,5,6};
    list<int> list3 = Recursive_merge(list1,list2);
    for (auto i: list3) {
        cout << i << " ";
    }
}