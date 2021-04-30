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


def generate_testcases(tests_to_generate=10000):
    for i in range(tests_to_generate):
        expected = True
        # Random length
        length = random.randint(13, 17)
        # Generate password
        cc = gen_cc('', length)
        # Get prefix type
        prefix_list = ['visa', 'mc1', 'mc2', 'amex']
        prefix = random.choice(prefix_list)
        # Generate prefix value
        if (prefix == 'visa'):
            pass
            # test_visa()
        elif (prefix == 'mc1'):
            pass
            # test_mc1()
        elif (prefix == 'mc2'):
            pass
            # test_mc2()
        elif (prefix == 'amex'):
            pass
            # test_amex()
        # Build test function
        message = 'Test case: {}, Expected: {}, Result: {}'
        new_test = build_test_func(expected, cc, credit_card_validator, message)
        setattr(TestCase, 'test_{}'.format(cc), new_test)


def gen_cc(prefix, length):
    cc_number = prefix
    cc_number = cc_number + ''.join(random.choice(string.digits) for i in range(length - len(prefix)))
    return cc_number

if __name__ == '__main__':
    generate_testcases()
    unittest.main()
