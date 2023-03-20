from math import sqrt
import matplotlib.pyplot as plt
import numpy as np

print("ax^2+bx+c=0")
a = float(input("Enter coefficient of a: "))
b = float(input("Enter coefficient of b: "))
c = float(input("Enter coefficient of c: "))

#make title of graph look better, if negative in values then it wont display + along with the - 
#too much effort for cleaner look? Nope. Is there a more efficient way? Probably
def title():
        if b < 1 and c < 1 :
                return f"Graph of {a}x^2{b}x{c}=0"
        elif c < 1:
                return f"Graph of {a}x^2+{b}x{c}=0"
        elif b < 1:
                return f"Graph of {a}x^2{b}x+{c}=0"
        else:
                return f"Graph of {a}x^2+{b}x+{c}=0"
        
        
#catch error if roots dont exist (-4ac > b^2) resulting in negative root (imaginary number)
try:
        #quadratic formula to get both values
        value1 = (-(b)+(sqrt((b**2)-4*a*c)))/(2*a)
        value2 = (-(b)-(sqrt((b**2)-4*a*c)))/(2*a)
except:
        value1 = "Doesn't exist"
        value2 = "Doesn't exist"

#cool way i figured out to get turning point coords, completing square and getting values in compact equations
tPointx = -(b/a)/2
tPointy = (-((b/a)/2)**2+(c/a))*a

#all hail f strings
print(f"x value 1 = {value1}")
print(f"x value 2 = {value2}")
print(f"y intercept = {c}")
print(f"Coordinates of turning point are ({tPointx}, {tPointy})")

ans = input("Would you like us to plot a graph of your equation? y/n: ")
if ans == "y" or "Y":
    #construct graph
    x = np.linspace(-10, 10, 1000)
    y = a*(x**2) + b*x + c  
    fig, ax = plt.subplots()
    #axis labels and title
    ax.set_title(title())
    plt.xlabel('x')
    plt.ylabel('y')
    #axis lines
    plt.axhline(y=0, color='r', linestyle='--')
    plt.axvline(x=0, color='r', linestyle='--')
    #plot and show final graph
    ax.plot(x, y)
    plt.show()
else:
    print("See ya next time then!")
