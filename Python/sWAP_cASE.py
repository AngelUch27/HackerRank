# https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true
def swap_case(s):
    for i in range(len(s)):
        return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
