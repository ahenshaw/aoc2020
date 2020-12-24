#![feature(str_split_once)]
use std::io::prelude::*;
use std::fs;
use std::collections::HashMap;

type Ticket = Vec<u32>;
type Fields = HashMap<String, Vec<u32>>;

fn parse_your_ticket(block: &str) -> Ticket {
    let (block_title, numbers) = block.split_once("\r\n").unwrap();
    numbers.split(",").map(|x| x.parse::<u32>().unwrap()).collect()
}

fn parse_nearby_tickets(block: &str) -> Vec<Ticket> {
    block
    .split("\r\n")
    .skip(1)
    .map(|line| line.split(",")
        .map(|x| x.parse::<u32>().unwrap()).collect::<Ticket>())
    .collect()
}

fn parse_fields(block: &str) -> Fields {
    HashMap::new()
}

fn main() {
    let mut data = String::new();
    let mut fh = fs::File::open("test.txt").unwrap();
    let mut your_ticket: Vec<u32> = vec![];
    let mut nearby_tickets: Vec<Ticket> = vec![];
    let mut fields: Fields;

    if let Ok(_) = fh.read_to_string(&mut data) {
        data.split("\r\n\r\n").for_each(|block| {
            if block.starts_with("your ticket") {
                your_ticket = parse_your_ticket(&block);
            } else if block.starts_with("nearby tickets") {
                nearby_tickets = parse_nearby_tickets(&block);
            } else {
                let fields:Fields = parse_fields(&block);
            }
        });
    }
    println!("{:?}", your_ticket);
    println!("{:?}", nearby_tickets);

}
