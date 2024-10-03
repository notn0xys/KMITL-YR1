use crate::library::Library_Item;

pub struct AudioBook{
    avaliable: bool,
    title:String
}
impl Library_Item for AudioBook{
    fn title(&self) -> &str{
        &self.title
    }
    fn check_in(&mut self){
        self.avaliable = true;
    }
    fn check_out(&mut self){
        self.avaliable = false;
    }
    fn is_avaliable(&self) -> bool{
        self.avaliable
    }
}
impl AudioBook{
    pub fn new(x: &str) -> Self{
        AudioBook{
            avaliable: true,
            title: x.to_string(),
        }
    }
}