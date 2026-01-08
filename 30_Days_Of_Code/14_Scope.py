class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0
    # https://www.hackerrank.com/challenges/30-scope/problem?isFullScreen=true
	# Add your code here
    def computeDifference(self):
        maximo = 0
        absoluto =0
        for i in range(len(self.__elements)-1):
            for j in range(i+ 1, len(self.__elements)):
                absoluto = abs(self.__elements[i] - self.__elements[j]) 
                if absoluto > maximo:
                    maximo = absoluto
        self.maximumDifference = maximo
# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
