# coding: utf-8

import os
import time


def main():
    """
    PDCAを回す
    """

    # PDCAの辺の長さ（平日は5日なので5固定）
    SIDE_LENGTH = 5
    base = make_pdca_base(SIDE_LENGTH)

    # PDCAを回す時にはバッファを持たせよう
    buf = [' '] * (SIDE_LENGTH-2)
    pdca = ['P'] + buf + ['D'] + buf + ['C'] + buf + ['A'] + buf

    # PDCAを回し続ける
    while True:
        # 前回のPDCAをクリア
        os.system('clear')

        # PDCAを回す
        for i in range(SIDE_LENGTH):
            print(base[i].format(pdca, ' '))

        # 次のPDCAの準備をしつつ休憩を取る
        pdca = pdca[1:] + [pdca[0]]
        time.sleep(0.1)


def make_pdca_base(side_length):
    """
    PDCAを回すための土台作り
    """

    bases = []
    for i in range(side_length):
        if i == 0:
            l = [str(x) for x in range(side_length)]
            base = '{0[' + ']}{0['.join(l) + ']}'
        elif i == side_length - 1:
            l = [str((side_length-1)*3 - x) for x in range(side_length)]
            base = '{0[' + ']}{0['.join(l) + ']}'
        else:
            base = '{0[' + str((side_length-1)*4-i) + ']}' \
                   + '{1}' * (side_length-2) \
                   + '{0[' + str((side_length-1)+i) + ']}'

        bases.append(base)

    return bases


if __name__ == '__main__':
    main()
