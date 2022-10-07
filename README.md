# threeMileIslandHydrogenModel
For MAT231
########################################################################################
This algorithm uses the multi-step process outlined below

Select two values for tb and K. Construct the ambient temperature equation Ta using these values

Now for each RTD:
  
  Select an optimal value for 𝛼
  
  Use Euler’s Method to numerically approximate Ti with the given parameter values
  
  Find the least squares value of the given data points on Ti

Sum up all the least squares values obtained from the 11 RTDs. This sum is called the least squares sum. Record sum value in a csv file.

Repeat all previous steps, with new values for tb and K. 
#########################################################################################
Go to plotter.py. They have specific values of the parameters hardcoded in it.
#########################################################################################
Go to multitester.py. The testing range is also hardcoded.
#########################################################################################
Sorry for the hardcoding and the lack of comments...
