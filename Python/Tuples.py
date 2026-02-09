# https://www.hackerrank.com/challenges/python-tuples/problem

#On python 2 because python 3 and pypy3 are bugged, 
if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    print(hash(tuple(integer_list)))
