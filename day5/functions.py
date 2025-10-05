#declaration and return

#without function we have to do same operation by writing code everytime
a = 10
b = 6
gmean1 = (a*b)/(a+b)
print(gmean1)

#but with function we can reuse a code of block for a logic just by calling it rach time we need the same logic

#function declaration
def calculateGmean(a,b):
    mean = (a*b)/(a+b)
    return mean             #local variable mean is returned
gmean2 = calculateGmean(a,b) #function call
print(gmean2)

#here a and b are parameters
#and gmean2 is return value
