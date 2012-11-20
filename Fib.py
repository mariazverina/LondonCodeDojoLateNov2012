'''
Created on Nov 19, 2012

@author: mariaz
'''
import unittest
import bisect

class FibGen(object):
    #----------- basic implementation -----

    def __init__(self, max_num):
        self.fib_seq = [1,2]    # boot strap the sequence
        while self.fib_seq[-1] < max_num:
            self.fib_seq.append(self.fib_seq[-1] + self.fib_seq[-2])
        self.cache = {}
    
    def biggest_sub_number(self, num):
        return [x for x in self.fib_seq if x <= num][-1]

    def zeckendorf(self, num):
        if num <= 1:
            return num
        max_addend = self.biggest_sub_number(num)
        position = self.fib_seq.index(max_addend)
        return 10 ** position + self.zeckendorf(num - max_addend)


    #----------- end basic implementation -----
    
    
    def fast_zeckendorf(self, num):
        if num <= 1:
            return num
        if num in self.cache:
            return self.cache[num]

        position = bisect.bisect_right(self.fib_seq, num) - 1
        self.cache[num] = 10 ** position + self.fast_zeckendorf(num - self.fib_seq[position])

        return self.cache[num]
        

class Test(unittest.TestCase):
    def testThat7HasBiggestAddend5(self):
        fg = FibGen(50)
        self.assertEquals(fg.biggest_sub_number(7), 5)
        
    def testThat1HasBiggestAddend1(self):
        fg = FibGen(50)
        self.assertEquals(fg.biggest_sub_number(1), 1)

    def testZeckendorfOne(self):
        fg = FibGen(50)
        self.assertEqual(fg.zeckendorf(1), 1)

    def testZeckendorfFive(self):
        fg = FibGen(50)
        self.assertEqual(fg.zeckendorf(5), 1000)

    def testZeckendorfSix(self):
        fg = FibGen(50)
        self.assertEqual(fg.zeckendorf(6), 1001)
        
    def testZeckendorf17(self):
        fg = FibGen(50)
        self.assertEqual(fg.zeckendorf(17), 100101)
        
    def testFirst10000(self):
        fg = FibGen(10001)
        for i in range(10001):
            f = fg.fast_zeckendorf(i)
#            print i,f

    def testThatZegendorfWasAGenius(self):
        fg = FibGen(1000001)
        for i in range(1000001):
            f = fg.fast_zeckendorf(i)
            self.assertFalse("11" in str(f))
        
        
        
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
