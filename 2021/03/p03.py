#!/usr/bin/env python3

def part1(inputs: list[list[int]]):
    bit_length = len(inputs[0])
    mcb = list() # most common bits
    lcb = list() # least common bits
    for bit_pos in range(bit_length):
        stat = stats([bits[bit_pos] for bits in inputs])
        mcb.append(stat['most_common_key'])
        lcb.append(stat['least_common_key'])

    gamma = decimal_from_bits(mcb)
    epsilon = decimal_from_bits(lcb)

    print(f"answer={gamma*epsilon}, gamma={gamma}, epsilon={epsilon}")

def part2(inputs: list[list[int]]):
    bit_length = len(inputs[0])
    inputs_o2, inputs_co2 = inputs.copy(), inputs.copy()

    def filter_func(bits: list[int], bit_pos, mcb, lcb, choose, if_eq):
        cmp_var = mcb if choose == 'mcb' else lcb
        if mcb == lcb:
            return bits[bit_pos] == if_eq
        elif bits[bit_pos] == cmp_var:
            return True
        else:
            return False

    for bit_pos in range(bit_length):
        if (len(inputs_o2) > 1):
            stat_o2 = stats([bits[bit_pos] for bits in inputs_o2])
            mcb, lcb= stat_o2['most_common_key'], stat_o2['least_common_key']
            inputs_o2 = list(filter(lambda x: filter_func(x, bit_pos, mcb, lcb, 'mcb', 1), inputs_o2))

        if (len(inputs_co2) > 1):
            stat_co2 = stats([bits[bit_pos] for bits in inputs_co2])
            mcb, lcb = stat_co2['most_common_key'], stat_co2['least_common_key']
            inputs_co2 = list(filter(lambda x: filter_func(x, bit_pos, mcb, lcb, 'lcb', 0), inputs_co2))

    o2_rating = decimal_from_bits(inputs_o2[0])
    co2_rating = decimal_from_bits(inputs_co2[0])
    print(f"answer={o2_rating * co2_rating}, o2_rating={o2_rating}, co2_rating={co2_rating}")

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
    freq_dict = dict({0: 0, 1: 0})
    for item in items:
        new_val = freq_dict.get(item, 0) + 1
        freq_dict.update({ item: new_val })

    return freq_dict

def decimal_from_bits(bits: list[int]):
    return int("".join([str(_) for _ in bits]), 2)

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
    # inputs = test_input()
    inputs = read_input()
    part1(inputs)
    part2(inputs)
