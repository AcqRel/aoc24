use std::io::BufRead;

fn vecmul(vec: u32, mat2: [u32; 24]) -> u32 {
    mat2.into_iter()
        .enumerate()
        .filter(|(i, _)| vec & (1 << i) != 0)
        .fold(0, |a, (_, b)| a ^ b)
}

fn matmul(mat1: [u32; 24], mat2: [u32; 24]) -> [u32; 24] {
    mat1.map(|r| vecmul(r, mat2))
}

fn matexp(mat: [u32; 24], n: usize) -> [u32; 24] {
    if n == 1 {
        return mat;
    }
    let half = matexp(mat, n / 2);
    let mut mat2 = matmul(half, half);
    if n % 2 == 1 {
        mat2 = matmul(mat2, mat);
    }
    mat2
}

fn shift_xor_mat(sh: i32) -> [u32; 24] {
    std::array::from_fn(|c| {
        (if (0..24).contains(&(c as i32 + sh)) {
            1 << (c as i32 + sh)
        } else {
            0
        }) | 1 << c
    })
}

fn main() {
    let it1 = matmul(shift_xor_mat(6), shift_xor_mat(-5));
    let it1 = matmul(it1, shift_xor_mat(11));
    let it2000 = matexp(it1, 2000);

    let mut stdin = std::io::stdin().lock();
    let mut line = String::new();
    let mut t = 0;
    while stdin.read_line(&mut line).unwrap() != 0 {
        let n: u32 = line.trim().parse().unwrap();
        t += vecmul(n, it2000) as u64;
        line.clear();
    }
    println!("{t}");
}
