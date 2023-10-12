SECT_112 = 203
SECT_113 = 121
SECT_116 = 28

def main():
    """
    This function uses input to receive a count of the three different section seats. Then,
    it will call each section from the class_total() function and use the new variables in 
    calling the income() function.
    """
    s_112 = int(input("Enter the count of Section 112 seats: "))
    s_113 = int(input("Enter the count of Section 113 seats: "))
    s_116 = int(input("Enter the count of Section 116 seats: "))

    income_112 = class_total(s_112, "112")
    income_113 = class_total(s_113, "113")
    income_116 = class_total(s_116, "116")

    income(income_112, income_113, income_116)

def class_total(seat, seating):
    """
    This function will use if statements to determine which calculation needs to be done for
    each section, using the global constants to calculate the income.
    """
    if seating == "112":
        return seat * SECT_112

    if seating == "113":
        return seat * SECT_113

    if seating == "116":
        return seat * SECT_116

def income(s_112, s_113, s_116):
    """
    This function will print the formatted individual income from each section, including the 
    grand total of income.
    """
    total = s_112 + s_113 + s_116
    print(f'Income from Section 112 seats: $ {s_112:,}')
    print(f'Income from Section 113 seats: $ {s_113:,}')
    print(f'Income from Section 116 seats: $ {s_116:,}')
    print(f'\nTotal income:\t\t       $ {total:,}')

# Call the main function.
if __name__ == '__main__':
    main()
