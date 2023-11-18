import math

def calculate_Z(t, x):
    if t > 0:
        return (9 * math.pi * t + 10 * math.cos(x)) / (math.sqrt(t) - abs(math.sin(t))) * math.exp(x)
    else:
        return "t must be greater than 0 to calculate Z."

def f(x):
    if x >= 0:
        return 0.5 - 4/abs(x)
    else:
        return (math.sin(x)**2) / (x**2)

t_value = 1  
x_value = 2  

Z_value = calculate_Z(t_value, x_value)
f_x_value = f(x_value)

print(f"Z: {Z_value:.3f}")
print(f"f(x): {f_x_value:.3f}")
