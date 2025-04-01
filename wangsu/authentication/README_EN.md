# Wangsu SDK for Python

This SDK provides Python interfaces to interact with Wangsu API services.

## Installation

Install the SDK using pip:

```bash
pip install wangsu-sdk-python
```

Install the SDK for a specific product category using pip:

```bash
pip install wangsu-sdk-python-authentication
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
from wangsu.authentication.models import *

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
| Createuser | Create a User for SecureLink | POST | /api/securelink/idaas/user |
| Deletegroup | To delete a local user group, delete the group, users and subgroups in the group. | DELETE | /api/securelink/idaas/usergroup |
| Creategroup | Create a new group for SecureLink | POST | /api/securelink/idaas/usergroup |
| Modifygroup | Modify the specific Group | PUT | /api/securelink/idaas/usergroup |
| Listgroups | Query the groups of specific parent group | GET | /api/securelink/idaas/usergroup/list |
| Listusers | Example Query the list of users in a specified user group | GET | /api/securelink/idaas/user/list |
| Deleteuser | Delete a specific User | DELETE | /api/securelink/idaas/user |
| Modifyuser | Modify the information of the specific user. | PUT | /api/securelink/idaas/user |
| Describeuserinfo | Describe User | GET | /api/securelink/idaas/user |
| Syncauthconfig | sync auth config  | POST | /api/securelink/idaas/authconfig/sync |