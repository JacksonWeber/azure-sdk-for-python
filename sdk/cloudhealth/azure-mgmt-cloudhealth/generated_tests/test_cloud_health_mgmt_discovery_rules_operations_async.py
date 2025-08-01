# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.cloudhealth.aio import CloudHealthMgmtClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer
from devtools_testutils.aio import recorded_by_proxy_async

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestCloudHealthMgmtDiscoveryRulesOperationsAsync(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(CloudHealthMgmtClient, is_async=True)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_discovery_rules_get(self, resource_group):
        response = await self.client.discovery_rules.get(
            resource_group_name=resource_group.name,
            health_model_name="str",
            discovery_rule_name="str",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_discovery_rules_create_or_update(self, resource_group):
        response = await self.client.discovery_rules.create_or_update(
            resource_group_name=resource_group.name,
            health_model_name="str",
            discovery_rule_name="str",
            resource={
                "id": "str",
                "name": "str",
                "properties": {
                    "addRecommendedSignals": "str",
                    "authenticationSetting": "str",
                    "discoverRelationships": "str",
                    "entityName": "str",
                    "resourceGraphQuery": "str",
                    "deletionDate": "2020-02-20 00:00:00",
                    "displayName": "str",
                    "errorMessage": "str",
                    "numberOfDiscoveredEntities": 0,
                    "provisioningState": "str",
                },
                "systemData": {
                    "createdAt": "2020-02-20 00:00:00",
                    "createdBy": "str",
                    "createdByType": "str",
                    "lastModifiedAt": "2020-02-20 00:00:00",
                    "lastModifiedBy": "str",
                    "lastModifiedByType": "str",
                },
                "type": "str",
            },
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_discovery_rules_delete(self, resource_group):
        response = await self.client.discovery_rules.delete(
            resource_group_name=resource_group.name,
            health_model_name="str",
            discovery_rule_name="str",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_discovery_rules_list_by_health_model(self, resource_group):
        response = self.client.discovery_rules.list_by_health_model(
            resource_group_name=resource_group.name,
            health_model_name="str",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...
