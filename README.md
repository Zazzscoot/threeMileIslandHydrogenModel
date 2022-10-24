# threeMileIslandHydrogenModel
For MAT231

Algorithm Process
----------------------------------------------------
This algorithm uses the multi-step process outlined below

1. Select two values for tb and K. Construct the ambient temperature equation Ta using these values
2. Now for each RTD: 
  a. Select an optimal value for 𝛼 
  b. Use Euler’s Method to numerically approximate Ti with the given parameter values  
  c. Find the least squares value of the given data points on Ti
3. Sum up all the least squares values obtained from the 11 RTDs. This sum is called the least squares sum. Record sum value in a csv file.
Repeat all previous steps, with new values for tb and K. 

Challenges Faced
-----------------------------------------------------------
1. This algorithm was written completely without numpy or scipy. It would have been a lot easier if those libraries were used.
2. The formatting on MatPlotLib is sometimes very difficult to work with. It took some practice to master for sure.
3. The code took exceptionally long to run, because it involved several nested for loops (I think the speed was O(n^3), I will try to speed it up in a future revision)
