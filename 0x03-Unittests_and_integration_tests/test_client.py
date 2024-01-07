#!/usr/bin/env python3

"""
Parameterize and patch as decorators
"""

import unittest
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized

from client import *


class TestGithubOrgClient(unittest.TestCase):
    """ class TestGithubOrgClient(unittest.TestCase)
    """

    @parameterized.expand([
        ('google',),  # Test case with organization name 'google'
        ('abc',),
    ])
    @patch('client.get_json', return_value={'payload': True})
    def test_org(self, test_case, mock_get_json):
        """ Test that GithubOrgClient.org returns the correct value
        """
        # Create an instance of GithubOrgClient with the provided
        #  organization name
        test_org = GithubOrgClient(test_case)

        # Call the org method to retrieve the result
        result = test_org.org

        # Assert that the result is equal to the expected return
        #  value from the patch
        self.assertEqual(result, mock_get_json.return_value)

        # Assert that get_json was called exactly once
        mock_get_json.assert_called_once()

    @patch.object(GithubOrgClient, "org", new_callable=PropertyMock,
                  return_value={"repos_url": "holberton"})
    def test_public_repos_url(self, mock_org):
        """ Test _public_repos_url property
        """

        # Create an instance of GithubOrgClient
        test_client = GithubOrgClient("holberton")

        # Access the _public_repos_url property
        test_return = test_client._public_repos_url

        # Assert that the org property was accessed exactly once
        mock_org.assert_called_once_with()

        # Assert that the result is equal to the expected
        #  repos_url from the mocked org property
        self.assertEqual(test_return, mock_org.return_value.get("repos_url"))

    @patch.object(GithubOrgClient, "org", new_callable=PropertyMock,
                  return_value={"repos_url": "holberton"})
    def test_public_repos(self, mock_org):
        """Test _public_repos_url property"""

        # Create an instance of GithubOrgClient
        test_client = GithubOrgClient("holberton")

        # Access the _public_repos_url property
        test_return = test_client._public_repos_url

        # Assert that the org property was accessed exactly once
        mock_org.assert_called_once_with()

        # Assert that the result is equal to the expected
        #  repos_url from the mocked org property
        self.assertEqual(test_return, mock_org.return_value.get("repos_url"))
