import numpy as np

CONSTANT = 'constant'
LINEAR = 'linear'


def read_file(file):
    with open(file, 'r', encoding='utf-8') as f:
        crab_pos = [int(v) for v in f.readline().split(',')]
        return crab_pos


def compute_conso(crab_pos, pos, fuel_method=CONSTANT):
    steps = np.abs(crab_pos - pos)
    if fuel_method == LINEAR:
        steps = steps * (steps + 1) / 2
    total = int(np.sum(steps))
    return total


def compute_fuel(file, fuel_consumption=CONSTANT):
    crab_pos = np.array(read_file(file))
    if fuel_consumption == CONSTANT:
        position = int(np.median(crab_pos))
    else:
        position = int(np.mean(crab_pos))
    print(f"Crabs go to position {position}")
    fuel_consumed = compute_conso(crab_pos, position, fuel_consumption)
    return fuel_consumed


if __name__ == '__main__':
    FILE = 'input.txt'
    fuel = compute_fuel(FILE)
    print(f"Fuel used is: {fuel}")
    fuel = compute_fuel(FILE, LINEAR)
    print(f"Fuel used is: {fuel}")
