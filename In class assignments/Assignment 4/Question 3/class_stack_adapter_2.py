from example_008_linked_list import LinkedList

 

class stack_adapter2:

    def __init__(self):

        self.list=LinkedList()

    def push(self, item):
        self.list.insertFirst(item)

    def pop(self):
        item_popped = self.list.deleteLink(self.list.first.data)

        return item_popped

    def peek(self):
        
        return self.list.first.data
    
def main():

    linked_list = stack_adapter2()

    linked_list.push(10)
    linked_list.push(30)
    linked_list.push(50)

    print(f"Current linked list: {linked_list.list}")
    print(f"Linked list peek: {linked_list.peek()}")
    print(f"Linked list popped: {linked_list.pop()}\n")

    print(f"Current linked list: {linked_list.list}")
    print(f"Linked list peek: {linked_list.peek()}")
    print(f"Linked list popped: {linked_list.pop()}\n")

    print(f"Current linked list: {linked_list.list}")
    print(f"Linked list peek: {linked_list.peek()}")
    print(f"Linked list popped: {linked_list.pop()}\n")

if __name__ == "__main__":
    main()