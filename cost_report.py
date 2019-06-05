""" Report on Dev Tenant Usage """

from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.managementgroups import ManagementGroupsAPI
from settings import AZURE_TENANT_ID, AZURE_CLIENT_ID, AZURE_KEY, AZURE_SUBSCRIPTION_ID

# This script expects that the following environment vars are set in settings.py:
#
# AZURE_TENANT_ID: with your Azure Active Directory tenant id or domain
# AZURE_CLIENT_ID: with your Azure Active Directory Application Client ID
# AZURE_CLIENT_SECRET: with your Azure Active Directory Application Secret
# AZURE_SUBSCRIPTION_ID: with your Azure Subscription Id
#

if __name__ == "__main__":

    # Delete me
    print(AZURE_TENANT_ID)
    print(AZURE_CLIENT_ID)
    print(AZURE_KEY)
    print(AZURE_SUBSCRIPTION_ID)

    credentials = ServicePrincipalCredentials(
        client_id=AZURE_CLIENT_ID,
        secret=AZURE_KEY,
        tenant=AZURE_TENANT_ID
    )

    management_group_client = ManagementGroupsAPI(credentials, base_url=None)

    dir_test = vars(management_group_client)
    print("Vars")
    print(dir_test)


