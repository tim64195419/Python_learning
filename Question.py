# by 暴力法
# 公鸡5元一只 母鸡3元一只 小鸡1元三只
# 用100元买100只鸡 问公鸡/母鸡/小鸡各多少只

for x in range(20):
    for y in range(33):
        z = 100 - x - y
        if 5*x + 3*y + z // 3 == 100 and z % 3 == 0:

            print('公雞 %s 母雞 %s 小雞 %s ' % (x, y, z))

print('==='*20)

# by 暴力法
# A、B、C、D、E五人在某天夜里合伙捕鱼 最后疲惫不堪各自睡觉
# 第二天A第一个醒来 他将鱼分为5份 扔掉多余的1条 拿走自己的一份
# B第二个醒来 也将鱼分为5份 扔掉多余的1条 拿走自己的一份
# 然后C、D、E依次醒来也按同样的方式分鱼 问他们至少捕了多少条鱼

fish = 6
while True:
    total = fish
    enough = True
    for _ in range(5):
        if (total - 1) % 5 == 0:
            total = (total - 1) // 5 * 4

        else:
            enough = False
            break
    if enough:
        print('至少需要補 %d 條魚' % fish)
        break
    fish += 5

print('==='*20)



# 貪婪法
# 假设小偷有一个背包，最多能装20公斤赃物，他闯入一户人家，发现如下表所示的物品。很显然，他不能把所有物品都装进背包，所以必须确定拿走哪些物品，留下哪些物品。

'''
# 物品
class Thing(object):
    def __init__(self,name,price,weight):
        self.name=name
        self.price=price
        self.weight=weight

    @property
    def value(self):
        # 價格重量比
        return self.price/self.weight


def input_thing():
    # 輸入物品訊息
    name_str,price_str,weight_str = input().split()
    return name_str,int(price_str),int(weight_str)


def main():
    """主函数"""
    max_weight, num_of_things = map(int, input().split())
    all_things = []
    for _ in range(num_of_things):
        all_things.append(Thing(*input_thing()))
    all_things.sort(key=lambda x: x.value, reverse=True)
    total_weight = 0
    total_price = 0
    for thing in all_things:
        if total_weight + thing.weight <= max_weight:
            print(f'小偷拿走了{thing.name}')
            total_weight += thing.weight
            total_price += thing.price
    print(f'总价值: {total_price}美元')


if __name__ == '__main__':
    main()

'''

"""
快速排序 - 选择枢轴对元素进行划分，左边都比枢轴小右边都比枢轴大
"""
def quick_sort(origin_items, comp=lambda x, y: x <= y):
    items = origin_items[:]
    _quick_sort(items, 0, len(items) - 1, comp)
    return items


def _quick_sort(items, start, end, comp):
    if start < end:
        pos = _partition(items, start, end, comp)
        _quick_sort(items, start, pos - 1, comp)
        _quick_sort(items, pos + 1, end, comp)


def _partition(items, start, end, comp):
    pivot = items[end]
    i = start - 1
    for j in range(start, end):
        if comp(items[j], pivot):
            i += 1
            items[i], items[j] = items[j], items[i]
    items[i + 1], items[end] = items[end], items[i + 1]
    return i + 1


'''
# 递归回溯法：叫称为试探法，按选优条件向前搜索，当搜索到某一步，发现原先选择并不优或达不到目标时，就退回一步重新选择，比较经典的问题包括骑士巡逻、八皇后和迷宫寻路等。

import sys
import time

SIZE = 5
total = 0


def print_board(board):
    for row in board:
        for col in row:
            print(str(col).center(4), end='')
        print()


def patrol(board, row, col, step=1):
    if row >= 0 and row < SIZE and \
        col >= 0 and col < SIZE and \
        board[row][col] == 0:
        board[row][col] = step
        if step == SIZE * SIZE:
            global total
            total += 1
            print(f'第{total}种走法: ')
            print_board(board)
        patrol(board, row - 2, col - 1, step + 1)
        patrol(board, row - 1, col - 2, step + 1)
        patrol(board, row + 1, col - 2, step + 1)
        patrol(board, row + 2, col - 1, step + 1)
        patrol(board, row + 2, col + 1, step + 1)
        patrol(board, row + 1, col + 2, step + 1)
        patrol(board, row - 1, col + 2, step + 1)
        patrol(board, row - 2, col + 1, step + 1)
        board[row][col] = 0


def main():
    board = [[0] * SIZE for _ in range(SIZE)]
    patrol(board, SIZE - 1, SIZE - 1)


if __name__ == '__main__':
    main()

'''



"""
动态规划 - 适用于有重叠子问题和最优子结构性质的问题
使用动态规划方法所耗时间往往远少于朴素解法(用空间换取时间)
"""


def fib(num, temp={}):
    """用递归计算Fibonacci数"""
    if num in (1, 2):
        return 1
    try:
        return temp[num]
    except KeyError:
        temp[num] = fib(num - 1) + fib(num - 2)

        return temp[num]

print('fib:12 = %d' % fib(12))






# dp動態規劃例子：子列表元素之和的最大值

