import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_range(self) : 
        ll, med, uu = 100*[0], 100*[0], 100*[0]
        for i in range(100) : 
            ll[i], med[i], uu[i] = myerrors(10,100)
            self.assertTrue( ll[i]<med[i] and med[i]<uu[i], "The median does not lie between the upper and lower percentile" )
  
        low, medi, upp = myerrors(10,100)
        self.assertTrue( low>=np.percentile(ll,5) and low<=np.percentile(ll,95), "the lower percentile doesn't appear to be sampling from the correct distribution" )
        self.assertTrue( medi>=np.percentile(med,5) and medi<=np.percentile(med,95), "the median doesn't appear to be sampling from the correct distribution" )
        self.assertTrue( upp>=np.percentile(uu,5) and upp<=np.percentile(uu,95), ""the upper percentile doesn't appear to be sampling from the correct distribution" )
