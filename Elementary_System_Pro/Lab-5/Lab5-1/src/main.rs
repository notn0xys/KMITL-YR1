use std::io;
use rand::Rng;

#[derive(Debug)]
struct Player{
        hp:i32,
        stamina: i32,
        power:i32,
        gold:i32,
        hp_max:i32
    }
#[derive(Debug,Clone)]
struct Enemy{
        hp:i32,
        stamina: i32,
        power:i32,
    }
enum Move {
        North,
        East,
        South,
        West
    }
enum Encounter{
        Nothing,
        Bush,
        Meat,
        Water,
        Herb,
        IronOre,
        Enemy
    }
impl Move {
    fn direction(&self){
        match self {
            Move::East => println!("You've moved east"),
            Move::North => println!("You've moved North"),
            Move::South => println!("You've moved south"),
            Move::West => println!("You've moved west")
        }
    }
} 

impl Player {
    fn get_encounter() -> Encounter{
        let n = rand::thread_rng().gen_range(1..100);
        match n {
            1..=17 => Encounter::Nothing,
            18..=25 => Encounter::Bush,
            26..=40 => Encounter::Meat,
            41..=55 => Encounter::Water,
            56..=70 => Encounter::Herb,
            71..=75 => Encounter::IronOre,
            _ => Encounter::Enemy
        }

    }
    fn Encounter(&mut self, x: Encounter, y:Vec<Enemy>) {
        match x {
            Encounter::Bush => {
                println!("You've found bush! Stamina -1");
                self.stamina -= 2;

            }
            Encounter::Herb =>{
                println!("You've found Herb! Power + 1");
                self.power += 1;
                self.stamina -= 1;
            }
            Encounter::IronOre => {
                println!("You found Iron Ore! Power + 10");
                self.power += 10;
                self.stamina -= 1;
            }
            Encounter::Nothing =>{
                println!("Found Nothing");
                self.stamina -= 1;
            }
            Encounter::Meat =>{
                println!("Found Meat");
                self.stamina -= 1;
                if self.hp >= self.hp_max  {
                    println!("Max Hp reached");
                    self.hp = self.hp_max;
                }
                else {
                    println!("HP not max added 4 hp");
                    self.hp += 4;
                }
            }
            Encounter::Water => {
                println!("Found water");
                self.stamina += 1;
            }
            Encounter::Enemy => {
                let n = rand::thread_rng().gen_range(1..100);
                match n {
                    
                }
            }
        }
    }
}


fn main() {
    
}
