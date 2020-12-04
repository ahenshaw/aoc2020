use std::io::prelude::*;
use std::{fs, io};
use std::collections::{HashSet, HashMap};
use itertools::Itertools;
use std::time::Instant;

type Passport<'a> = HashMap<&'a str, &'a str>;

fn main(){
    let mut contents = String::new();
    let fh = fs::File::open("input/input.txt").unwrap();
    let mut reader = io::BufReader::new(fh);

    reader.read_to_string(&mut contents).unwrap();

    let data = contents.split("\r\n\r\n");
    let mut passports = Vec::<Passport>::new();
    let start = Instant::now();
    for raw_passport in data {
        let passport: Passport = raw_passport.split_whitespace()
            .flat_map(|p| p.split(':'))
            .tuples()
            .collect();
        if required_fields_present(&passport) {
            passports.push(passport);
        }
    }
    let duration = start.elapsed();
    println!("Elapsed: {:?}", duration);
    println!("Part 1: {}", passports.len());

    let result = passports.iter().filter(|x| is_valid(x)).count();
    println!("Part 2: {}", result);
}



fn required_fields_present(passport: &Passport) -> bool {
    let required:HashSet<&str> = "byr iyr eyr hgt hcl ecl pid".split(" ").collect();
    let keys:HashSet<&str> = passport.keys().cloned().collect();
    required.is_subset(&keys)
}

fn is_valid(passport: &Passport) -> bool {
    passport.iter().all(|(&k, v)| match k {
        "byr" => (1920..=2002).contains(&v.parse().unwrap_or(0)),
        "iyr" => (2010..=2020).contains(&v.parse().unwrap_or(0)),
        "eyr" => (2020..=2030).contains(&v.parse().unwrap_or(0)),
        "hcl" => v.starts_with('#') && v.len() == 7 && v.chars().skip(1).all(|c| c.is_ascii_hexdigit()),
        "ecl" => ["amb","blu","brn","gry","grn","hzl","oth"].contains(v),
        "pid" => v.len() == 9 && v.chars().all(|c| c.is_ascii_digit()),
        "cid" => true,
        "hgt" => {
          let height = v[0..(v.len() - 2)].parse().unwrap_or(0);
          match &v[(v.len() - 2)..] {
            "cm" => (150..=193).contains(&height),
            "in" => (59..=76).contains(&height),
            _ => false
          }
        },
        _ => unreachable!()
      })
}