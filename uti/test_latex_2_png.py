import numpy as np
import matplotlib.mathtext as mathtext
import matplotlib.pyplot as plt
import matplotlib
import re
matplotlib.rc('image', origin='upper')
matplotlib.rcParams['text.latex.preamble']=[r"\usepackage{amsmath}"]
matplotlib.rc('text', usetex=True)

from latexmath2png import math2png

'''
parser = mathtext.MathTextParser("Bitmap")


#latextext = latextext.replace(r'\',r'\\')
print latextext
                  
parser.to_png('test2.png',r'$\alpha$' r'$\\\\$' r'$\beta$'
              , color='k', fontsize=14, dpi=100)

print 1
'''

latextext = r"""\[\left\{ \begin{array}{l}
{y_1}\left( {x = d} \right) = {y_3}\left( {x = d} \right)\\
\frac{{d{y_1}}}{{dx}}(x = d) = \frac{{d{y_3}}}{{dx}}(x = d)\\
\frac{{d{y_1}}}{{dx}}(x = 0) = 0\\
 - EI\frac{{{d^3}{y_1}}}{{d{x^3}}}(x = 0) + \frac{P}{2} = 0
\end{array} \right.\]"""
math2png([latextext],'test')