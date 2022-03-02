import unittest


def f(x: int, y: float, z):
    return x + y + z


def safecall(funcarg, **kwargs):
    # Try and Catch Will Eliminate me having to take care of other cases
    try:
        annotdict = funcarg.__annotations__
        # Iterate over Arguments
        for key in kwargs:
            # Check if Argument is not a argument with annotate and belongs - continue to next iteration
            if key not in annotdict:
                if key in funcarg.__code__.co_varnames:
                    continue
                    # If types Are same then Obvious continue Here, But if not the same - Raise Error
            if type(kwargs[key]) is annotdict[key]:
                continue
            else:
                raise TypeError('Error: Given Type"' + str(type(kwargs[key])) + '" Needed ' + str(annotdict[key]))
        # Proper way In python - Else Return None
        return funcarg(**kwargs)
    except:
        return "Error Happened"


class Testing(unittest.TestCase):

    def test_safecall(self):
        # Regular Call
        self.assertEqual(safecall(f, x=8, y=2.0, z=2), 12.0)
        self.assertEqual(safecall(f, x=2, y=2.5, z=2), 6.5)
        # Annotate Abuse - Int is Decimal
        self.assertEqual(safecall(f, x=2.2, y=2.5, z=2), "Error Happened")
        self.assertEqual(safecall(f, x=2.2, y=2.5, z="test"), "Error Happened")
        # To Many Arguents
        self.assertEqual(safecall(f, x=2.2, y=2.5, z=2, e=9), "Error Happened")
        self.assertEqual(safecall(f, x=2.2, y=2.5, z=2, e=9, t=3), "Error Happened")
        # Lesser Arguments
        self.assertEqual(safecall(f, x=2, y=2.5), "Error Happened")
        self.assertEqual(safecall(f, x=2), "Error Happened")
        self.assertEqual(safecall(f,), "Error Happened")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Hello")
