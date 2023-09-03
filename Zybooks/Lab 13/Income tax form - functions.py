# Calculate AGI and repair any negative values
def calc_AGI(wages, interest, unemployment):
   
    wages = abs(wages)
    interest = abs(interest)
    unemployment = abs(unemployment)

    AGI = wages + interest + unemployment
    
    return AGI

# Calculate deduction depending on single, dependent or married
def get_deduction(status):

    status_key = {
        0 : 6000,
        1 : 12000,
        2 : 24000
    }

    if status in status_key:
        return status_key[status]
    else:
        return status_key[0]

# Calculate taxable but not allow negative results
def calc_taxable(agi, deduction):

    taxable_amount = agi - deduction
    
    if taxable_amount < 0:
        return 0
    else:
        return taxable_amount

# Calculate tax for single or dependent
def calc_tax(status, taxable):
    
    tax_brackets = {
        1: [
            (0, 10000, .1, 0, 0),
            (10001, 40000, .12, 10000, 1000),
            (40001, 85000, .22, 40000, 4600),
            (85001, float('inf'), .24, 85000, 14500)
        ],
        2: [
            (0, 20000, .1, 0, 0),
            (20001, 80000, .12, 20000, 2000),
            (80001, float('inf'), .22, 80000, 9200)
        ]
    }

    if status not in tax_brackets: #Because same calculation used as 1 for those that are not single or married
        status = 1

    if status in tax_brackets:
        for bracket in tax_brackets[status]:
            start, end, rate, amount_over, flat_amount = bracket
            if start <= taxable <= end:
                return int((taxable-amount_over)*rate + flat_amount)

# Calculate tax due and check for negative withheld
def calc_tax_due(tax, withheld):

    withheld = 0 if withheld < 0 else withheld

    tax_due = tax - withheld

    return tax_due

if __name__ == '__main__':
    # Step #1: Input wages, interest, unemployment, status, withheld
    information = input()
    information_list = information.split()
    field_names = ["wages", "interest", "unemployment", "status", "withheld"]
    information_key = {}

    for field in range(len(field_names)):
        information_key[field_names[field]] = int(information_list[field])

    #Calculate AGI
    information_key["agi"] = calc_AGI(information_key["wages"], information_key["interest"], information_key["unemployment"])
    print(f"AGI: ${information_key['agi']:,}")

    #Calculate deduction
    information_key["deduction"] = get_deduction(information_key["status"])
    print(f"Deduction: ${information_key['deduction']:,}")

    #Calculate taxable amount
    information_key["taxable amount"] = calc_taxable(information_key["agi"], information_key["deduction"])
    print(f"Taxable income: ${information_key['taxable amount']:,}")

    #Calculate tax amount
    information_key["tax"] = calc_tax(information_key["status"], information_key["taxable amount"])
    print(f"Federal tax: ${information_key['tax']:,}")

    #Calculate tax due
    information_key["tax due"] = calc_tax_due(information_key["tax"], information_key["withheld"])
    print(f"Tax due: ${information_key['tax due']:,}")
