import unittest
import scipy.stats as st
import scipy.special as sp
from main import *

class UnitTests(unittest.TestCase) :
    def test_xplot(self) : 
        fighand = plt.gca()
        for i in range(noutcomes) :
            x, y = fighand.patches[i].get_xy() 
            self.assertTrue( np.fabs(x+0.5*fighand.patches[i].get_width()-kparam-i)<1e-7, "the x-coordinates of the bars in your histogram are incorrect" )
  
    def test_normalisation(self) :
        ssum = 0.
        fighand=plt.gca()
        for i in range(noutcomes) : ssum = ssum + fighand.patches[i].get_height()
        self.assertTrue( np.fabs(ssum - 1.)<1e-7, "your histogram has not been normalised" )

   def test_plot(self) : 
       fighand=plt.gca()
       for i in range(noutcomes) :
           pval = sp.binom( i+kparam-1, kparam-1  )*pow(prob,kparam)*pow( 1-prob, i ) 
           bar = np.sqrt( pval*(1-pval)  )*st.norm.ppf( (0.99 + 1) / 2 )
           self.assertTrue( np.fabs( fighand.patches[i].get_height() - pval )<bar, "the heights of the bars in your historam appear to be incorrect" )
