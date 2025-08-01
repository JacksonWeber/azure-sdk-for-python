# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.dnsresolver.aio import DnsResolverManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer
from devtools_testutils.aio import recorded_by_proxy_async

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestDnsResolverManagementDnsForwardingRulesetsOperationsAsync(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(DnsResolverManagementClient, is_async=True)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_dns_forwarding_rulesets_begin_create_or_update(self, resource_group):
        response = await (
            await self.client.dns_forwarding_rulesets.begin_create_or_update(
                resource_group_name=resource_group.name,
                dns_forwarding_ruleset_name="str",
                parameters={
                    "dnsResolverOutboundEndpoints": [{"id": "str"}],
                    "location": "str",
                    "etag": "str",
                    "id": "str",
                    "name": "str",
                    "provisioningState": "str",
                    "resourceGuid": "str",
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
                api_version="2025-05-01",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_dns_forwarding_rulesets_begin_update(self, resource_group):
        response = await (
            await self.client.dns_forwarding_rulesets.begin_update(
                resource_group_name=resource_group.name,
                dns_forwarding_ruleset_name="str",
                parameters={"dnsResolverOutboundEndpoints": [{"id": "str"}], "tags": {"str": "str"}},
                api_version="2025-05-01",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_dns_forwarding_rulesets_begin_delete(self, resource_group):
        response = await (
            await self.client.dns_forwarding_rulesets.begin_delete(
                resource_group_name=resource_group.name,
                dns_forwarding_ruleset_name="str",
                api_version="2025-05-01",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_dns_forwarding_rulesets_get(self, resource_group):
        response = await self.client.dns_forwarding_rulesets.get(
            resource_group_name=resource_group.name,
            dns_forwarding_ruleset_name="str",
            api_version="2025-05-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_dns_forwarding_rulesets_list_by_resource_group(self, resource_group):
        response = self.client.dns_forwarding_rulesets.list_by_resource_group(
            resource_group_name=resource_group.name,
            api_version="2025-05-01",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_dns_forwarding_rulesets_list(self, resource_group):
        response = self.client.dns_forwarding_rulesets.list(
            api_version="2025-05-01",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_dns_forwarding_rulesets_list_by_virtual_network(self, resource_group):
        response = self.client.dns_forwarding_rulesets.list_by_virtual_network(
            resource_group_name=resource_group.name,
            virtual_network_name="str",
            api_version="2025-05-01",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...
