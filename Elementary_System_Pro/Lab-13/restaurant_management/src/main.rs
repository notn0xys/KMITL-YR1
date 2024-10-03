mod restaurant;
fn main() {
    println!("Restuarant Management System");
    restaurant::main();
    restaurant::call_do_sth();
    restaurant::back_of_house::main();
}
