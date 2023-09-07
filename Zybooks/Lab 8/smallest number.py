
def smallest_number(list):


    list.sort()

    return list[0]

def main():
    input_1 = input()
    input_2 = input()
    input_3 = input()

    input_list = [int(input_1), int(input_2), int(input_3)]

    print(smallest_number(input_list))



if __name__ == "__main__":
    main()