# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.hybridcompute.aio import HybridComputeManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer
from devtools_testutils.aio import recorded_by_proxy_async

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestHybridComputeManagementLicensesOperationsAsync(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(HybridComputeManagementClient, is_async=True)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_licenses_begin_validate_license(self, resource_group):
        response = await (
            await self.client.licenses.begin_validate_license(
                parameters={
                    "location": "str",
                    "id": "str",
                    "licenseDetails": {
                        "assignedLicenses": 0,
                        "edition": "str",
                        "immutableId": "str",
                        "processors": 0,
                        "state": "str",
                        "target": "str",
                        "type": "str",
                        "volumeLicenseDetails": [{"invoiceId": "str", "programYear": "str"}],
                    },
                    "licenseType": "str",
                    "name": "str",
                    "provisioningState": "str",
                    "systemData": {
                        "createdAt": "2020-02-20 00:00:00",
                        "createdBy": "str",
                        "createdByType": "str",
                        "lastModifiedAt": "2020-02-20 00:00:00",
                        "lastModifiedBy": "str",
                        "lastModifiedByType": "str",
                    },
                    "tags": {"str": "str"},
                    "tenantId": "str",
                    "type": "str",
                },
                api_version="2025-02-19-preview",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_licenses_begin_create_or_update(self, resource_group):
        response = await (
            await self.client.licenses.begin_create_or_update(
                resource_group_name=resource_group.name,
                license_name="str",
                parameters={
                    "location": "str",
                    "id": "str",
                    "licenseDetails": {
                        "assignedLicenses": 0,
                        "edition": "str",
                        "immutableId": "str",
                        "processors": 0,
                        "state": "str",
                        "target": "str",
                        "type": "str",
                        "volumeLicenseDetails": [{"invoiceId": "str", "programYear": "str"}],
                    },
                    "licenseType": "str",
                    "name": "str",
                    "provisioningState": "str",
                    "systemData": {
                        "createdAt": "2020-02-20 00:00:00",
                        "createdBy": "str",
                        "createdByType": "str",
                        "lastModifiedAt": "2020-02-20 00:00:00",
                        "lastModifiedBy": "str",
                        "lastModifiedByType": "str",
                    },
                    "tags": {"str": "str"},
                    "tenantId": "str",
                    "type": "str",
                },
                api_version="2025-02-19-preview",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_licenses_begin_update(self, resource_group):
        response = await (
            await self.client.licenses.begin_update(
                resource_group_name=resource_group.name,
                license_name="str",
                parameters={
                    "edition": "str",
                    "licenseType": "str",
                    "processors": 0,
                    "state": "str",
                    "tags": {"str": "str"},
                    "target": "str",
                    "type": "str",
                },
                api_version="2025-02-19-preview",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_licenses_get(self, resource_group):
        response = await self.client.licenses.get(
            resource_group_name=resource_group.name,
            license_name="str",
            api_version="2025-02-19-preview",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_licenses_begin_delete(self, resource_group):
        response = await (
            await self.client.licenses.begin_delete(
                resource_group_name=resource_group.name,
                license_name="str",
                api_version="2025-02-19-preview",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_licenses_list_by_resource_group(self, resource_group):
        response = self.client.licenses.list_by_resource_group(
            resource_group_name=resource_group.name,
            api_version="2025-02-19-preview",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_licenses_list_by_subscription(self, resource_group):
        response = self.client.licenses.list_by_subscription(
            api_version="2025-02-19-preview",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...
