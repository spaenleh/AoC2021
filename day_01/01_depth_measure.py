
def convert_val(v):
    return int(v.strip())


def read_measurements(file='input.txt'):
    measures = []
    with open(file, 'r', encoding='utf-8') as f:
        for val in f.readlines():
            val = convert_val(val)
            measures.append(val)
    return measures


def one_step_inc_count():
    inc_count = 0
    measures = read_measurements('input.txt')
    prev = measures[0]
    for val in measures[1:]:
        if val > prev:
            inc_count += 1
        prev = val
    return inc_count


def get_window_sum(arr, idx, window_size=3):
    return sum(arr[idx:idx+window_size])


def sliding_window_inc_count(window_size=3):
    inc_count = 0
    measures = read_measurements('input.txt')
    prev = get_window_sum(measures, 0, window_size)
    for i in range(1, len(measures)-window_size+1):
        val = get_window_sum(measures, i, window_size)
        if val > prev:
            inc_count += 1
        prev = val
    return inc_count


if __name__ == '__main__':
    print(f"Using the single measurements: {one_step_inc_count()}")
    print(f"Using a sliding window: {sliding_window_inc_count(3)}")
