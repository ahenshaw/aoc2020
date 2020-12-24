use std::fmt;
use std::time::Instant;

fn main() {
    const MIN: usize = 1;
    const MAX: usize = 1_000_000;

    let start: Instant = Instant::now();
    // let data:Vec<usize> = vec![3,8,9,1,2,5,4,6,7]; // test input
    let data:Vec<usize> = vec![2,8,4,5,7,3,9,6,1]; // real input

    let mut cups = Cups::new(MAX);
    for cup in data {
        cups.append(cup);
    }
    for cup in 10..=MAX {
        cups.append(cup);
    }
    for _ in 1..=10_000_000 {
        let current = cups.head;
        let pickup = cups.cut(current, 3);
        let mut dest = current - 1;
        loop {
            if dest < MIN {
                dest = MAX;
            }
            if !pickup.contains(&dest) {
                break;
            }
            dest -= 1;
        }
        cups.insert(dest, pickup);
        cups.rotate();
    }
    while cups.head != 1 {
        cups.rotate();
    }
    let a = cups.get(cups.head);
    let b = cups.get(a);

    println!("Part 2: {}", a*b);
    println!("Elapsed: {:?}", Instant::now() - start);
}

struct Cups {
    head: usize,
    tail: usize,
    llist: Vec<usize>,
}

impl Cups {
    fn new(capacity: usize) -> Cups {
        Cups {head: 0, 
              tail: 0, 
              llist: (0..=capacity).collect()
        }
    }

    fn set(&mut self, cup: usize, next_cup: usize) {
        self.llist[cup] = next_cup;
    }

    fn get(&self, cup: usize) -> usize {
        self.llist[cup]
    }

    fn append(&mut self, cup: usize) {
        if self.head == 0 {
            self.head = cup;
            self.tail = cup;
            self.set(cup, cup);
        } else {
            let temp = self.get(self.tail);
            self.set(cup, temp);
            self.set(self.tail, cup);
            self.tail = cup;
        }
    }

    fn rotate(&mut self) {
        self.tail = self.head;
        self.head = self.get(self.head);
    }
    
    fn cut(&mut self, cursor: usize, n: usize) -> Vec<usize> {
        let mut chain = Vec::<usize>::new();
        let start = cursor;
        let mut cursor = cursor;
        for _ in 0..n {
            cursor = self.get(cursor);
            chain.push(cursor);
        }
        self.set(start, self.get(cursor));
        chain
    }
    
    fn insert(&mut self, cup: usize, chain: Vec<usize>) {
        let temp = self.get(cup);
        self.set(cup, *chain.first().unwrap());
        self.set(*chain.last().unwrap(), temp);
    }
}

impl fmt::Display for Cups {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        let mut cursor = self.head;
        let mut out = String::new();
        if self.llist.len() > 0 {
            loop {
                out += format!("{}", cursor).as_str();
                cursor = self.get(cursor);
                if cursor == self.head {
                    break;
                }
            }
        }
        write!(f, "{}", out)
    }
}


