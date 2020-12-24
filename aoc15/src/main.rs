use std::collections::HashMap;
use std::collections::VecDeque;

fn machine(data: &Vec<usize>, stop: usize) {
    let mut spoken: HashMap<usize, VecDeque<usize>> = HashMap::new();
    let mut last: usize = 0;

    for turn in 0..stop {
        let entries = spoken.entry(last).or_insert(VecDeque::new());
        if turn < data.len() {
            last = data[turn];
        } else {
            last = if entries.len() < 2 {0} else {entries[0] - entries[1]};
        }
        let entries = spoken.entry(last).or_insert(VecDeque::new());
        (*entries).push_front(turn);
    }
    println!("{}", last);

}
fn main() {
    let data: Vec<usize> = include_str!("../test.txt").split(",").map(|x| x.parse::<usize>().unwrap()).collect();
    machine(&data, 2020);
    machine(&data, 30_000_000);
}
