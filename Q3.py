import unittest

import sympy as sym

x = sym.Symbol('x')


def find_root(p, a, b):
    # Derivative - Part Of NR
    p_prime = sym.diff(p)
    # Accuracy - Epsilon
    acc = 10 ** -9
    # Initial "Guess/Estimate" that is The Minimum in The [A,B] range
    xi = a
    # Delta As Infinity to Begin|| The distance may be far enough to count.
    delta = sym.oo
    # Other Wise the algorithm has found an approximate solution and returns xn.
    while abs(delta) > acc:
        # Delta is Dependant on Xi, At first iteration, Delta will be our f/f' calculated at xi
        # Like in Calculus im Looking for the Convergence, hence the while will stop when close enough to epsilon
        delta = (p / p_prime).subs(x, xi).evalf()
        xi -= delta  # Raphson Iteration
    if a <= xi <= b:
        return xi
    else:
        return "No Root in Given range"


class find_rootTestCase(unittest.TestCase):
    def test_numbers(self):
        # Test that are Correct - Example of Usage
        self.assertAlmostEqual(find_root(x ** 2 - 8, 1, 3), 2.82842712, 6, "OK")
        self.assertAlmostEqual(find_root(x ** 2 - 4, 1, 3), 2.0, 6, "OK")
        self.assertAlmostEqual(find_root(x ** 2 - 12, 1, 4), 3.46410161513775, 7, "OK")
        # Bad Tests - When Root is not in Range
        self.assertEqual(find_root(x ** 2 - 12, 1, 3), "No Root in Given range")
        self.assertEqual(find_root(x ** 2 - 20, 1, 3), "No Root in Given range")


if __name__ == "__main__":
    # unittest.main()

    print(find_root(x ** 2 - 4, 1, 5))
