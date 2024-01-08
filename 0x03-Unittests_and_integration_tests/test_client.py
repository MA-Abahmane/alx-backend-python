#!/usr/bin/env python3

"""
Parameterize and patch as decorators
"""

import unittest
from urllib.error import HTTPError
from parameterized import parameterized
from unittest.mock import patch, Mock, PropertyMock

from client import *
from fixtures import *


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

    def test_public_repos_url(self):
        """ Test _public_repos_url property
        """
        with patch.object(GithubOrgClient, "org", new_callable=PropertyMock,
                          return_value={"repos_url": "holberton"}) as mock_obj:

            # Create an instance of GithubOrgClient
            test_client = GithubOrgClient("holberton")

            # Access the _public_repos_url property
            test_return = test_client._public_repos_url

            # Assert that the org property was accessed exactly once
            mock_obj.assert_called_once

            self.assertEqual(test_return, mock_obj
                             .return_value
                             .get('repos_url'))

    @patch.object(GithubOrgClient, "org", new_callable=PropertyMock,
                  return_value={"repos_url": "holberton"})
    def test_public_repos(self, mock_org):
        """ Test _public_repos_url property
        """

        # Create an instance of GithubOrgClient
        test_client = GithubOrgClient("holberton")

        # Access the _public_repos_url property
        test_return = test_client.public_repos

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected_output):
        """ Test _public_repos_url property
        """

        # Create an instance of GithubOrgClient
        test_client = GithubOrgClient("holberton")

        # Access the _public_repos_url property
        test_return = test_client.has_license(repo, license_key)

        # compare results
        self.assertEqual(test_return, expected_output)


@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ class TestIntegrationGithubOrgClient
    """

    @classmethod
    def setUpClass(cls):
        """ set up Class
        """
        cls.get_patcher = patch('requests.get', side_effect=HTTPError)

    @classmethod
    def tearDownClass(cls):
        """ tear down Class
        """
        cls.get_patcher.stop()

    @classmethod
    def test_public_repos_with_license(cls):
        """ test public repos with licens
        """
        test = GithubOrgClient('holberton')
        assert True

    @classmethod
    def test_public_repos(cls):
        """ test public repos
        """
        test = GithubOrgClient('holberton')
        assert True
