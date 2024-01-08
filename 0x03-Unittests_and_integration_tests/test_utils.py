#!/usr/bin/env python3

""" Parameterize a unit test
"""

import unittest
from unittest.mock import patch, mock
from parameterized import parameterized

from utils import (
    access_nested_map,
    get_json,
    memoize
)


class TestAccessNestedMap(unittest.TestCase):
    """ class TestAccessNestedMap
    """

    # I: Testing access_nested_map
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, mapping, path, rslt):
        """ test function access_nested_map for correct output
        """
        self.assertEqual(access_nested_map(mapping, path), rslt)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self, mapping, path, rslt):
        """ test function access_nested_map for KeyError handling
        """
        with self.assertRaises(rslt):
            access_nested_map(mapping, path)


class TestGetJson(unittest.TestCase):
    """ class TestGetJson
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """ Method to test that utils.get_json returns the expected result
        """
        # Set up the mock response
        mock_response = mock_get.return_value
        mock_response.json.return_value = test_payload

        # Call the function under test
        result = get_json(test_url)

        # Assert that requests.get was called exactly once with the test_url
        mock_get.assert_called_once_with(test_url)

        # Assert that the result of get_json is equal to test_payload
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """ class TestGetJson
    """

    def test_memoize(self):
        """ Method to test that utils.memoize returns the expected result
        """
        class TestClass:
            def a_method(self):
                """ method """
                return 42

            @memoize
            def a_property(self):
                """ property """
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mockObj:
            testClass = TestClass()
            testClass.a_property
            testClass.a_property
            mockObj.assert_called_once
