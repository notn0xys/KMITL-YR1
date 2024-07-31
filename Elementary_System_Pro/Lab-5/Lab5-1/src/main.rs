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
    fn Encounter(&self, x: Encounter, y:Vec<Enemy>) {
        match x {
            
        }
    }
}


fn main() {
    
}
