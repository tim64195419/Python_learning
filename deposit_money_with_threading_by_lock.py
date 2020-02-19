from time import sleep
from threading import Thread,Lock

class Account(object):
    def __init__(self):
        self._balance = 0
        self._lock= Lock()
    def deposit(self,money):
        self._lock.acquire()
        '''硬體指令 semaphore'''
        try:
            new_balance = self._balance + money
            sleep(0.01)
            self._balance = new_balance
        finally:
            self._lock.release()
            '''硬體指令 semaphore'''

    @property
    def balance(self):
        return self._balance

class AddMoneyThread(Thread):
    def __init__(self,account,money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self):
        self._account.deposit(self._money)

def main():
    account = Account()
    threads = []
    for _ in range(100):
        t = AddMoneyThread(account,1)
        threads.append(t)
        # print(threads)
        t.start()

    for t in threads:
        t.join()
    print('帳號餘額： $%d ' %account.balance )

if __name__ == '__main__':
    main()