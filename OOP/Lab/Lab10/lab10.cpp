#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>

using namespace std;

struct Movie {
    string title;
    string date;
    vector<vector<vector<bool>>> availableSeats; 

    Movie(string t, string d) : title(t), date(d), availableSeats(4, vector<vector<bool>>(4, vector<bool>(10, true))) {}
};

void displaySchedule(const vector<Movie> &movies) {
    for (const auto &movie : movies) {
        cout << movie.title << " (" << movie.date << ")" << endl;
        for (int i = 0; i < 4; i++) {
            int available = 0;
            for (const auto &row : movie.availableSeats[i]) {
                for (bool seat : row) {
                    if (seat) {
                        available++;
                    }
                }
            }
            cout << "- Round " << i + 1 << ": " << available << " seats left" << endl;
        }
    }
}

void displaySeats(const Movie &movie, int round) {
    cout << "Seating chart for " << movie.title << " on " << movie.date << " (Round " << round << "):\n";
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 10; j++) {
            if (movie.availableSeats[round - 1][i][j] ? "O " : "X ") {
                cout << "O ";
            }
            else {
                cout << "X ";
            }
        }
        cout << endl;
    }
}

void saveData(const vector<Movie> &movies) {
    ofstream file("reservations.csv");
    file << "Movie Title,Date,Round,Seat Number,Availability\n";
    for (const auto &movie : movies) {
        for (int i = 0; i < 4; i++) { 
            for (int row = 0; row < 4; row++) { 
                for (int col = 0; col < 10; col++) {
                    int seatNumber = row * 10 + col + 1;
                    file << movie.title << "," << movie.date << "," << i + 1 << "," << seatNumber << "," << movie.availableSeats[i][row][col] << endl;
                }
            }
        }
    }
    file.close();
}


void loadData(vector<Movie> &movies) {
    ifstream file("reservations.csv");
    if (!file) return;
    string line, title, date;
    int round, seatNumber, available;
    getline(file, line);
    while (getline(file, line)) {
        stringstream ss(line);
        getline(ss, title, ',');
        getline(ss, date, ',');
        ss >> round; ss.ignore();
        ss >> seatNumber; ss.ignore();
        ss >> available;
        
        for (auto &movie : movies) {
            if (movie.title == title && movie.date == date) {
                int row = (seatNumber - 1) / 10, col = (seatNumber - 1) % 10;
                movie.availableSeats[round - 1][row][col] = available;
            }
        }
    }
    file.close();
}

void makeReservation(vector<Movie> &movies) {
    displaySchedule(movies);
    string title, date, name;
    int round, seat;
    
    cout << "Enter your name: "; 
    cin >> name;
    cout << "Enter movie title: "; 
    cin.ignore(); 
    getline(cin, title);
    cout << "Enter date (YYYY-MM-DD): "; 
    cin >> date;
    cout << "Enter round (1-4): "; 
    cin >> round;
    
    for (auto &movie : movies) {
        if (movie.title == title && movie.date == date && round > 0 && round < 5) {
            displaySeats(movie, round);
            cout << "Enter seat number (1-40): "; cin >> seat;
            int row = (seat - 1) / 10, col = (seat - 1) % 10;
            
            if (movie.availableSeats[round - 1][row][col]) {
                movie.availableSeats[round - 1][row][col] = false;
                cout << "Reservation successful!" << endl;
                saveData(movies);
                return;
            } else {
                cout << "Seat is already booked!" <<endl;
                return;
            }
        }
    }
    cout << "Error: Movie title or date not found! or Round not avaliable\n";
}

void cancelReservation(vector<Movie> &movies) {
    string title, date, name;
    int round, seat;
    cout << "Enter your name: "; 
    cin >> name;
    cout << "Enter movie title: "; 
    cin.ignore(); 
    getline(cin, title);
    cout << "Enter date (YYYY-MM-DD): "; 
    cin >> date;
    cout << "Enter round (1-4): "; 
    cin >> round;
    cout << "Enter seat number (1-40): "; 
    cin >> seat;
    
    for (auto &movie : movies) {
        if (movie.title == title && movie.date == date) {
            int row = (seat - 1) / 10, col = (seat - 1) % 10;
            if (!movie.availableSeats[round - 1][row][col]) {
                movie.availableSeats[round - 1][row][col] = true;
                cout << "Reservation canceled!\n";
                saveData(movies);
                return;
            } else {
                cout << "No reservation found!\n";
                return;
            }
        }
    }
    cout << "Error: Movie title or date not found!\n";
}

int main() {
    vector<Movie> movies = {
        {"Captain America Brave New World", "2024-02-16"},
        {"Bridget Jones Mad About the Boy", "2024-02-17"},
        {"Flat Girls", "2024-02-18"},
        {"Heretic", "2024-02-19"},
        {"Dark Nuns", "2024-02-20"}
    };
    
    loadData(movies);
    
    while (true) {
        cout << "\n1. View Schedule\n2. Make Reservation\n3. Cancel Reservation\n4. Exit\nChoice: ";
        int choice;
        cin >> choice;
        switch (choice) {
            case 1: 
                displaySchedule(movies) ;
                break;
            
            case 2:
                makeReservation(movies); 
                break;
            case 3: 
                cancelReservation(movies); 
                break;
            case 4: 
                saveData(movies); 
                return 0;
            default: 
            cout << "Invalid choice!"<< endl;
        }
    }
}
