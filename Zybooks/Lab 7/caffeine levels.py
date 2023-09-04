caffeine_mg = float(input())

''' Type your code here. '''

def caffeine_half_life(caffeine):
    half_life_key = {
        0: caffeine
    }

    time_start = 6

    for i in range(3):
        starting_caffeine = caffeine
        end_caffeine = starting_caffeine/(2**(time_start/6))
        half_life_key[time_start] = end_caffeine
        time_start *= 2


    return half_life_key


def main():
    caffeine_amount = caffeine_half_life(caffeine_mg)
    del(caffeine_amount[0])

    for key in caffeine_amount:
        print("After " + str(key) + f" hours: {caffeine_amount[key]:.2f} mg")

if __name__ == "__main__":
    main()