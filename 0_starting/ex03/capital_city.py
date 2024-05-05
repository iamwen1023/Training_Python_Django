import sys

def capital_city(state):
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
    if state not in states:
        print('Unknown state')
        return
    key = states[state]
    print(capital_cities[key])


if __name__ == '__main__':
    if len(sys.argv) != 2 :
        sys.exit(1)
    capital_city(sys.argv[1])
    
