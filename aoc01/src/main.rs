use std::io::{self, Read};
use anyhow::{Result, anyhow};

fn main() -> Result<()> {
    println!("Advent of Code - Day 01");
    let mut input = String::new();
    io::stdin().read_to_string(&mut input)?;
    let data: Vec<i64> = input.lines()
                              .map(|x| x.parse::<i64>()
                              .unwrap())
                              .collect();
    part1(&data)?;
    part2(&data)?;
    Ok(())
}

fn part1(data: &Vec<i64>) -> Result<()> {
    for &i in data {
        for &j in data {
            if i + j == 2020 {
                println!("Part 1: {}, {}, {}", i, j, i * j);
                return Ok(());
            }
        }
    }
    Err(anyhow!("No solution found"))
}

fn part2(data: &Vec<i64>) -> Result<()> {
    for &i in data {
        for &j in data {
            if i + j > 2020 {
                continue;
            }
            for &k in data {
                if i + j + k == 2020 {           
                   println!("Part 2: {}, {}, {}, {}", i, j, k, i * j * k);
                   return Ok(());
                }
            }
        }
    }
    Err(anyhow!("No solution found"))
}
