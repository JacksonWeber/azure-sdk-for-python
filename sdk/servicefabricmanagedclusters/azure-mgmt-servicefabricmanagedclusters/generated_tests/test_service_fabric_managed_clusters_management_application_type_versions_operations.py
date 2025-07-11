# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.servicefabricmanagedclusters import ServiceFabricManagedClustersManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer, recorded_by_proxy

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestServiceFabricManagedClustersManagementApplicationTypeVersionsOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(ServiceFabricManagedClustersManagementClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_application_type_versions_get(self, resource_group):
        response = self.client.application_type_versions.get(
            resource_group_name=resource_group.name,
            cluster_name="str",
            application_type_name="str",
            version="str",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_application_type_versions_begin_create_or_update(self, resource_group):
        response = self.client.application_type_versions.begin_create_or_update(
            resource_group_name=resource_group.name,
            cluster_name="str",
            application_type_name="str",
            version="str",
            parameters={
                "id": "str",
                "location": "str",
                "name": "str",
                "properties": {"appPackageUrl": "str", "provisioningState": "str"},
                "systemData": {
                    "createdAt": "2020-02-20 00:00:00",
                    "createdBy": "str",
                    "createdByType": "str",
                    "lastModifiedAt": "2020-02-20 00:00:00",
                    "lastModifiedBy": "str",
                    "lastModifiedByType": "str",
                },
                "tags": {"str": "str"},
                "type": "str",
            },
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_application_type_versions_update(self, resource_group):
        response = self.client.application_type_versions.update(
            resource_group_name=resource_group.name,
            cluster_name="str",
            application_type_name="str",
            version="str",
            parameters={"tags": {"str": "str"}},
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_application_type_versions_begin_delete(self, resource_group):
        response = self.client.application_type_versions.begin_delete(
            resource_group_name=resource_group.name,
            cluster_name="str",
            application_type_name="str",
            version="str",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_application_type_versions_list_by_application_types(self, resource_group):
        response = self.client.application_type_versions.list_by_application_types(
            resource_group_name=resource_group.name,
            cluster_name="str",
            application_type_name="str",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...
