
fn multiply_matrix(x:[[i32;3];2],y:[[i32;3];3]) -> [[i32;3];2]{
    let mut final_matrix:[[i32;3];2] = [[0,0,0],[0,0,0]];
    for i in 0..x.len(){
        let mut new_arr = [0,0,0];
        for j in 0..y[0].len(){
            let mut result = 0;
            for k in 0..y.len(){
                let var = x[i][k] * y[k][j];
                result += var;
            }
            new_arr[j] = result;
        }
        final_matrix[i] = new_arr;
    }

    final_matrix
}


fn main() {
    let matrix1= [[1,2,3],[4,5,6]];
    let matrix2 = [[7,8,9],[10,11,12],[13,14,15]];
    let total_matrix = multiply_matrix(matrix1, matrix2);
    for i in &total_matrix{
        println!("{:?}", i);
    }

}
