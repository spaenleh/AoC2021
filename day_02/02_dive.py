FORWARD = 'forward'
DOWN = 'down'
UP = 'up'


def get_command(v):
    cmd, val = v.split()
    val = int(val)
    return cmd, val


def get_final_position(file):
    horizontal_pos = 0
    depth = 0
    with open(file, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            cmd, val = get_command(line)
            if cmd == FORWARD:
                horizontal_pos += val
            elif cmd == DOWN:
                depth += val
            elif cmd == UP:
                depth -= val
            else:
                print(f'unrecognized command {cmd}')
    return horizontal_pos, depth


def get_final_position_complex(file):
    h_pos = 0
    depth = 0
    aim = 0
    with open(file, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            cmd, val = get_command(line)
            if cmd == FORWARD:
                h_pos += val
                depth += aim * val
            elif cmd == DOWN:
                aim += val
            elif cmd == UP:
                aim -= val
            else:
                print(f'unrecognized command {cmd}')
    return h_pos, depth


if __name__ == '__main__':
    FILE = 'input.txt'
    final_h_pos, final_depth = get_final_position(FILE)
    print(f"Final pos is [{final_h_pos}, {final_depth}] and product is {final_h_pos * final_depth}")
    final_h_pos, final_depth = get_final_position_complex(FILE)
    print(f"Final pos is [{final_h_pos}, {final_depth}] and product is {final_h_pos * final_depth}")
