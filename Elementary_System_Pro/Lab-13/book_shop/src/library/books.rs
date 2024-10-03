use crate::library::Library_Item;

pub struct Book{
    avaliable: bool,
    title:String
}
impl Library_Item for Book{
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
impl Book{
    pub fn new(x: &str) -> Self{
        Book{
            avaliable: true,
            title: x.to_string(),
        }
    }
}