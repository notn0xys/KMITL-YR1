use crate::outer;
pub fn utils(){
    println!("Hi from utils");
}
pub fn hi_from_out_calledfrom_util(){
    outer::meow::hi_from_meow();
}