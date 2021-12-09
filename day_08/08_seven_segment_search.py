from collections import Counter

SIMPLE_DIGITS_LEN = [2, 3, 4, 7]


def sort_strings(sample):
    return [''.join(sorted(bit)) for bit in sample.split()]


def read_file(file):
    with open(file, 'r', encoding='utf-8') as f:
        samples = []
        output_vals = []
        for line in f.readlines():
            sample, end_bit = line.split('|')
            samples.append(sort_strings(sample))
            output_vals.append(sort_strings(end_bit))
        return samples, output_vals


def count_simple_digits(file):
    _, output_values = read_file(file)
    output_values = [v for vals in output_values for v in vals]
    len_vals = [len(s) for s in output_values]
    counter = Counter(len_vals)
    total = sum([counter.get(k) if counter.get(k) else 0 for k in SIMPLE_DIGITS_LEN])
    return total


def compute_output(out_vals, mapping):
    digits = []
    for out in out_vals:
        d = str(mapping[out])
        digits.append(d)
    return int(''.join(digits))


def get_digit_mapping(s):
    s = list(set(s))
    code_lengths = [len(v) for v in s]
    # given by their length
    code_1 = s[code_lengths.index(2)]
    code_7 = s[code_lengths.index(3)]
    code_4 = s[code_lengths.index(4)]
    code_8 = s[code_lengths.index(7)]

    # get the numbers with length 5 -> 2, 3, 5
    code_len_5 = [s[i] for i, code_len in enumerate(code_lengths) if code_len == 5]

    # get the numbers with length 6 -> 0, 6, 9
    code_len_6 = [s[i] for i, code_len in enumerate(code_lengths) if code_len == 6]

    # 3 is the only digit of length 5 that includes both letters from 1
    code_3 = [c for c in code_len_5 if all([digit in c for digit in code_1])][0]
    code_len_5.remove(code_3)

    # 6 if the only digit of length 6 that does not include both letters from 1
    code_6 = [c for c in code_len_6 if not all([digit in c for digit in code_1])][0]
    code_len_6.remove(code_6)

    # when we compute the difference from 2 and 5 with 6 we get 1 for 5 and 2 for 6
    diff_6_to_len5 = [len(set(code_6).difference(set(c))) for c in code_len_5]
    code_5 = code_len_5[diff_6_to_len5.index(1)]
    code_2 = code_len_5[diff_6_to_len5.index(2)]

    # when we compute the overlap of letters from 9 and 0 to 4 we get 4 for 9 and 3 for 0
    super_4_to_len6 = [len(set(c).intersection(set(code_4))) for c in code_len_6]
    code_9 = code_len_6[super_4_to_len6.index(4)]
    code_0 = code_len_6[super_4_to_len6.index(3)]

    # assigning
    mapping = {
        code_0: 0,
        code_1: 1,
        code_2: 2,
        code_3: 3,
        code_4: 4,
        code_5: 5,
        code_6: 6,
        code_7: 7,
        code_8: 8,
        code_9: 9,
    }
    return mapping


def compute_sum_of_outputs(file):
    samples, outputs = read_file(file)
    output_values = []
    for s, o in zip(samples, outputs):
        mapping = get_digit_mapping(s)
        number = compute_output(o, mapping)
        output_values.append(number)
    return sum(output_values)


if __name__ == '__main__':
    FILE = 'input.txt'
    count = count_simple_digits(FILE)
    print(f"The count is {count}")
    sum_outputs = compute_sum_of_outputs(FILE)
    print(f"The sum of the outputs is {sum_outputs}")
