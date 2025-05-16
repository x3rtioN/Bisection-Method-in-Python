# 🧮 Bisection Method Root Finder

This Python script demonstrates a simple implementation of the **bisection method** to find the root of a nonlinear equation.

## 🔍 About

The goal is to find a root of the function:

```
f(x) = x³ - (x + 3)^(1/3) - 3
```

using the **bisection method**, a well-known numerical technique for solving nonlinear equations. The method repeatedly halves an interval and selects a subinterval in which the function changes sign, eventually converging to a root.

## 📌 Features

- Implements the bisection method with a customizable tolerance.
- Tracks and prints the number of iterations required to find the root.
- Raises an error if the initial interval does not bracket a root.

## 🧠 Function Definitions

```python
def f(x):
    return x**3 - (x + 3)**(1/3) - 3
```

Defines the function for which we want to find the root.

```python
def bisection_method(a, b, tol=1e-2):
    ...
```

Finds the root of `f(x)` within the interval `[a, b]` using a specified tolerance (default: `0.01`).

## ▶️ Example Run

```python
a, b = 1, 2
root, num_iterations = bisection_method(a, b)
print(f"Root: {root:.4f}, Iterations: {num_iterations}")
```

### Sample Output:
```
Root: 1.7803, Iterations: 6
```

## 🛠 Requirements

- Python 3.x

No additional libraries are required.

## 📄 License

This project is licensed under the MIT License.

---

Feel free to contribute or modify the function to try other root-finding techniques!
