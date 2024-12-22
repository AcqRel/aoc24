use std::collections::HashMap;
use std::io::BufRead;

fn main() {
    let mut stdin = std::io::stdin().lock();
    let mut line = String::new();

    let mut total_for = HashMap::new();
    let mut score_for = HashMap::new();

    while stdin.read_line(&mut line).unwrap() != 0 {
        let mut n: u32 = line.trim().parse().unwrap();

        score_for.clear();
        let mut hist = [0; 4];
        for i in 0..2000 {
            let last = n % 10;
            n ^= 16777215 & (n << 6);
            n ^= 16777215 & (n >> 5);
            n ^= 16777215 & (n << 11);
            let new = n % 10;
            hist.rotate_left(1);
            hist[3] = new as i8 - last as i8;
            if i >= 3 {
                score_for.entry(hist).or_insert(new as u8);
            }
        }

        for (&chunk, &score) in &score_for {
            *total_for.entry(chunk).or_insert(0_u32) += score as u32;
        }

        line.clear();
    }
    println!("{}", total_for.values().max().unwrap());
}
