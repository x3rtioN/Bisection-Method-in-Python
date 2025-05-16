def f(x):
    return x**3 - (x + 3)**(1/3) - 3

def bisection_method(a, b, tol=1e-2):
    if f(a) * f(b) >= 0:
        raise ValueError("f(a) and f(b) must have opposite signs")
    
    iteration = 0
    while (b - a) / 2 > tol:
        midpoint = (a + b) / 2
        if f(midpoint) == 0:
            return midpoint, iteration
        elif f(a) * f(midpoint) < 0:
            b = midpoint
        else:
            a = midpoint
        iteration += 1
    
    return (a + b) / 2, iteration

a, b = 1, 2
root, num_iterations = bisection_method(a, b)
print(f"Root: {root:.4f}, Iterations: {num_iterations}")
