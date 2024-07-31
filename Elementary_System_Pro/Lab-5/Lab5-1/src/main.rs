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
        id:i32
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
    fn get_encounter(){

    }
}


fn main() {
    
}
