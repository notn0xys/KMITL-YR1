use std::fmt;

#[derive(Debug)]
struct Data_Store<T>{
    data:Vec<T>
}
impl<T> Data_Store<T> {
    fn add_items(&mut self, x:T){
            self.data.push(x)
        
    }
    fn remove_items(&mut self, index:usize) -> Option<T>{
            if index <= self.data.len() - 1{
                let x = self.data.remove(index);
                println!("Removed");
                Some(x)
            }
            else{
                println!("Not found");
                None
            }
    }
    fn get_items(&self, index:usize)-> Option<&T>{
        if index <= self.data.len() - 1{
            let x = &self.data[index];
            Some(&x)
        }
        else{
            println!("Not found");
            None
        }
    }
    fn find_item<F>(&self, predicate:F) -> Option<&T>
    where
        F: Fn(&T) -> bool,
    {
            self.data.iter().find(|&item| predicate(item))
    }
    
    
    fn new() -> Self {
       Data_Store{data:vec![]}
    }
}
#[derive(Debug)]
enum Data_Type<T> {
    Number(T),
    Text(String),
    Boolean(bool)
}


fn main() {
    let mut int_store: Data_Store<Data_Type<i32>> = Data_Store::<Data_Type<i32>>::new();
    int_store.add_items(Data_Type::Number(42));
    let mut float_store: Data_Store<Data_Type<f64>> = Data_Store::<Data_Type<f64>>::new();
    float_store.add_items(Data_Type::Number(3.14));

    let mut String_Store = Data_Store::<String>::new();
    String_Store.add_items("Hello".to_string());

    println!("{:?}",int_store.get_items(0).unwrap());
    println!("{:?}",float_store.get_items(0).unwrap());
    println!("{:?}",String_Store.get_items(0).unwrap());

    let found = int_store.find_item(|item| match item{
        Data_Type::Number(n) => *n > 30,
        _ => false
    });
    println!("Found: {:?}" , found);
        
    
}
