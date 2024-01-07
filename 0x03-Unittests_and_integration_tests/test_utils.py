#!/usr/bin/env python3
""" Test_SUITE_Unittest_module_Task """

from unittest import TestCase, mock
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(TestCase):
    """ Class_for_testing_Nested_Map_function """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, map, path, expected_output):
        """ Test_method_return_output """
        real_output = access_nested_map(map, path)
        self.assertEqual(real_output, expected_output)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, map, path, wrong_output):
        """ Test_method_raises_correct_exception """
        with self.assertRaises(KeyError) as e:
            access_nested_map(map, path)
            self.assertEqual(wrong_output, e.exception)


class TestGetJson(TestCase):
    """ Class_for_testing_get_json_function """
    # order of args: test_url, test_payload
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """ Test_method_returns_correct_output """
        # set mock response to have return value of test payload
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        # function calls requests.get, need patch to get mock return value
        with patch('requests.get', return_value=mock_response):
            real_response = get_json(test_url)
            self.assertEqual(real_response, test_payload)
            # check that mocked method called once per input
            mock_response.json.assert_called_once()


class TestMemoize(TestCase):
    """ Class_for_testing_memoization """

    def test_memoize(self):
        """ Tests_memoize_function """

        class TestClass:
            """ Test class """

            def a_method(self):
                """ Method_to_always_return_42 """
                return 42

            @memoize
            def a_property(self):
                """ Returns_memoized_property """
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as patched:
            test_class = TestClass()
            real_return = test_class.a_property
            real_return = test_class.a_property

            self.assertEqual(real_return, 42)
            patched.assert_called_once()
