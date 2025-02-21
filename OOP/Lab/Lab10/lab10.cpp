#include <vector>
#include <iostream>
#include <string>
using namespace std;

struct Movie {
    string title;
    string date;
    vector<vector<bool>> availableSeats;
};
struct Reservation {
    string custumorName;
    string movieName;
    string date;
    int round;
    int seatNumber;
};
int main() {
    Movie movie1 = {"Captain America Brave New World", "2024-02-16",vector<vector<bool>>(4, vector<bool>(10, true))};
    Movie movie2 = {"Bridget Jones Mad About the Boy", "2024-02-17",vector<vector<bool>>(4, vector<bool>(10, true))};
    Movie movie3 = {"Flat Girls", "2024-02-18",vector<vector<bool>>(4, vector<bool>(10, true))};
    Movie movie4 = {"Heretic", "2024-02-19", vector<vector<bool>>(4,vector<bool>(10, true))};
    Movie movie5 = {"Dark Nuns", "2024-02-20",vector<vector<bool>>(4, vector<bool>(10, true))};
}