#include <iostream>
#include <array>
using namespace std;

class Instrument {
    public:
        virtual void play() = 0;
};

class Guitar: public Instrument {
    public:
        void play() {
            cout << "Strumming the guitar" << endl;
        }
};

class Piano: public Instrument {
    public:
        void play() {
            cout << "Playing the piano" << endl;
        }
};

int main() {
    Instrument* Guitarptr;
    Instrument* PianoPtr;
    Guitar guitar;
    Piano piano;
    Guitarptr = &guitar;
    PianoPtr = &piano;
    array<Instrument*,2> instruments = {Guitarptr,PianoPtr};
    for (auto instrument: instruments) {
        instrument->play();
    }
    return 0;
}