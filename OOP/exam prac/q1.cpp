#include <iostream>
#include <string>
#include <vector>
using namespace std;
class Instrument {
    private:
        string name;
        string type;
        string manufacturer;
        float price;
    public:
        Instrument(string inti_name, string init_type, string init_manu, float init_price): name(inti_name), type(init_type), manufacturer(manufacturer), price(init_price){}
        void display_instrument_details() {
            cout << "Name: " << name << endl;
            cout << "Type: " << type << endl;
            cout << "Manufacturer: " << manufacturer << endl;
            cout << "Price: " << price << endl;
        }
        void get_price_after_tax() {
            float after_tax = price * 1.07;
            cout << "Price: " << after_tax << endl;
        }
        const string get_name() {
            return name;
        }
        const string get_type() {
            return type;
        }
        const string get_manufacturer() {
            return manufacturer;
        }
        float get_price() {
            return price;
        }
        void set_name(string nenw_name) {
            name = nenw_name;
        }
        void set_type(string new_type) {
            type = new_type;
        }
        void set_manufacturer(string new_manufacturer) {
            manufacturer = new_manufacturer;
        } 
        void set_price(float new_price) {
            price = new_price;
        }



};

int main() {
    Instrument Guitar("Moew", "Stringy", "Your mom", 999.9);
    Instrument Piano("Pew","Key","Yamaha", 29392.3);
    vector<Instrument> instruments = {Guitar,Piano};
    for (Instrument i: instruments) {
        i.display_instrument_details();
        i.get_price_after_tax();
    }
}