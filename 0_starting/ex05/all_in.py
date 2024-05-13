import sys

def all_in(expressions):
    # print(expressions)
    states = {
    "Oregon" : "OR",
    "Alabama" : "AL",
    "New Jersey": "NJ",
    "Colorado" : "CO"
    }
    capital_cities = {
    "OR": "Salem",
    "AL": "Montgomery",
    "NJ": "Trenton",
    "CO": "Denver"
    }
    expressions = [expr.strip() for expr in expressions.split(',')]
    # print(expressions)
    # print('hello')
    for expr in expressions:
        # Skip empty expressions
        if not expr:
            continue
        
        expr_lower = expr.lower()

        # Check if the expression is a state
        if expr_lower in [state.lower() for state in states.keys()]:
            state_item = [item for item in states.items() if item[0].lower() == expr_lower][0]
            capital = capital_cities[state_item[1]]
            print(f"{capital} is the capital of {state_item[0]}")
        # Check if the expression is a capital city
        elif expr_lower in [city.lower() for city in capital_cities.values()]:
            state_abbr = [key for key, value in capital_cities.items() if value.lower() == expr_lower][0]
            state = [key for key, value in states.items() if value.upper() == state_abbr][0]
            print(f"{capital_cities[state_abbr]} is the capital of {state}")
        else:
            print(f"{expr} is neither a capital city nor a state")



if __name__ == '__main__':
    if len(sys.argv) != 2 :
        sys.exit(1)
    all_in(sys.argv[1])