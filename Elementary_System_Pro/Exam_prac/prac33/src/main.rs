struct Duck{
    sound:String
}
struct Chicken{
    sound:String
}
trait Diet{
    fn food(&self) -> String;
}
trait Habitat{
    fn Enviroment(&self) -> String;
}
impl Duck{
    fn new() -> Self{
        Duck{
            sound: "Quack".to_string()
        }
    }
}
impl Diet for Duck{
    fn food(&self) -> String{
        return "Plants and small fish".to_string();
    }
}
impl Diet for Chicken{
    fn food(&self) -> String{
        return "Seeds and insect".to_string();
    }
}
impl Habitat for Duck{
    fn Enviroment(&self) -> String{
        return "Wetlands and Ponds".to_string();
    }
}
impl Habitat for Chicken{
    fn Enviroment(&self) -> String{
        return "farms and backyards".to_string();
    }
}
impl Chicken{
    fn new() -> Self {
        Chicken{
            sound: "Roost".to_string()
        }
    }
}
fn describe_animal<T:Diet + Habitat>(animal : &T){
    println!("Habitat: {}, Diet: {}",animal.Enviroment(),animal.food());
}
fn main() {
    let fuzzy = Chicken::new();
    let meow = Duck::new();
    describe_animal(&fuzzy);
    describe_animal(&meow);
}
