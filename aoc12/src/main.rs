use std::io::prelude::*;
use std::{fs, io};

type Step = (String, f32);
type Steps = Vec<Step>;

fn main() {
    let f = fs::File::open("input.txt").unwrap();
    let reader = io::BufReader::new(f);
    let steps: Steps = reader
        .lines()
        .map(|line| {
            let line = line.unwrap();
            let (cmd, num) = line.split_at(1);
            (cmd.to_string(), num.parse::<f32>().unwrap())
        })
        .collect();

    part1(&steps);
    part2(&steps);
}

fn part1(steps: &Steps) {
    let mut x = 0.0;
    let mut y = 0.0;
    let mut facing = 0.0;
    for (cmd, num) in steps {
        match &cmd[..] {
            "N" => y += num, 
            "S" => y -= num, 
            "E" => x += num, 
            "W" => x -= num, 
            "L" => facing += num,
            "R" => facing -= num,
            "F" => {
                x += facing.to_radians().cos() * num;
                y += facing.to_radians().sin() * num;    
            }
            _ => (),
        };
    }
    println!("Part 1: {:0.0}", x.abs() + y.abs());
}

fn part2(steps: &Steps) {
    let mut x = 0.0;
    let mut y = 0.0;
    let mut wx = 10.0;
    let mut wy = 1.0;
    for (cmd, num) in steps {
        match &cmd[..] {
            "N" => wy += num, 
            "S" => wy -= num, 
            "E" => wx += num, 
            "W" => wx -= num, 
            "L" => {
                let theta = wy.atan2(wx).to_degrees() + num;
                let magnitude = (wx*wx + wy*wy).sqrt();
                wx = magnitude * theta.to_radians().cos();
                wy = magnitude * theta.to_radians().sin();
            },
            "R" => {
                let theta = wy.atan2(wx).to_degrees() - num;
                let magnitude = (wx*wx + wy*wy).sqrt();
                wx = magnitude * theta.to_radians().cos();
                wy = magnitude * theta.to_radians().sin();
            },
            "F" => {
                x += wx * num;
                y += wy * num;
            }
            _ => (),
        };
    }
    println!("Part 2: {:0.0}", x.abs() + y.abs());
}
