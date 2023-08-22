import CloudBilling
import CloudCatalog
from google.cloud.billing import budgets_v1beta1

# main starts here!!!! this function is being triggerd by messages in the pubsub trigger
def subscribe(cloud_event, context):
    import base64
    import json
    #import uuid
    # decode the base64 encoded payload which is the value of the key data
    response = (base64.b64decode(cloud_event["data"]))
    # decode bytes format and make a dictionary out of it
    response_dict = json.loads(response.decode())
    # select the payload which is identified with the dictionary key 'protoPayload'
    payload = response_dict['protoPayload']
    # From the whole payload we only need the value which project is being targeted. We find that as a value with the key 'resourceName'
    project= payload['resourceName']
    # the value returns projects/<PROJECT-ID>. We just need the project-id so we split the string and take the right part of it and store that in the variable for further use...
    project_id = project.rsplit('/',1)[1]
    # set the folder ID´s to exclude all project in that folder or subfolders
    sample_create_budget(project_id)



def sample_create_budget():
    # Create a client
    client = budgets_v1beta1.BudgetServiceClient()

    # Initialize request argument(s)
    request = budgets_v1beta1.CreateBudgetRequest(
        parent="parent_value",
    )

    # Make the request
    response = client.create_budget(request=request)

    # Handle the response
    print(response)