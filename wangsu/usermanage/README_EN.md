# Wangsu SDK for Python

This SDK provides Python interfaces to interact with Wangsu API services.

## Installation

Install the SDK using pip:

```bash
pip install wangsu-sdk-python
```

Install the SDK for a specific product category using pip:

```bash
pip install wangsu-sdk-python-usermanage
```


## Requirements

- Python 3.6 or later
- Dependencies:
  - requests >= 2.10.0
  - alibabacloud_tea >= 0.3.3
  - alibabacloud_tea_openapi >= 0.3.6
  - alibabacloud_tea_console >= 0.0.1
  - alibabacloud_tea_util >= 0.3.8

## Quick Start

### Example

The SDK uses AKSK authentication. You need to configure your access key and secret key:

```python
import json
from wangsu.common.auth.AkSkConfig import AkSkConfig
from wangsu.common.auth.AkSkAuth import AkSkAuth
from wangsu.usermanage.models import *

# Refer to the API list at the end of this document and modify the corresponding {ActionName}, Method, Uri
request = {ActionName}Request()

aksk_config = AkSkConfig()
aksk_config.access_key = "YOUR_ACCESS_KEY"
aksk_config.secret_key = "YOUR_SECRET_KEY"
aksk_config.uri = "/your/api/path"
aksk_config.method = "GET"  # HTTP method: GET, POST, PUT, DELETE, etc.

# Convert request to JSON and make the API call
response = AkSkAuth.invoke(aksk_config, json.dumps(request.to_map()))
print(response)

```



## API List
For detailed API documentation and available methods, please refer to the [official Wangsu API documentation](https://www.wangsu.com/document/api-doc/Overview?productType=all).

| ActionName | enDescription | client_methods | uri |
| --- | --- | --- | --- |
| Addsubaccount | Create a sub account | POST | /sub-account |
| Querysubaccountinfo | Get sub account | GET | /sub-account/* |
| Getsubaccountlist | Get the list of sub-users by the main account | POST | /sub-account/list |
| Updatesubaccount | Update sub account | PUT | /sub-account |
| Deletesubaccount | Delete Specified sub-users | DELETE | /sub-account/* |
| Querypolicyattachedmainaccountorsubaccount | This interface is used to query the list of permission policies associated with a specified user. By entering their login name, users can obtain information about the policies linked to them, including the policy ID, name, description, type (system policy or custom policy), and support for multilingual descriptions. The results returned by the interface include status codes and related information to help users understand the specific attributes and classifications of the policies. This is very useful for managing user permissions and creating or modifying permission policies, enabling system administrators to configure and adjust permissions more efficiently. | GET | /user/policy-attached/* |
| Batchaddorrevokepolicytosubaccount | This interface is used to batch add or revoke permission policies for a specified sub-user. By inputting the sub-user's login name and a list of permission policy identifiers, you can choose to perform add or revoke operations. When adding permissions, the system will add the corresponding policies to the sub-account to expand its permission scope; when revoking permissions, it will remove the specified policies, reducing the sub-account's access permissions. The return value includes a request status code and operation information prompts, allowing users to confirm the success of the batch operation. This interface is suitable for scenarios where centralized management of sub-account permissions is needed, simplifying the process of batch permission adjustments.<br><br><br> | POST | /user/policies |
| Checkloginnamelegal | Check login name legal | POST | /login-name/check |
| Addaccountident | Add account aksk<br> | POST | /account-ident |
| Deleteaccountident | Delete account aksk | DELETE | /account-ident/* |
| Updateaccountident | Update account aksk<br> | PUT | /account-ident |
| Listaccountident | List account aksk<br> | POST | /account-ident/list |
| Queryagentassociatedmainaccountservice | This interface is used to query the relationship between multi-level agent accounts and their associated main accounts. Through this interface, users can understand detailed information about each agent account's main account, including the main account's display name, login name, and the login name of its corresponding parent main account. When calling this interface, users receive status codes and messages about the request, ensuring transparency of the query execution. This interface is suitable for scenarios requiring the management and querying of complex hierarchical agent account relationships, helping to enhance overall understanding and control of account management. | POST | /user/multilevel-agent/main-accounts |