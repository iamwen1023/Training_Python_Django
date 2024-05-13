import sys

def state(city):
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
    key = ''
    for k, v in capital_cities.items():
        if v == city:
            key = k
            break
    if not key:
        print('Unknown capital city')
        return
    for k, v in states.items():
        if key == v:
            print(k)


if __name__ == '__main__':
    if len(sys.argv) != 2 :
        sys.exit(1)
    state(sys.argv[1])
    
