use std::io::BufRead;
use std::sync::atomic::AtomicU16;
use std::sync::atomic::Ordering;

use rayon::iter::{IntoParallelRefIterator, ParallelIterator};

fn main() {
    let mut stdin = std::io::stdin().lock();
    let mut line = String::new();

    let total_for: Vec<_> = (0..19_usize.pow(4)).map(|_| AtomicU16::new(0)).collect();

    let mut inputs = Vec::new();
    while stdin.read_line(&mut line).unwrap() != 0 {
        let n: u32 = line.trim().parse().unwrap();
        inputs.push(n);
        line.clear();
    }

    inputs.par_iter().for_each_init(
        || vec![0_u32; (19_usize.pow(4) + 31) / 32],
        |seen, &(mut n)| {
            for n in seen.iter_mut() {
                *n = 0;
            }

            let mut hash = 0;
            for i in 0..2000 {
                let last = n % 10;
                n ^= 16777215 & (n << 6);
                n ^= 16777215 & (n >> 5);
                n ^= 16777215 & (n << 11);

                let new = n % 10;
                let diff = (new + 9 - last) as usize;
                hash = (hash * 19 + diff) % 19_usize.pow(4);

                if i >= 3 && seen[hash >> 5] & (1 << (hash & 31)) == 0 {
                    seen[hash >> 5] |= 1 << (hash & 31);
                    total_for[hash].fetch_add(new as u16, Ordering::Relaxed);
                }
            }
        },
    );

    println!(
        "{}",
        total_for
            .iter()
            .map(|n| n.load(Ordering::Relaxed))
            .max()
            .unwrap()
    );
}
