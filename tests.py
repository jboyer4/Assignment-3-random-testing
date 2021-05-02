import unittest
import string
import random
from credit_card_validator import credit_card_validator


class TestCase(unittest.TestCase):
    pass


def build_test_func(expected, test_case, func_under_test, message):
    def test(self):
        result = func_under_test(test_case)
        self.assertEqual(expected, result, message.format(test_case, expected, result))
    return test


def generate_testcases(tests_to_generate=400000):
    for i in range(tests_to_generate):
        expected = True
        # Random length
        close_len = random.randint(14, 17)
        any_len = random.randint(0, 100)
        length = random.choice([close_len, any_len])
        # Get prefix type
        prefix_list = ['visa', 'mc1', 'mc2', 'amex', '']
        prefix = random.choice(prefix_list)
        prefix_value = ''

        # Generate prefix value
        if (prefix == 'visa'):
            prefix_value = test_visa()
        elif (prefix == 'mc1'):
            prefix_value = test_mc1()
        elif (prefix == 'mc2'):
            prefix_value = test_mc2()
        elif (prefix == 'amex'):
            prefix_value = test_amex()

        # Generate password
        cc = gen_cc(prefix_value, length)

        # Build test function
        message = 'Test case: {}, Expected: {}, Result: {}'
        new_test = build_test_func(expected, cc, credit_card_validator, message)
        print(length, prefix, cc)
        setattr(TestCase, 'test_{}'.format(cc), new_test)


# Test valid visa prefix or edge cases
def test_visa():
    options = ['3', '4', '4', '5']
    return random.choice(options)


def test_mc1():
    options = ['50', '51', '52', '53', '54', '55', '56']
    return random.choice(options)


def test_mc2():
    options = ['2220', '2221', '2222', '2719', '2720', '2721']
    return random.choice(options)


def test_amex():
    options = ['33', '34', '35', '36', '37']
    return random.choice(options)


def gen_cc(prefix, length):
    cc_number = prefix
    cc_number = cc_number + ''.join(random.choice(string.digits) for i in range(length - len(prefix)))
    return cc_number


if __name__ == '__main__':
    generate_testcases()
    unittest.main()
