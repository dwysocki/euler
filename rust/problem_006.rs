fn main() {
    let sum_sq = sum_of_squares(100);
    let sq_sum = square_of_sum(100);
    println!("{}-{} = {}", sq_sum, sum_sq, sq_sum-sum_sq);
}

fn sum_of_squares(n: int) -> int {
    if n > 1 {
        n*n + sum_of_squares(n-1)
    } else {
        1
    }
}

fn square_of_sum(n: int) -> int {
    let sum = (n * (n + 1)) / 2;

    sum*sum
}
