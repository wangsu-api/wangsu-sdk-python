# Wangsu SDK for Python

This SDK provides Python interfaces to interact with Wangsu API services.

## Installation

Install the SDK using pip:

```bash
pip install wangsu-sdk-python
```

Install the SDK for a specific product category using pip:

```bash
pip install wangsu-sdk-python-basicpermission
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
from wangsu.basicpermission.models import *

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
| Addterminalauth | Add a terminal authority. | POST | /api/securelink/idaas/terminalauth |
| Updateterminalauth | edit a terminal authority. | PUT | /api/securelink/idaas/terminalauth |
| Deleteterminalauth | delete a terminal auth by terminalAuthId. | DELETE | /api/securelink/idaas/terminalauth |
| Addterminalauthuserorgroup | Basic permissions are associated with users or user groups. | POST | /api/securelink/idaas/terminalauth/user-group |
| Queryterminalauthlist | Get a list of basic permissions. | GET | /api/securelink/idaas/terminalauth |
| Queryterminalauthinfo | Query basic permission information | GET | /api/securelink/idaas/terminalauth/query |
| Removeterminalauthresource | Remove apps associated with basic permissions | DELETE | /api/securelink/idaas/terminalauth/related-resources |
| Removeterminalauthuserorgroup | Remove users or user groups associated with basic permissions | DELETE | /api/securelink/idaas/terminalauth/user-group |
| Queryterminalauthresourcelist | Get the list of applications with basic permissions | GET | /api/securelink/idaas/terminalauth/resources |
| Updateterminalauthrelatedresources | Modify applications associated with basic permissions | PUT | /api/securelink/idaas/terminalauth/related-resources |
| Queryterminalusergroupbyauthconfig | query terminal user group list by auth config. | GET | /api/securelink/idaas/usergroup/list-by-authconfig |
| Associaterightsgroupstouserorusergroup | This API is used to directly associate a permission group with specified users/user groups. If multiple users need to be assigned the same set of application permissions, the administrator can first associate the applications with a single permission group and then use this API to assign it to the users/user groups. | POST | /api/securelink/idaas/terminalauth/user-bind |