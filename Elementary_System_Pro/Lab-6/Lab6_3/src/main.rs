
trait SimpleAnalyzable {
    fn mean(&self) -> f64;
    fn median(&self) -> f64;
}

struct SimpleDataSet{
    data: Vec<f64>
}

impl SimpleAnalyzable for Vec<f64> {
    fn mean(&self) -> f64 {
        
    }
    fn median(&self) -> f64 {
        
    }
}

fn main() {
    println!("Hello, world!");
}
