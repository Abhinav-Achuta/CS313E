from example_006_stack import Stack

class queue_adapter:

    def __init__(self):

        self.stack1 = Stack()

        self.stack2 = Stack()

    def enqueue(self, item):

        self.stack1.push(item)

    def dequeue(self):

        if self.stack2.isEmpty():

            for i in range(self.stack1.size()):
                self.stack2.push(self.stack1.pop())

        item_to_relay = self.stack2.pop()

        #print(f"This is stack2: {self.stack2}")

        for i in range(self.stack2.size()):
            self.stack1.push(self.stack2.pop())
        
        #print(f"This is stack1: {self.stack1}")

        if item_to_relay:
            return item_to_relay
        else:
            return "Queue is empty"
    
    def __str__(self):
        return f"Current queue: {self.stack1}"

def main():

    queue = queue_adapter()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    print(f"Your queue: {queue}")

    print(f"Item to be dequeued: {queue.dequeue()}")
    print(f"Item to be dequeued: {queue.dequeue()}")
    print(f"Item to be dequeued: {queue.dequeue()}")

if __name__ == "__main__":
    main()



