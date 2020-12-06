use std::io::prelude::*;
use std::{fs, io};
use std::i32;
use std::collections::HashSet;
fn main() {
    let fh = fs::File::open("input/input.txt").unwrap();
    let reader = io::BufReader::new(fh);

    let seats: Vec<i32> = reader
                .lines()
                .map(|line| i32::from_str_radix(&(line.unwrap()
                    .replace("F", "0")
                    .replace("B", "1")
                    .replace("L", "0")
                    .replace("R", "1")), 2).unwrap()
                )
                .collect();
    let min = seats.iter().min().unwrap();
    let max = seats.iter().max().unwrap();
    println!("Part 1: {}", max);
    let possible: HashSet<i32> = (*min..=*max).collect();
    let occupied: HashSet<i32> = seats.into_iter().collect();
    let unoccupied = possible.difference(&occupied);
    println!("Part 2: {:?}", unoccupied);
}
