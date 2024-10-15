struct Duck{
    noise:String,
}
struct Chicken{
    noise:String,
}
trait Diet{
    fn food(&self) -> String;
}
trait Habitat{
    fn enviroment(&self) -> String;
}
impl Chicken{
    fn new() -> Self{
        Chicken{
            noise: "Woof".to_string()
        }
    }
}
impl Duck{
    fn new() -> Self{
        Duck{
            noise: "Quack".to_string()
        }
    }
}
impl Diet for Duck {
    fn food(&self) -> String {
        return "Plants and small fish".to_string();
    }
}
impl Diet for Chicken {
    fn food(&self) -> String {
        return "seed and insects".to_string();
    }
}
impl Habitat for Duck {
    fn enviroment(&self) -> String {
        return "Wetlands and pond".to_string();
    }
}
impl Habitat for Chicken {
    fn enviroment(&self) -> String {
        return "farm and backyards".to_string();
    }
}
fn descripbe_animal<T: Diet + Habitat>(animal:&T){
    println!("{} , {} ",animal.food(),animal.enviroment());
}
fn main() {
    let ruff = Chicken::new();
    let qucky = Duck::new();
    descripbe_animal(&ruff);
    descripbe_animal(&qucky);
}
