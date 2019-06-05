from settings import AZURE_TENANT_ID, AZURE_CLIENT_ID, AZURE_CLIENT_SECRET, AZURE_SUBSCRIPTION_ID
import azure.mgmt.managementgroups

# This script expects that the following environment vars are set in settings.py:
#
# AZURE_TENANT_ID: with your Azure Active Directory tenant id or domain
# AZURE_CLIENT_ID: with your Azure Active Directory Application Client ID
# AZURE_CLIENT_SECRET: with your Azure Active Directory Application Secret
# AZURE_SUBSCRIPTION_ID: with your Azure Subscription Id
#

if __name__ == "__main__":
    print(AZURE_TENANT_ID)
    print(AZURE_CLIENT_ID)
    print(AZURE_CLIENT_SECRET)
    print(AZURE_SUBSCRIPTION_ID)