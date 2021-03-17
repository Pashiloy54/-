import sys


class Math:
    def __init__(self):

        self.first_num = float(input('Первое число: '))
        self.two_num = float(input('Второе число: '))

        self.answ = input('Знак: ')

        if self.answ == '+':
            self.result = self.first_num + self.two_num
        elif self.answ == '-':
            self.result = self.first_num - self.two_num
        elif self.answ == '/':
            self.result = self.first_num / self.two_num
        elif self.answ == '*':
            self.result = self.first_num * self.two_num
        else:
            print('ERROR!')
            sys.exit(0)

        print(self.result)

math = Math()
