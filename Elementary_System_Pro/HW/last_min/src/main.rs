fn matrix_mult(a:Vec<Vec<i32>>, b: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
    let mut final_vec:Vec<Vec<i32>> = Vec::new();
    for i in 0..a.len(){
        let mut temp_vec:Vec<i32> = Vec::new();
        for j in 0..b[0].len(){
            let mut result = 0;
            for k in 0..a[0].len(){
                result += (a[i][k] * b[k][j]);
            }
            temp_vec.push(result);
        }
        final_vec.push(temp_vec);
    }
    final_vec
}
fn main() {
    let a:Vec<Vec<i32>> = vec![
        vec![1,3,4],
        vec![2,5,6],
        vec![6,5,4]
    ];
    let b:Vec<Vec<i32>> = vec![
        vec![2,3,4],
        vec![4,6,6],
        vec![6,2,4]
    ];
    let result = matrix_mult(a,b);
    for i in result {
        println!("{:?}", i);
    }
}