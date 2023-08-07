class ListQueue:
    def __init__(self):
        self.items = []
        self.size = 0
    
    def enqueue(self,data):
        self.items.insert(0,data)
        self.size += 1

    def dequeue(self):
        data = self.items.pop()
        self.size -= 1
        return data
    
    def traverse(self):
        total_items = self.size

        for item in range(total_items):
            print(self.items[item])


if __name__ == '__main__':
    food = ListQueue()
    food.enqueue('eggs')
    food.enqueue('ham')
    food.enqueue('spam')
    print(food.dequeue())
    food.traverse()