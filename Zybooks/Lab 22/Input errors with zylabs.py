def main():

    max = 0
    input_read = 0

    try:
        input_1 = int(input())
        
        if input_1 > max:
            max = input_1
        input_read += 1

        input_2 = int(input())
        if input_2 > max:
            max = input_2
        input_read += 1
            
        input_3 = int(input())
        if input_3 > max:
            max = input_3
        input_read += 1

        print(max)
    except EOFError:
        if input_read != 0:
            print(f"{input_read} input(s) read:\nMax is {max}")
        else:
            print(f"{input_read} input(s) read:\nNo max")
        

if __name__ == "__main__":
    main()