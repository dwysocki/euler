fn main() {
    let mut sum = 2u;
    let mut f1  = 1u;
    let mut f2  = 2u;
    let mut f   = f1 + f2;

    while {f < 4000000u} {
        if f % 2 == 0 {
            sum += f
        }
        f1 = f2;
        f2 = f;
        f  = f1 + f2;
    }

    println!("{}", sum);
}
