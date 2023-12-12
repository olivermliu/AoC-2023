from math import prod

data = {
    1: "12 blue, 15 red, 2 green; 17 red, 8 green, 5 blue; 8 red, 17 blue; 9 green, 1 blue, 4 red",
    2: "6 red, 6 blue, 2 green; 1 blue, 1 red; 6 green, 1 red, 10 blue",
    3: "1 green, 2 blue; 7 blue, 4 green; 2 green, 1 blue; 10 blue, 4 green; 4 blue; 1 green, 7 blue, 1 red",
    4: "16 red, 12 blue, 10 green; 15 red, 5 green, 6 blue; 10 green, 15 red, 12 blue",
    5: "2 green, 2 red, 9 blue; 1 red, 5 green; 4 green, 12 blue, 1 red; 5 blue, 8 green",
    6: "17 blue, 3 green, 4 red; 6 green, 16 blue, 3 red; 2 red, 15 blue",
    7: "4 green, 10 red; 1 green, 4 red, 4 blue; 4 blue, 11 red",
    8: "8 green, 4 blue; 17 green, 4 red; 10 blue, 5 green, 9 red; 9 green, 8 red, 3 blue; 9 green, 5 red, 2 blue",
    9: "4 red, 2 green; 7 blue, 3 red, 3 green; 3 green, 7 blue, 3 red",
    10: "3 green, 2 red, 2 blue; 3 green, 11 red, 1 blue; 16 green, 11 red",
    11: "2 blue, 18 green; 12 blue, 1 green; 2 green, 6 blue; 1 red, 4 blue, 20 green; 14 blue, 1 red, 4 green",
    12: "2 green, 1 blue, 7 red; 11 red, 3 green, 6 blue; 1 red, 2 blue, 3 green; 4 red, 2 green, 5 blue",
    13: "4 red, 17 blue, 5 green; 6 blue, 2 green; 12 blue, 4 green, 2 red; 5 green, 9 blue; 5 green, 3 blue, 3 red; 4 green, 1 red, 7 blue",
    14: "4 blue, 18 green; 3 blue, 3 red, 13 green; 5 blue, 10 green; 10 green, 2 blue; 1 blue, 14 green; 3 blue, 18 green, 2 red",
    15: "1 green, 2 blue, 1 red; 1 green, 2 red, 1 blue; 1 green, 2 red; 1 green, 4 blue, 4 red; 6 blue, 2 red, 1 green; 3 blue, 2 red",
    16: "3 green, 2 red; 4 green, 1 red, 8 blue; 5 blue, 9 red, 3 green; 7 blue, 19 green, 18 red",
    17: "10 blue, 9 red, 7 green; 16 red, 11 green, 11 blue; 8 blue, 3 green; 12 red, 1 blue, 10 green",
    18: "11 green, 11 blue, 5 red; 7 red, 11 green, 13 blue; 5 green, 9 red, 6 blue; 9 red, 16 green, 17 blue",
    19: "8 red, 3 green, 16 blue; 13 green, 8 blue; 7 red, 8 green, 1 blue; 13 red, 3 blue, 7 green; 6 green, 14 blue, 13 red; 15 blue, 9 green, 13 red",
    20: "1 red, 7 green, 5 blue; 14 green, 4 blue; 10 green, 11 blue, 2 red; 2 red, 3 blue, 1 green; 1 red, 5 blue, 8 green",
    21: "10 green, 12 blue, 6 red; 17 blue, 6 red, 6 green; 12 blue, 9 green, 4 red; 5 blue, 3 red, 4 green; 6 green, 7 blue, 5 red",
    22: "1 blue, 3 red, 16 green; 4 red, 1 blue, 3 green; 12 green, 1 blue, 2 red; 12 red",
    23: "2 red, 6 blue, 1 green; 11 red, 13 blue, 4 green; 8 red, 3 blue, 6 green; 2 green, 8 blue, 2 red; 7 red, 11 blue, 4 green",
    24: "4 red, 12 green, 2 blue; 8 blue, 15 red; 1 blue, 10 green, 8 red; 1 green, 2 blue, 6 red; 10 green, 8 blue, 5 red",
    25: "2 blue, 11 green; 17 green, 1 red, 2 blue; 2 blue, 3 red, 1 green",
    26: "16 blue, 11 green; 4 green; 9 green, 4 blue; 10 green, 5 blue; 1 red, 5 blue, 9 green; 5 green, 5 blue",
    27: "10 green, 2 red; 5 blue, 1 red; 6 red, 5 green",
    28: "3 red, 5 green, 10 blue; 1 red, 5 green, 2 blue; 6 blue, 2 green, 2 red; 6 red, 9 blue, 1 green; 3 red; 3 red, 2 green, 2 blue",
    29: "8 red, 18 blue, 5 green; 1 blue, 8 red, 2 green; 2 red, 4 green, 18 blue; 6 red, 4 green, 7 blue",
    30: "1 red, 18 green; 11 green; 4 blue, 5 red, 14 green; 3 green, 8 blue, 2 red",
    31: "1 red, 5 blue, 17 green; 7 blue; 10 green, 8 blue, 1 red; 11 green, 4 blue",
    32: "5 blue, 15 red, 12 green; 6 red, 8 green, 8 blue; 2 red, 14 green, 3 blue; 4 blue, 15 green; 7 blue, 12 red, 7 green; 2 blue, 9 red, 7 green",
    33: "13 red, 2 green; 1 green, 7 red, 15 blue; 1 green, 14 blue, 13 red; 8 red, 2 green; 12 red, 14 blue, 10 green; 8 green, 16 blue, 10 red",
    34: "11 green, 9 blue, 2 red; 4 red, 1 green, 8 blue; 4 blue, 7 green, 4 red; 7 blue, 1 red, 8 green; 9 blue, 1 red, 4 green; 2 red, 10 green, 4 blue",
    35: "3 red, 9 blue; 11 blue, 3 red, 12 green; 7 green, 10 blue, 2 red",
    36: "9 blue, 3 green, 3 red; 5 blue, 1 red, 3 green; 2 green, 6 red; 9 blue, 7 red",
    37: "1 red, 7 blue; 4 red, 1 green; 1 green, 9 red, 9 blue",
    38: "1 green, 12 red; 4 green, 12 red, 4 blue; 5 green, 10 red; 6 red, 4 green, 3 blue; 4 green, 10 red; 2 green, 5 blue, 4 red",
    39: "2 blue; 4 red; 4 red, 5 green, 1 blue",
    40: "7 red, 2 green, 17 blue; 12 green, 1 red, 7 blue; 9 green, 2 red, 8 blue",
    41: "18 green, 5 red, 4 blue; 20 green, 17 blue, 5 red; 3 red, 7 blue, 7 green; 4 red, 19 green, 18 blue; 20 blue, 20 green",
    42: "1 green, 6 blue, 1 red; 5 blue, 1 red, 3 green; 3 green, 7 blue, 1 red",
    43: "4 blue, 6 green, 13 red; 16 red, 7 blue, 8 green; 4 green, 16 red",
    44: "5 green, 4 red, 13 blue; 4 red, 12 blue, 3 green; 6 green",
    45: "1 red, 17 blue, 15 green; 6 red, 3 green, 9 blue; 5 green, 1 blue, 7 red; 6 blue, 4 red, 4 green",
    46: "1 blue, 11 red, 1 green; 2 red, 2 green, 1 blue; 4 red, 1 green, 1 blue; 2 blue, 7 red, 3 green; 11 red, 3 green",
    47: "2 red, 1 blue; 1 green, 1 red, 1 blue; 5 green, 1 red",
    48: "9 blue, 1 red; 1 green, 2 red, 11 blue; 2 red, 6 blue",
    49: "5 blue, 7 red, 17 green; 5 red, 4 green, 7 blue; 1 red, 3 blue; 4 red, 12 green, 6 blue; 6 green, 4 blue, 3 red",
    50: "11 blue, 12 green, 1 red; 8 green, 7 red, 9 blue; 13 red, 12 blue, 10 green; 5 green, 10 blue, 3 red",
    51: "8 blue, 1 red; 5 red, 2 green; 9 blue, 6 red, 4 green; 4 green, 1 red, 13 blue; 15 blue, 3 red, 8 green; 6 red, 1 green, 4 blue",
    52: "2 blue, 1 red; 1 red, 4 blue, 5 green; 3 red, 14 blue, 2 green",
    53: "8 blue, 10 green, 11 red; 5 red, 4 blue, 19 green; 8 red, 3 blue; 3 red, 3 blue, 2 green; 4 red, 4 green",
    54: "3 green, 17 red; 7 green, 13 red, 5 blue; 11 blue, 10 red, 10 green; 3 green, 19 red, 4 blue; 11 green, 6 blue, 19 red; 5 red, 4 blue, 9 green",
    55: "3 blue, 4 red; 1 red, 1 blue, 2 green; 4 blue, 2 green, 4 red",
    56: "10 red, 3 green, 5 blue; 2 blue, 2 red; 7 red, 3 blue, 2 green",
    57: "12 red, 1 blue, 8 green; 1 blue, 3 green, 10 red; 5 green, 8 red",
    58: "6 red, 4 green, 2 blue; 7 red, 6 blue, 14 green; 5 blue, 6 red, 2 green; 2 red, 4 blue; 7 blue, 12 green; 7 green, 3 blue, 8 red",
    59: "6 red, 5 blue; 5 blue, 1 green; 1 blue, 6 red; 4 blue, 2 red, 1 green; 3 red, 2 blue; 3 blue, 5 red, 1 green",
    60: "1 red, 12 green, 2 blue; 4 red, 5 blue; 12 green, 1 red; 5 blue, 13 red, 17 green; 15 green, 1 blue",
    61: "10 blue, 18 red; 4 blue, 1 green, 14 red; 4 blue, 2 green; 2 green, 6 red, 10 blue",
    62: "2 green, 13 blue, 8 red; 7 green, 5 red, 8 blue; 5 red, 8 blue; 3 red, 5 green, 4 blue; 15 blue, 5 red, 6 green",
    63: "6 red, 7 green, 2 blue; 2 red, 6 green; 2 blue, 4 red, 5 green; 1 blue, 2 red, 5 green; 4 red, 8 green; 9 green, 2 red",
    64: "4 red, 4 blue; 7 blue, 5 red; 8 green, 5 red, 6 blue; 2 red, 3 blue, 1 green; 7 blue, 9 green, 7 red; 11 green, 2 red, 3 blue",
    65: "1 red, 11 green, 9 blue; 2 red, 5 green, 17 blue; 2 red, 3 blue, 6 green; 2 red, 6 green, 14 blue",
    66: "7 green, 5 red, 2 blue; 5 red, 7 green, 2 blue; 6 green, 3 blue, 15 red; 8 green, 20 red, 4 blue; 8 red, 8 green, 3 blue; 3 blue, 11 red, 5 green",
    67: "2 blue, 2 green; 6 blue, 1 green, 3 red; 3 red, 7 green, 4 blue; 1 red, 1 green, 8 blue",
    68: "1 green, 3 red; 2 green, 1 blue, 5 red; 2 red, 2 green, 1 blue; 2 green, 3 red, 1 blue; 6 red, 1 blue",
    69: "4 red, 2 green, 3 blue; 14 red; 3 blue; 11 red, 1 green; 13 red, 3 green, 2 blue",
    70: "1 green, 1 blue, 6 red; 1 green, 4 red, 1 blue; 6 red, 1 blue",
    71: "1 green, 8 blue, 10 red; 6 green, 3 red, 2 blue; 14 red, 3 green; 9 blue, 2 green, 2 red; 7 blue, 5 red, 1 green; 6 green, 5 blue, 10 red",
    72: "2 red, 10 blue; 1 red, 7 blue, 4 green; 1 red, 3 green, 6 blue",
    73: "6 red, 6 blue, 5 green; 1 blue, 11 green, 7 red; 10 red, 7 blue, 2 green",
    74: "4 green, 2 red, 3 blue; 1 red, 6 green; 2 red, 4 blue; 1 blue; 2 blue, 1 green",
    75: "10 red, 5 blue, 1 green; 12 blue; 2 green, 11 blue, 9 red; 1 blue, 14 red; 2 red, 2 green, 13 blue",
    76: "9 green, 1 blue; 8 green, 2 blue, 7 red; 4 blue, 7 green, 4 red",
    77: "14 red, 3 blue, 10 green; 3 blue, 7 green, 2 red; 5 red, 7 green, 3 blue; 14 red, 8 green, 3 blue; 9 green, 5 red; 2 blue, 7 red, 15 green",
    78: "5 blue, 9 green, 8 red; 11 green, 9 blue, 4 red; 8 red, 2 blue, 10 green; 3 blue, 7 green",
    79: "4 red, 6 blue, 10 green; 2 blue, 17 green, 15 red; 15 red, 6 blue, 14 green",
    80: "2 red, 8 green; 6 blue, 6 green; 1 green, 3 red, 8 blue; 5 green, 4 blue, 3 red; 3 blue, 1 red; 7 green, 8 blue, 3 red",
    81: "5 blue, 1 red; 10 blue, 7 red, 3 green; 4 green, 1 red, 10 blue; 8 red, 4 blue, 3 green; 11 blue, 9 green, 1 red; 6 red, 10 green",
    82: "1 green, 2 blue, 1 red; 2 blue, 1 green, 2 red; 2 red, 8 green; 3 red, 3 blue, 5 green",
    83: "3 blue, 4 green, 5 red; 6 blue, 5 red, 5 green; 4 red, 2 blue, 5 green; 2 green, 6 blue, 5 red; 1 red, 2 green",
    84: "14 blue, 1 green; 9 green, 3 red, 1 blue; 5 green, 10 blue, 3 red; 9 green; 6 green, 18 blue; 2 red, 8 green",
    85: "1 blue, 7 red; 12 green, 7 red, 5 blue; 9 blue, 6 green, 7 red; 10 red, 7 green, 1 blue; 3 green, 6 blue, 7 red; 10 red, 16 blue",
    86: "9 red, 10 blue, 2 green; 2 red, 12 blue, 9 green; 11 green, 2 blue, 3 red",
    87: "1 blue, 7 red, 9 green; 1 red, 6 blue; 3 blue, 12 green",
    88: "1 blue, 4 green; 4 red, 13 blue, 1 green; 7 green, 4 blue, 3 red; 2 blue, 4 green, 5 red; 4 red, 7 green, 10 blue; 1 red, 7 green, 13 blue",
    89: "5 blue, 8 red, 1 green; 7 blue, 2 green, 7 red; 2 green, 8 blue, 11 red",
    90: "5 blue, 1 green, 11 red; 6 blue, 8 red; 2 red, 3 blue, 4 green; 2 green, 4 blue, 7 red; 3 blue, 8 red; 6 red, 3 blue, 1 green",
    91: "2 green, 13 red, 9 blue; 12 blue, 6 green; 14 green, 10 blue, 3 red; 13 blue, 7 green, 5 red; 1 green, 9 blue, 14 red; 10 green, 8 blue, 17 red",
    92: "10 green, 3 red, 17 blue; 13 red, 7 green, 15 blue; 9 blue, 8 red, 4 green; 1 blue, 8 red; 9 red, 1 green, 19 blue",
    93: "1 blue, 7 green, 4 red; 2 blue, 8 green; 10 red, 10 green, 1 blue; 10 green, 2 blue; 3 red, 3 blue",
    94: "5 red, 8 green, 14 blue; 4 red, 7 green, 20 blue; 11 blue, 4 red, 13 green; 18 blue, 1 red, 3 green",
    95: "5 red, 8 green, 11 blue; 12 green, 5 blue; 4 blue, 14 green; 7 green, 9 blue, 5 red; 3 red, 4 green, 7 blue; 3 red, 12 blue, 3 green",
    96: "10 red, 12 blue, 9 green; 4 green, 8 blue, 4 red; 8 blue, 3 red, 4 green; 6 green, 10 red; 2 blue, 3 green, 15 red; 12 red, 2 green, 2 blue",
    97: "13 green, 1 blue; 9 green, 1 red, 1 blue; 6 blue, 10 green; 1 red, 6 blue, 11 green",
    98: "2 blue, 14 green, 2 red; 7 green, 1 blue; 1 blue, 1 red, 3 green; 2 red, 1 blue, 15 green; 1 blue, 2 red, 10 green",
    99: "3 green, 8 red, 7 blue; 6 red, 13 blue; 12 red, 4 green, 4 blue; 12 red, 8 green, 3 blue; 11 blue, 11 red, 4 green",
    100: "2 red, 13 blue, 1 green; 1 green, 12 blue; 1 red, 5 blue, 1 green; 3 blue, 3 red"
}

avail = {
    "red": 12,
    "green": 13,
    "blue": 14
}

id_sum_1 = 0
invalid_peek = False

for id, game in data.items():
    for peek in game.split(";"):  # each peek from bag
        for group in peek.strip().split(","):  # each group of colored balls
            amount, color = group.strip().split()
            if int(amount) > avail[color]:
                invalid_peek = True
                break
        if invalid_peek:
            break
    if invalid_peek:
        invalid_peek = False
    else:
        id_sum_1 += id

print(f"Sum of all possible game IDs for 1: {id_sum_1}")

id_sum_2 = 0

for id, game in data.items():
    max_amount = {"red": 0, "green": 0, "blue": 0}
    for peek in game.split(";"):  # each peek from bag
        for group in peek.strip().split(","):  # each group of colored balls
            amount, color = group.strip().split()
            max_amount[color] = max(max_amount[color], int(amount))
    id_sum_2 += prod(max_amount.values())

print(f"Sum of all possible game IDs for 2: {id_sum_2}")