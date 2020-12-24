class Cups:
    def __init__(self):
        self.head = None
        self.llist = {}
    
    def set(self, x, y):
        self.llist[x] = y
    
    def get(self, x):
        return self.llist[x]

    def append(self, x):
        if self.head is None:
            self.llist[x] = self.head = self.tail = x
        else:
            temp = self.get(self.tail)
            self.set(x, temp)
            self.set(self.tail, x)
            self.tail = x

    def rotate(self):
        self.tail = self.head
        self.head = self.get(self.head)

    def cut(self, x, n=3):
        chain = []
        start = x
        for i in range(n):
            chain.append(self.get(x))
            x = chain[-1]
        self.set(start, self.get(x))
        return chain
    
    def insert(self, x, chain):
        temp = self.get(x)
        self.set(x, chain[0])
        self.set(chain[-1], temp)

    def __str__(self):
        out = ''
        cursor = self.head
        while True:
            out += str(cursor)
            cursor = self.get(cursor)
            if cursor == self.head:
                return out
