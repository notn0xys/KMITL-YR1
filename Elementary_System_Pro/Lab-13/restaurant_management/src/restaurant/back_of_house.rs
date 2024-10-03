mod hosting;
pub fn do_sth2(){
    println!("From back");
}
pub fn call_do_sth(){
    hosting::do_sth();
}
pub fn main(){
    hosting::inner::let_me_cook(25);
}