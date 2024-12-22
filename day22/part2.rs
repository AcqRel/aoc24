use std::io::BufRead;
use std::iter::zip;

fn main() {
    let mut stdin = std::io::stdin().lock();
    let mut line = String::new();

    let mut total_for = vec![0_u16; 19_usize.pow(4)];
    let mut seen = vec![0_u32; (19_usize.pow(4) + 31) / 32];

    let hash = |diffs: [i8; 4]| {
        (diffs[0] as usize + 9) * 19_usize.pow(3)
            + (diffs[1] as usize + 9) * 19_usize.pow(2)
            + (diffs[2] as usize + 9) * 19_usize.pow(1)
            + (diffs[3] as usize + 9) * 19_usize.pow(0)
    };

    while stdin.read_line(&mut line).unwrap() != 0 {
        let mut n: u32 = line.trim().parse().unwrap();

        let mut hist = [0; 4];
        for n in seen.iter_mut() {
            *n = 0;
        }

        for i in 0..2000 {
            let last = n % 10;
            n ^= 16777215 & (n << 6);
            n ^= 16777215 & (n >> 5);
            n ^= 16777215 & (n << 11);
            let new = n % 10;
            hist.rotate_left(1);
            hist[3] = new as i8 - last as i8;
            let hash = hash(hist);
            if i >= 3 && seen[hash >> 5] & (1 << (hash & 31)) == 0 {
                seen[hash >> 5] |= 1 << (hash & 31);
                total_for[hash] += new as u16;
            }
        }

        line.clear();
    }
    println!("{}", total_for.iter().max().unwrap());
}
