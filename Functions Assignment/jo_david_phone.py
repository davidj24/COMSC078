import math

# David Jo. Assignment 1 "Functions" Part 3
# Program purpose: To calculate the costs of 2 phone plans and also output the cheaper one 
# given a number of units used

def get_units():
    units = int(input("Enter number of units used: "))
    return units


def calculate_cost(num_units, base_cost, base_lim, extra_unit_cost):
    if (num_units < base_lim):
        return base_cost
    cost = base_cost
    num_units -= base_lim
    cost += extra_unit_cost * num_units
    return cost


def main():
    num_units = get_units()
    if (num_units < 0):
        print(f"you didn't use a negative number of units -_-")
    else:
        plan1_cost = calculate_cost(num_units, 9.38, 65, .045)
        plan2_cost = calculate_cost(num_units, 8.57, 50, .052)
        print(f'Cost for plan 1: ${plan1_cost:.2f}')
        print(f'Cost for plan 2: ${plan2_cost:.2f}')
        if (plan1_cost < plan2_cost):
            cheap_plan = f"Plan 1"
        else:
            cheap_plan = f"Plan 2"
        print(f"{cheap_plan} is cheaper.")

if __name__=='__main__':
    main()