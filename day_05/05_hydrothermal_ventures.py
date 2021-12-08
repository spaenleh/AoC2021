START = 0
END = 1
X = 0
Y = 1

def read_file(file):
    with open(file, 'r', encoding='utf-8') as f:
        coords = []
        for line in f.readlines():
            coord = line.split('->')
            coords.append([tuple([int(v) for v in c.split(',')]) for c in coord])
        return coords


def no_diags(coords):
    n_coords = []
    for line in coords:
        if line[START][X] == line[END][X] or line[START][Y] == line[END][Y]:
            n_coords.append(line)
    return n_coords


def get_inc(d):
    if d > 0:
        return 1
    elif d < 0:
        return -1
    else:
        return 0


def get_path(line):
    point = line[START]
    path = [point]
    while point != line[END]:
        dx = line[END][X] - point[X]
        dy = line[END][Y] - point[Y]

        point = (point[X] + get_inc(dx), point[Y] + get_inc(dy))
        path.append(point)
    return path
    # for ddx in range(0, dx + (1 if dx > 0 else -1), 1 if dx > 0 else -1):
    #     for ddy in range(0, dy + (1 if dy > 0 else -1), 1 if dy > 0 else -1):
    #         x = line[START][X] + ddx
    #         y = line[START][Y] + ddy
    #         path.append((x, y))
    # return path


def compute_number_danger_zones(file, thresh=2, allow_diags=True):
    coords = read_file(file)
    # print(coords)
    if not allow_diags:
        # filter out diags
        coords = no_diags(coords)
    # print(coords)
    danger_zones = {}
    for line in coords:
        path = get_path(line)
        # print(line)
        # print(path)
        for p in path:
            if danger_zones.get(p):
                danger_zones[p] += 1
            else:
                danger_zones[p] = 1
    return len([v for v in danger_zones.values() if v >= thresh])


if __name__ == '__main__':
    FILE = 'input.txt'
    nbr_danger = compute_number_danger_zones(FILE, 2, allow_diags=False)
    print(f"There are {nbr_danger} danger zones")
    nbr_danger = compute_number_danger_zones(FILE, 2)
    print(f"There are {nbr_danger} danger zones when considering diagonals")
