def read_customer_data(filename):
    """Read and return data from filename as a list of lists (name, state, debt)"""
    names = []
    states = []
    debts = []

    with open(filename) as f:
        rows = f.readlines()
    for row in rows:
        row = row.split(',')
        names.append(row[0])
        states.append(row[1])
        debts.append(float(row[2].strip()))
    return names, states, debts

def highest_debt(debts, names, num):

    current_highest_debt = [min(debts), 0]

    if num > len(names): num = len(names)  

    count = -1
    for i in range(num): #Loops through specifified number of customers
        count += 1
        if debts[i] > current_highest_debt[0]:
            current_highest_debt[0], current_highest_debt[1] = debts[i], count

    return current_highest_debt[0], names[current_highest_debt[1]]

def starter_check(phrase, names, num):

    if num > len(names): num = len(names)

    starts_with_phrase = 0
    for i in range(num):
        if names[i].startswith(phrase):
            starts_with_phrase += 1
    return starts_with_phrase

def debt_check(debt_limiter, debts, num):

    if num > len(debts): num = len(debts)

    has_debt = 0
    debt_free = 0

    for i in range(num):
        if debts[i] > debt_limiter:
            has_debt += 1
        elif debts[i] == 0:
            debt_free += 1

    return debt_free, has_debt

def list_to_state(state, names, debts, num, states):

    cut_names = []
    cut_debts = []

    for i in range(num):
        if states[i] == state:
            cut_names.append(names[i])
            cut_debts.append(debts[i])

    return cut_names, cut_debts

# Main portion of the program
if __name__ == '__main__':
    # number of rows to consider
    num_customers = int(input())


    names, states, debts = read_customer_data("CustomerData.csv")

    # Type your code here.
    debt_limiter = int(input())
    search_phrase = input()
    state_abbreviation = input()

    most_debt, person_highest_debt = highest_debt(debts, names, num_customers)
    string_starts = starter_check(search_phrase, names, num_customers)
    debt_free, has_debt = debt_check(debt_limiter, debts, num_customers)

    print("U.S. Report")
    print(f"Customers: {num_customers}")
    print(f"Highest debt: {person_highest_debt}")
    print(f'Customer names that start with "{search_phrase}": {string_starts}')
    print(f"Customers with debt over ${debt_limiter}: {has_debt}")
    print(f"Customers debt free: {debt_free}")

    state_names, state_debts = list_to_state(state_abbreviation, names, debts, num_customers, states)

    most_debt, person_highest_debt = highest_debt(state_debts, state_names, num_customers) #FOR STATE
    string_starts = starter_check(search_phrase, state_names, num_customers)
    debt_free, has_debt = debt_check(debt_limiter, state_debts, num_customers)

    print(f"\n{state_abbreviation} Report")
    print(f"Customers: {len(state_names)}")
    print(f"Highest debt: {person_highest_debt}")
    print(f'Customer names that start with "{search_phrase}": {string_starts}')
    print(f"Customers with debt over ${debt_limiter}: {has_debt}")
    print(f"Customers debt free: {debt_free}")