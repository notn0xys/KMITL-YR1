pub mod books;
pub mod media;
pub trait Library_Item{
    fn title(&self) -> &str;
    
    fn check_out(&mut self);

    
    fn check_in(&mut self);

    
    fn is_avaliable(&self) -> bool;

    
}