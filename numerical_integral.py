import numpy as np

def integral(func: str, a: float, b: float, h: float, printing=False):

    """
    Approximates the area under a curve of a function

    parameters:
    func: given function
    a: lower bound
    b: upper bound
    h: partition
    printing: if True, prints the value of the area in the terminal
    """

    # Fixing possible errors
    
    swap = False
    if a > b:
        # If the boundries are switched, it swaps them and sets 'swap' to True
        a, b = b, a
        swap = True

    if a == b:
        print("The integal of", func, "is equal to 0, because the lower and the upper bound are equal")
        return 0
    
    if h > (b-a)/10:
        print("The partition is not small enough!")
        return
    
    # Defining the function as a string with eval()
    def f(x):
        f = eval(func)
        return f
    
    # Setting parameters
    T = 0.0
    x = np.arange(a, b, h)
    y = []
    
    # Giving the y values
    for i in range(len(x)):
        y = np.append(y, f(x[i]))

        # Analysing the domain
        if str(y[i]) == 'nan':
            print("The function is not interpreted on the given range!")
            return
    
    # Calculating area
    for i in range(len(y)):
        T += y[i]*h
    
    # Printing area
    if printing:
        print("The area of", func, "from", '.3g'%a, "to", '%.3g'%b, "equals to", '%.3g'%T)
    
    # If the boundries have been swapped, it returns the -1 times the area
    if swap:
        return -T
        
    return T

#example:
#integral("np.sin(x)", 0, np.pi, 0.01, printing=True)
