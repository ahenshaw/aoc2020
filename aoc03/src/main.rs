use std::io::prelude::*;
use std::{fs, io};

fn main() {
    let f = fs::File::open("input/input.txt").unwrap();
    let reader = io::BufReader::new(f);
    let terrain: Vec<String> = reader.lines().map(|line| line.unwrap()).collect();
    println!("Part 1: {}", trees(&terrain, 3, 1));

    let slopes = [(1usize, 1usize), (3, 1), (5, 1), (7, 1), (1, 2)];
    let result:usize = slopes.iter().map(|&(right, down)| trees(&terrain, right, down)).product();
    println!("Part 2: {}", result);
}

fn trees(terrain: &Vec<String>, right: usize, down: usize) -> usize {
    let mut row: usize = 0;
    let mut col: usize = 0;
    let mut count: usize = 0;

    while row < terrain.len() {
        let line = terrain[row].as_bytes();
        count += (line[col % line.len()] == b'#') as usize;
        row += down;
        col += right;
    }
    count
}
