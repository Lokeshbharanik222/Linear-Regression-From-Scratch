x = [20,22,24,26,28,30]         #Temperature in C
y = [100,110,120,130,140,150]   #Eletricity Usage in kWH
n = len(x)                      # n value
fx = 32                         # x value for needs to find y value
def E(a):                       # Summation funtion to add list items
    k = 0
    for i in a:
        k += i
    return k

Ex = E(x)                       # Summation of x
Ey = E(y)                       # Summation of y

x2 = [i**2 for i in x]          # list of square of x values
y2 = [i**2 for i in y]          # list of square of y values

Ex2 = E(x2)                     # Summation of x^2 values
Ey2 = E(y2)                     # Summation of y^2 values

xy = []                         # Empty list to product values of x & y

for i in range(n):            # loop to product both lists
    xy.append(x[i]*y[i])

Exy = E(xy)                     # Summation of xy (product term)

s = ((Ex*Ey)-(n*Exy))/(Ex**2-(n*Ex2)) #finding slope for linear regression
c = (Ey - (s*Ex))/n             #finding intercept for linear regression

fy = (s*fx) + c                 #finding y value for given x value
print("For ",fx,"°C, the Electricity consumption is ",fy,"kWH") #final prediction
