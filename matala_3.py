
from copy import deepcopy
from prettytable import PrettyTable
from votes_arrays import votes, votes_from_325


NUM_OF_SEATS = 120

def Adams(votes_arr):
    seats = 0
    while(seats < NUM_OF_SEATS):
        max, maxName = 0, ''
        for name in votes_arr:
            fs = votes_arr[name]['seats']
            if fs != 0 and (votes_arr[name]['votes'] / fs) > max:
                max = votes_arr[name]['votes'] / fs
                maxName = name
            elif fs == 0:
                maxName = name
                break
        votes_arr[maxName]['seats'] += 1
        seats += 1
    print_results(votes_arr, 'Adams')

def Jefferson(votes_arr):
    seats = 0
    while(seats < NUM_OF_SEATS):
        max, maxName = 0, ''
        for name in votes_arr:
            fs = votes_arr[name]['seats'] + 1
            if (votes_arr[name]['votes'] / fs) > max:
                max = votes_arr[name]['votes'] / fs
                maxName = name
        votes_arr[maxName]['seats'] += 1
        seats += 1
    print_results(votes_arr, 'Jefferson')

def Webster(votes_arr):
    seats = 0
    while(seats < NUM_OF_SEATS):
        max, maxName = 0, ''
        for name in votes_arr:
            fs = votes_arr[name]['seats'] + 0.5
            if (votes_arr[name]['votes'] / fs) > max:
                max = votes_arr[name]['votes'] / fs
                maxName = name
        votes_arr[maxName]['seats'] += 1
        seats += 1
    print_results(votes_arr, 'Webster')

def print_results(votes_arr, method_name=str):
    t = PrettyTable(['Party name', method_name+'_seats', 'actual_seats', 'difference'])
    for name in votes_arr:
        t.add_row([name, votes_arr[name]['seats'],votes_arr[name]['actual'], votes_arr[name]['actual'] - votes_arr[name]['seats']])
    print(t)

if __name__ == "__main__":

    print("-------Adams-------")
    Adams(deepcopy(votes))
    print("\n")

    print("-------Jefferson-------")
    Jefferson(deepcopy(votes))
    print("\n")

    print("-------Webster-------")
    Webster(deepcopy(votes))
    print("\n==================================== parties with at least 3.25% of votes ====================================\n")

## parties with at least 3.25% votes
    print("-------Adams-------")
    Adams(deepcopy(votes_from_325))
    print("\n")

    print("-------Jefferson-------")
    Jefferson(deepcopy(votes_from_325))
    print("\n")

    print("-------Webster-------")
    Webster(deepcopy(votes_from_325))
