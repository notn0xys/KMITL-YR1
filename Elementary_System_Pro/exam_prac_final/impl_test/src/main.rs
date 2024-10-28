trait Land{
    fn drive(&self){
        println!("Driving")
    }
}
trait Water{
    fn sail(&self){
        println!("Sailing");
    }
}
trait Amphibious{
    fn moveee(&self){
        println!("Moving both land and water");
    }
}
impl <T: Water + Land> Amphibious for T {}
impl Water for HoverCraft{}
impl Land for HoverCraft {}

struct SUV {
    name:String
}
struct Boat{
    name:String
}
struct HoverCraft{
    name:String
}
fn moew_test1(x: &dyn Amphibious){
    x.moveee();
}           
fn land_water<T: Land + Water>(x: &T){
    x.sail();
    x.drive();
}
fn main() {
    let test1 = HoverCraft{
        name:"Moew".to_string()
    };
    moew_test1(&test1);
    land_water(&test1);
}           
