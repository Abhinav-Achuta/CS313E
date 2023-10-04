from example_007_queue import Queue

class stack_adapter():

    def __init__(self):

        self.queue1 = Queue()

        self.queue2 = Queue()

    def push(self, item):

        self.queue1.enqueue(item)
    
    def pop(self):
        
        if self.queue1.isEmpty():
            return None

        pop_item = self.queue1.dequeue()

        return pop_item
    
    def peek(self):

        if self.queue1.isEmpty():
            return None
        
        peek_item = self.queue1.dequeue()
        self.queue2.enqueue(peek_item)

        #print(f"Test queue1 and queue2: {self.queue1} and {self.queue2}")

        while self.queue1.size() > 0:

            self.queue2.enqueue(self.queue1.dequeue())
        
        #print(f"Test queue1 and queue2: {self.queue1} and {self.queue2}")

        self.queue1, self.queue2 = self.queue2, self.queue1

        #print(f"Test queue1 and queue2: {self.queue1} and {self.queue2}")

        return peek_item
    
def main():

    queue = stack_adapter()

    queue.push(10)
    queue.push(20)
    queue.push(300)
    print(f"Queue: {queue.queue1}\n")


    print(f"Peek: {queue.peek()}")
    print(f"Pop: {queue.pop()}")
    print(f"Queue: {queue.queue1}\n")

    print(f"Peek: {queue.peek()}")
    print(f"Pop: {queue.pop()}")
    print(f"Queue: {queue.queue1}\n")

    print(f"Peek: {queue.peek()}")
    print(f"Pop: {queue.pop()}")
    print(f"Queue: {queue.queue1}\n")


if __name__ == "__main__":
    main()