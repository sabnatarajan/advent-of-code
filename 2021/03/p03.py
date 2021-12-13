#!/usr/bin/env python3

def part1(inputs: list[list[int]]):
    bit_length = len(inputs[0])
    mcb = list() # most common bits
    lcb = list() # least common bits
    for i in range(bit_length):
        stat = stats([bits[i] for bits in inputs])
        mcb.append(stat['most_common_key'])
        lcb.append(stat['least_common_key'])

    gamma = int("".join([str(_) for _ in mcb]), 2)
    epsilon = int("".join([str(_) for _ in lcb]), 2)

    print(gamma * epsilon)

def part2(inputs: list[list[int]]):
    pass

def stats(bits: list[int]):
    most_common_key = None
    most_common_val = -1
    least_common_key = None
    least_common_val = 2**31-1

    for k, v in freq(bits).items():
        if v > most_common_val:
            most_common_val = v
            most_common_key = k
        if v < least_common_val:
            least_common_val = v
            least_common_key = k

    return {
        "most_common_key": most_common_key,
        "most_common_val": most_common_val,
        "least_common_key": least_common_key,
        "least_common_val": least_common_val,
    }



def freq(items: list) -> dict:
    freq_dict = dict()
    for item in items:
        new_val = freq_dict.get(item, 0) + 1
        freq_dict.update({ item: new_val })

    return freq_dict

def test_input() -> list[list[int]]:
    return [[0,0,1,0,0], 
            [1,1,1,1,0], 
            [1,0,1,1,0], 
            [1,0,1,1,1], 
            [1,0,1,0,1], 
            [0,1,1,1,1], 
            [0,0,1,1,1], 
            [1,1,1,0,0], 
            [1,0,0,0,0], 
            [1,1,0,0,1], 
            [0,0,0,1,0], 
            [0,1,0,1,0]]

def read_input() -> list[list[int]]:

    bit_matrix = list(list())
    with open('input.txt', 'r') as f:
        for line in f.readlines():
            bit_matrix.append([int(_) for _ in line.strip()])

        return bit_matrix

if __name__ == "__main__":
    inputs = read_input()
    part1(inputs)
    part2(inputs)
