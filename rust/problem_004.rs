use std::iter::order::equals;

fn main() {
    let mut pal = 0i;

    for x in range(100i, 1000i).rev() {
        for y in range(x, 1000i).rev() {
            let n = x*y;
            if palindrome(n) && n>pal {
                pal = n;
            }
        }
    }

    println!("{}", pal);
}

fn palindrome(x: int) -> bool {
    let s: String = x.to_string();
    let b  = s.as_bytes();
    let iter = b.iter();
    let n: uint = iter.len() << 1;

    equals(iter.take(n), iter.rev().take(n))
}
