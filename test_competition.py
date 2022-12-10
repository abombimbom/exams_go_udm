# -*- coding: utf-8 -*-

if __name__ == '__main__':
    print(
        [(not bool(i%3))*'Fizz' + (not bool(i%5))*'Buzz'  if not bool(i%3*i%5) else i for i in range(1,101)]
    )