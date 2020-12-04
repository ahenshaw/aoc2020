use std::io::prelude::*;
use std::{fs, io};
use parse_display::{Display, FromStr};

#[derive(Display, FromStr)]
#[display("{min}-{max} {letter}: {password}")]
struct Rule {
    min:      usize,
    max:      usize,
    letter:   char,
    password: String,
}

type Rules = Vec<Rule>;
fn main() {
    let f = fs::File::open("input/input.txt").unwrap();
    let reader = io::BufReader::new(f);
    let rules: Rules = reader.lines().map(|line| line.unwrap().parse::<Rule>().unwrap()).collect();

    part1(&rules);
    part2(&rules);
}

fn part1(rules: &Rules) {
    let mut num_valid: usize = 0;
    for rule in rules {
        let c = rule.password.matches(rule.letter).count();
        num_valid += (c >= rule.min && c <= rule.max) as usize;
    }
    println!("Part 1: {}", num_valid);
}

fn part2(rules: &Rules) {
    let mut num_valid: usize = 0;
    for rule in rules {
        let s = rule.password.as_bytes();
        let l = rule.letter as u8;
        num_valid += ((s[rule.min-1] == l) ^ (s[rule.max-1] == l)) as usize;
    }
    println!("Part 2: {}", num_valid);
}