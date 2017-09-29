# coding: utf-8

"""


    No descripton provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version:

    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.apis.apiskubevirtiovalpha_api import ApiskubevirtiovalphaApi


class TestApiskubevirtiovalphaApi(unittest.TestCase):
    """ ApiskubevirtiovalphaApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.apiskubevirtiovalpha_api.ApiskubevirtiovalphaApi()

    def tearDown(self):
        pass

    def test_console(self):
        """
        Test case for console

        Open a websocket connection to a serial console on the specified VM.
        """
        pass

    def test_create_migration(self):
        """
        Test case for create_migration


        """
        pass

    def test_create_virtualmachine(self):
        """
        Test case for create_virtualmachine


        """
        pass

    def test_create_virtualmachinereplicaset(self):
        """
        Test case for create_virtualmachinereplicaset


        """
        pass

    def test_delete_migration(self):
        """
        Test case for delete_migration

        test3
        """
        pass

    def test_delete_migrations(self):
        """
        Test case for delete_migrations


        """
        pass

    def test_delete_virtualmachine(self):
        """
        Test case for delete_virtualmachine

        test3
        """
        pass

    def test_delete_virtualmachinereplicaset(self):
        """
        Test case for delete_virtualmachinereplicaset

        test3
        """
        pass

    def test_delete_virtualmachinereplicasets(self):
        """
        Test case for delete_virtualmachinereplicasets


        """
        pass

    def test_delete_virtualmachines(self):
        """
        Test case for delete_virtualmachines


        """
        pass

    def test_func1(self):
        """
        Test case for func1


        """
        pass

    def test_get_migration(self):
        """
        Test case for get_migration

        test4
        """
        pass

    def test_get_virtualmachine(self):
        """
        Test case for get_virtualmachine

        test4
        """
        pass

    def test_get_virtualmachinereplicaset(self):
        """
        Test case for get_virtualmachinereplicaset

        test4
        """
        pass

    def test_kube_connection_healthz_func(self):
        """
        Test case for kube_connection_healthz_func

        Health endpoint
        """
        pass

    def test_list_all_migrations(self):
        """
        Test case for list_all_migrations

        test4
        """
        pass

    def test_list_all_virtualmachinereplicasets(self):
        """
        Test case for list_all_virtualmachinereplicasets

        test4
        """
        pass

    def test_list_all_virtualmachines(self):
        """
        Test case for list_all_virtualmachines

        test4
        """
        pass

    def test_list_migrations(self):
        """
        Test case for list_migrations


        """
        pass

    def test_list_virtualmachinereplicasets(self):
        """
        Test case for list_virtualmachinereplicasets


        """
        pass

    def test_list_virtualmachines(self):
        """
        Test case for list_virtualmachines


        """
        pass

    def test_patch_migration(self):
        """
        Test case for patch_migration

        test5
        """
        pass

    def test_patch_virtualmachine(self):
        """
        Test case for patch_virtualmachine

        test5
        """
        pass

    def test_patch_virtualmachinereplicaset(self):
        """
        Test case for patch_virtualmachinereplicaset

        test5
        """
        pass

    def test_spice(self):
        """
        Test case for spice

        Returns a remote-viewer configuration file. Run `man 1 remote-viewer` to learn more about the configuration format.
        """
        pass

    def test_update_migration(self):
        """
        Test case for update_migration

        test2
        """
        pass

    def test_update_virtualmachine(self):
        """
        Test case for update_virtualmachine

        test2
        """
        pass

    def test_update_virtualmachinereplicaset(self):
        """
        Test case for update_virtualmachinereplicaset

        test2
        """
        pass

    def test_watch_all_migrations(self):
        """
        Test case for watch_all_migrations


        """
        pass

    def test_watch_all_virtualmachinereplicasets(self):
        """
        Test case for watch_all_virtualmachinereplicasets


        """
        pass

    def test_watch_all_virtualmachines(self):
        """
        Test case for watch_all_virtualmachines


        """
        pass

    def test_watch_migrations(self):
        """
        Test case for watch_migrations


        """
        pass

    def test_watch_virtualmachinereplicasets(self):
        """
        Test case for watch_virtualmachinereplicasets


        """
        pass

    def test_watch_virtualmachines(self):
        """
        Test case for watch_virtualmachines


        """
        pass


if __name__ == '__main__':
    unittest.main()
