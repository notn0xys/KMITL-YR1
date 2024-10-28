use inner::back::cutey;

mod inner;
mod outer;
struct Cutiepie{
    name:String
}
impl cutey for Cutiepie{}

fn main() {
    let me = Cutiepie{
        name:"Aki".to_string()
    };
    me.im_so_cute();
    outer::meow::hi_from_meow();
    inner::back::ulti::hi_from_out_calledfrom_util();
}

