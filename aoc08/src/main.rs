#![feature(str_split_once)]
use std::io::prelude::*;
use std::{fs, io};
use std::collections::HashSet;

type Operation = (String, i32);
type Program = Vec<Operation>;

fn main() {
    let fh = fs::File::open("input.txt").expect("Missing input");
    let reader = io::BufReader::new(fh);

    let mut program: Program = Vec::new();
    for line in reader.lines() {
        if let Some((opcode, s)) = line.unwrap().split_once(" ") {
            let offset = s.parse::<i32>().unwrap();
            program.push((opcode.to_string(), offset));
        }
    }
    let (acc, _ip, _flag) = run(&program);
    println!("Part 1: {}", acc);
    for (i, (opcode, offset)) in program.iter().enumerate() {
        let mut newp = program.clone();
        match opcode.as_ref() {
             "nop" => newp[i] = ("jmp".to_string(), *offset),
             "jmp" => newp[i] = ("nop".to_string(), *offset),
             _ => continue
        }
        let (acc, _ip, flag) = run(&newp);
        if flag {
            println!("Part 2: {}", acc);
        }
    }
}

fn run(program: &Program) -> (i32, i32, bool) {
    let mut acc: i32 = 0;
    let mut ip: i32 = 0;
    let mut seen:HashSet<i32> = HashSet::new();
    loop {
        if seen.contains(&ip) {return (acc, ip, false);}

        seen.insert(ip);
        if let Some((opcode, offset)) = program.get(ip as usize) {
            match opcode.as_ref() {
                "jmp" => ip += offset - 1,
                "acc" => acc += offset,
                _     => (),
            }
        } else {
            return (acc, ip, true);
        }
        ip += 1;
    }
}