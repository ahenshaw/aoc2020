#![feature(str_split_once)]
use std::io::prelude::*;
use std::{fs, io};
use regex::Regex;
use std::collections::HashMap;

static FILE_PATH: &'static str = "input.txt";
// static FILE_PATH: &'static str = "test.txt";
#[derive(Debug)]
enum Code {
    Mask(String),
    Mem{addr:u64, value:u64},
}
type Program = Vec<Code>;
type Memory = HashMap<u64, u64>;

fn main() {
    let f = fs::File::open(FILE_PATH).unwrap();
    let reader = io::BufReader::new(f);
    let re = Regex::new(r"(?:(mem)\[(\d+)\] = (\d+))|(?:mask = (\S+))").unwrap();
    let program: Program = reader
        .lines()
        .map(|line| {
            let line = line.unwrap();
            let cap = re.captures(&line).unwrap();
            // println!("{:?}", cap);
            match cap.get(1) {
                Some(_) => {
                    let addr:u64  = cap[2].parse().unwrap();
                    let value:u64 = cap[3].parse().unwrap();
                    Code::Mem{addr:addr, value:value}
                },
                _ => Code::Mask(cap[4].to_owned()),
            }                       
        })
        .collect();
    
    part1(&program);
    // part2(&program);
 }

fn part1(program: &Program) {
    let mut memory: Memory = HashMap::new();
    let mut mask = 0u64;
    let mut bits = 0u64;
    for code in program {
        match code {
            Code::Mask(s) => {
                mask = 0;
                bits = 0;
                for c in s.chars() {
                    mask <<= 1;
                    bits <<= 1;
                    if c == 'X' {
                        mask |= 1;
                    } else {
                        if c == '1' {
                            bits |= 1;
                        }
                    }
                }
            },
            Code::Mem{addr, value} => {
                memory.insert(*addr, *value & mask | bits);
            },
        }
    }
    println!("Part 1: {}", memory.values().sum::<u64>());
 }

