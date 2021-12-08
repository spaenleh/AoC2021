from collections import Counter


def read_file(file):
    with open(file, 'r', encoding='utf-8') as f:
        return [int(v) for v in f.readline().split(',')]


def naive_lanternfish(fish_list, days):
    for d in range(1, days + 1):
        cold_fish = fish_list.copy()
        for i, fish_age in enumerate(cold_fish):
            if fish_age == 0:
                fish_list[i] = 6
                fish_list.append(8)
            else:
                fish_list[i] -= 1
    return len(fish_list)


def print_fish(string, r):
    print(string, "-" * 20)
    for a in range(9):
        print(f"{a}: {r.get(a)}")


def smart_lanternfish(fish_list, days):
    registry = dict(Counter(fish_list))
    for d in range(days):
        n_registry = registry.copy()
        # shifting
        for age in range(1, 9):
            if registry.get(age):
                n_registry[age - 1] = registry.get(age)
            else:
                n_registry[age - 1] = 0
        # the fish that were 0 at the beginning of the day give birth
        if registry.get(0):
            n_registry[6] += registry.get(0)
            n_registry[8] = registry.get(0)
        else:
            n_registry[8] = 0
        registry = n_registry.copy()
    return sum([v for v in registry.values()])


def compute_number_fish(file, days=80):
    fish_list = read_file(file)
    nbr_fish = smart_lanternfish(fish_list, days)
    return nbr_fish


if __name__ == '__main__':
    FILE = 'input.txt'
    nbr_fish = compute_number_fish(FILE, 80)
    print(f"There will be {nbr_fish}")
    nbr_fish = compute_number_fish(FILE, 256)
    print(f"There will be {nbr_fish}")
