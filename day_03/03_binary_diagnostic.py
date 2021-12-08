import numpy as np

OXYGEN = 'oxygen'
CO2 = 'co2_scrubber'


def convert_to_decimal(val):
    val = ''.join([str(v) for v in val])
    return int(val, 2)


def read_input(file):
    diag = []
    with open(file, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            diag.append([int(v) for v in line.strip()])
    arr = np.array(diag)
    return arr


def get_power_rates(file):
    arr = read_input(file)
    gamma = (arr.mean(axis=0) >= 0.5).astype(int)
    epsilon = (arr.mean(axis=0) < 0.5).astype(int)
    return convert_to_decimal(gamma), convert_to_decimal(epsilon)


def get_common_bit(arr, idx, most=True):
    if most:
        return (arr[:, idx].mean(axis=0) >= 0.5).astype(int)
    else:
        return (arr[:, idx].mean(axis=0) < 0.5).astype(int)


def get_rate(arr, which=OXYGEN):
    most = False
    if which == OXYGEN:
        most = True
    num_bits = arr.shape[1]
    f_arr = arr
    for i in range(num_bits):
        filter_bit = get_common_bit(f_arr, i, most=most)
        mask = f_arr[:, i] == filter_bit
        f_arr = f_arr[mask, :]
        dim = f_arr.shape
        if dim[0] == 1:
            print(f_arr[0])
            return f_arr[0]


def get_life_support_rates(file):
    arr = read_input(file)
    oxygen_rate = get_rate(arr, OXYGEN)
    co2_rate = get_rate(arr, CO2)
    return convert_to_decimal(oxygen_rate), convert_to_decimal(co2_rate)


if __name__ == '__main__':
    FILE = 'input.txt'
    g, e = get_power_rates(FILE)
    print(f"We have gamma: {g} and epsilon: {e} which a power of {g * e}")
    oxy, co2 = get_life_support_rates(FILE)
    print(f"Oxy: {oxy}, CO2: {co2}, {oxy * co2}")
