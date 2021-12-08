import numpy as np


def read_file(file):
    with open(file, 'r', encoding='utf-8') as f:
        seq = [int(v) for v in f.readline().split(',')]
        boards = []
        board = []
        for line in f.readlines():
            if line.strip() == '':
                continue
            else:
                board.append([int(v) for v in line.split()])
            if len(board) == 5:
                boards.append(board)
                board = []
        return seq, np.array(boards)


def compute_points(idx, boards, marked, num):
    board = boards[idx, :, :]
    pts = board[marked[idx, :, :] == False].sum() * num
    return pts


def compute_winning_board(file, last=False):
    seq, boards = read_file(file)
    marked = np.zeros_like(boards)
    for num in seq:
        # print(boards)
        # mark boards
        marked[boards == num] = True
        # check if one is winning
        for ax in [1, 2]:
            check = marked.mean(axis=ax)
            win_pos = np.where(check == 1)[0]
            if len(win_pos):
                idx = win_pos[0]
                pts = compute_points(idx, boards, marked, num)
                if last:
                    boards = np.delete(boards, idx, axis=0)
                    marked = np.delete(marked, idx, axis=0)
                    # print(boards.shape)
                    if boards.shape[0] == 1:
                        last = False
                        break
                else:
                    return pts


if __name__ == '__main__':
    FILE = 'input.txt'
    points = compute_winning_board(FILE)
    print(f"You win with {points}")
    points = compute_winning_board(FILE, last=True)
    print(f"You loose with {points}")
