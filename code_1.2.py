import math

# Define the function to calculate Z without numpy
def calculate_Z(t, x):
    if t > 0:
        return (9 * math.pi * t + 10 * math.cos(x)) / (math.sqrt(t) - abs(math.sin(t))) * math.exp(x)
    else:
        return "t must be greater than 0 to calculate Z."

# Define the piecewise function for f(x) without numpy
def f(x):
    if x >= 0:
        return 0.5 - 4/abs(x)
    else:
        return (math.sin(x)**2) / (x**2)

# Example usage
t_value = 1  # Replace with user input
x_value = 2  # Replace with user input

Z_value = calculate_Z(t_value, x_value)
f_x_value = f(x_value)

print(f"Z: {Z_value:.3f}")
print(f"f(x): {f_x_value:.3f}")
