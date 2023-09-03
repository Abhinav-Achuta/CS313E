def income_tax(data):
    results = {
        "Input wages": [],
        "Taxable interest": [],
        "Unemployment compensation": [],
        "Status": [],
        "Taxes withheld": [],
    }
    final_data_key = {
        "AGI": [],
        "Deduction": [],
        "Taxable income": [],
        "Federal tax": [],
        "Tax due": [],
    }

    initial_agi_data = []
    raw_list = data.split()

    if len(raw_list) != len(results):
        return "Invalid input. Please provide all required fields."

    #Adding each field to the key for further calculations
    for i in range(len(raw_list)):
        key = list(results.keys())[i]
        results[key].append(raw_list[i])

    initial_agi_data.append(agi(results["Input wages"], results["Taxable interest"], results["Unemployment compensation"]))

    if len(initial_agi_data[0]) > 1:
        return f"AGI: ${initial_agi_data[0][0]:,}" + "\nError: Income too high to use this form"
    else:
        #Calculate AGI
        final_data_key["AGI"].append(initial_agi_data[0][0])

        #Calculate deduction and taxable income
        deduction, taxable_income = deduction_amount(results["Status"][0], final_data_key["AGI"][0])
        final_data_key["Deduction"].append(deduction)
        final_data_key["Taxable income"].append(taxable_income)

        #Calculate tax amount
        final_data_key["Federal tax"].append(federal_tax(results["Status"], final_data_key["Taxable income"]))

        #Calculate tax due
        refund, tax = tax_due(results["Taxes withheld"], final_data_key["Federal tax"])
        final_data_key["Tax due"].append(tax)
        tax_due_text = ""
        if refund:
            tax_due_text = "Tax refund: "
        else:
            tax_due_text = "Taxes Owed: "

        return f"AGI: ${final_data_key['AGI'][0]:,}" + f"\nDeduction: ${final_data_key['Deduction'][0]:,}" + f"\nTaxable income: ${final_data_key['Taxable income'][0]:,}" + f"\nFederal tax: ${final_data_key['Federal tax'][0]:,}" + "\n" + tax_due_text + f"${final_data_key['Tax due'][0]:,}"

def tax_due(withheld, federal_tax):

    tax_due = federal_tax[0] - int(withheld[0])

    if tax_due < 0:
        refund = True
    else:
        refund = False
    
    return refund, abs(tax_due)

def agi(wages, interest, unemployment):

    wages = int(wages[0])
    interest = int(interest[0])
    unemployment = int(unemployment[0])

    agi_calculation = wages + interest + unemployment

    if agi_calculation > 120000:
        return [agi_calculation, "Error"]
    else:
        return [agi_calculation]

def deduction_amount(status, AGI):
    deduction = 0
    status = int(status)

    if status == 2:
        deduction = 24000
    else:
        deduction = 12000
    
    taxable_income = AGI - deduction
    if taxable_income < 0:
        taxable_income = 0

    return deduction, taxable_income

def federal_tax(status, taxable_income):
    status = int(status[0])
    taxable_income = taxable_income[0]

    #If filing as single status
    if status != 2:
        if 0 <= taxable_income <= 10000:
            federal_tax = taxable_income*.1
        if 10001 <= taxable_income <= 40000:
            federal_tax = 1000 + ((taxable_income-10000)*.12)
        if 40001 <= taxable_income <= 85000:
            federal_tax = 4600 + ((taxable_income-40000)*.22)
        if 85000 <= taxable_income:
            federal_tax = 14500 + ((taxable_income-85000)*.24)
    if status == 2:
        if 0 <= taxable_income <= 20000:
            federal_tax = taxable_income*.1
        if 20001 <= taxable_income <= 80000:
            federal_tax = 2000 + ((taxable_income-20000)*.12)
        if 80000 <= taxable_income <= 85000:
            federal_tax = 9200 + ((taxable_income-80000)*.22)
    
    federal_tax = round(federal_tax)
    
    return federal_tax

def main():
    tax_form = input()
    print(income_tax(tax_form))

if __name__ == "__main__":
    main()