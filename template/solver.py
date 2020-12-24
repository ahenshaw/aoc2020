from logging import basicConfig, info, debug, log, DEBUG, INFO
basicConfig(level=INFO, format='%(message)s')

fn = "input.txt"
fn = "test.txt"
# fn = "test2.txt"

# parse the data
# data = open(fn).readlines()

# for line in open(fn):
#     pass

data = open(fn).read().split('\n\n')
