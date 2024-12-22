use std::collections::HashMap;
use std::io::BufRead;

fn main() {
    let mut stdin = std::io::stdin().lock();
    let mut line = String::new();

    let mut total_for = HashMap::new();
    let mut score_for = HashMap::new();
    let mut values = Vec::new();
    let mut diffs = Vec::new();

    while stdin.read_line(&mut line).unwrap() != 0 {
        let mut n: u32 = line.trim().parse().unwrap();

        values.clear();
        diffs.clear();
        for _ in 0..2000 {
            let last = n % 10;
            n ^= 16777215 & (n << 6);
            n ^= 16777215 & (n >> 5);
            n ^= 16777215 & (n << 11);
            let new = n % 10;
            values.push(new as u8);
            diffs.push(new as i8 - last as i8);
        }

        score_for.clear();
        for (chunk, &digit) in diffs.windows(4).zip(&values[3..]) {
            let chunk: [i8; 4] = chunk.try_into().unwrap();
            score_for.entry(chunk).or_insert(digit);
        }

        for (&chunk, &score) in &score_for {
            *total_for.entry(chunk).or_insert(0_u32) += score as u32;
        }

        line.clear();
    }
    println!("{}", total_for.values().max().unwrap());
}
