"""
以下情况需要使用多线程：

程序需要维护许多共享的状态（尤其是可变状态），Python中的列表、字典、集合都是线程安全的，所以使用线程而不是进程维护共享状态的代价相对较小。
程序会花费大量时间在I/O操作上，没有太多并行计算的需求且不需占用太多的内存。
以下情况需要使用多进程：

程序执行计算密集型任务（如：字节码操作、数据处理、科学计算）。
程序的输入可以并行的分成块，并且可以将运算结果合并。
程序在内存使用方面没有任何限制且不强依赖于I/O操作（如：读写文件、套接字等）。
"""
import concurrent.futures
import math

PRIMES = [
    1116281,
    1297337,
    104395303,
    472882027,
    533000389,
    817504243,
    982451653,
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419
] * 5


def is_prime(n):
    """判断素数"""
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


def main():
    """主函数"""
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print('%d is prime: %s' % (number, prime))


if __name__ == '__main__':
    main()

# import time
# import threading
#
# from concurrent.futures import ThreadPoolExecutor
#
#
# class Account(object):
#     """银行账户"""
#
#     def __init__(self):
#         self.balance = 0.0
#         self.lock = threading.Lock()
#
#     def deposit(self, money):
#         # 通过锁保护临界资源
#         with self.lock:
#             new_balance = self.balance + money
#             time.sleep(0.001)
#             self.balance = new_balance
#
#
# class AddMoneyThread(threading.Thread):
#     """自定义线程类"""
#
#     def __init__(self, account, money):
#         self.account = account
#         self.money = money
#         # 自定义线程的初始化方法中必须调用父类的初始化方法
#         super().__init__()
#
#     def run(self):
#         # 线程启动之后要执行的操作
#         self.account.deposit(self.money)
#
# def main():
#     """主函数"""
#     account = Account()
#     # 创建线程池
#     pool = ThreadPoolExecutor(max_workers=10)
#     futures = []
#     for _ in range(100):
#         # 创建线程的第1种方式
#         # threading.Thread(
#         #     target=account.deposit, args=(1, )
#         # ).start()
#         # 创建线程的第2种方式
#         # AddMoneyThread(account, 1).start()
#         # 创建线程的第3种方式
#         # 调用线程池中的线程来执行特定的任务
#         future = pool.submit(account.deposit, 1)
#         futures.append(future)
#     # 关闭线程池
#     pool.shutdown()
#     for future in futures:
#         future.result()
#     print(account.balance)
#
#
# if __name__ == '__main__':
#     main()

# from random import randint
# from threading import Thread
# from time import time, sleep
#
#
# def download(filename):
#     print('开始下载%s...' % filename)
#     time_to_download = randint(5, 10)
#     sleep(time_to_download)
#     print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))
#
#
# def main():
#     start = time()
#     t1 = Thread(target=download, args=('Python从入门到住院.pdf',))
#     t1.start()
#     t2 = Thread(target=download, args=('Peking Hot.avi',))
#     t2.start()
#     t1.join()
#     t2.join()
#     end = time()
#     print('总共耗费了%.3f秒' % (end - start))
#
#
# if __name__ == '__main__':
#     main()
#
#
