# Wangsu SDK for Python

This SDK provides Python interfaces to interact with Wangsu API services.

## Installation

Install the SDK using pip:

```bash
pip install wangsu-sdk-python
```

Install the SDK for a specific product category using pip:

```bash
pip install wangsu-sdk-python-appmanage
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
from wangsu.appmanage.models import *

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
| Manageephoneapp | Specify the ePhone instance to perform application operations, including application installation, uninstallation, start, stop and data clearing. | POST | /ephone/apps/action |
| Queryapplist | Gets the list of applications for the specified edge cloud phone instance. | GET | /ephone/apps/list |
| Addtunnelapplications | This API is used to add new tunnel access applications. Users can specify the application's name and content. Before authoring application permissions to users, the application must be created first. | POST | /api/securelink/idaas/tunnelapp/add |
| Updatetunnelapplications | This API is used to modify tunnel access applications. Users can change the application's name and content. When there are changes to application information (such as IP or domain name), this API can be used to make modifications so that users can continue to access the application normally. | POST | /api/securelink/idaas/tunnelapp/update |
| Updatewebapplications | This API is used to modify Web access applications. Users can change the application's name and content. When there are changes to application information (such as IP or domain name), this API can be used to make modifications so that users can continue to access the application normally. | POST | /api/securelink/idaas/webapp/update |
| Addwebapplications | This API is used to add new Web access applications. Users can specify the application's name and content. Before authoring application permissions to users, the application must be created first. | POST | /api/securelink/idaas/webapp/add |
| Deletewebapplications | This API is used to delete web access applications. After a web access application is taken offline, this API can be used to delete the application. Before deleting a web access application, it is necessary to ensure that the application is not in use (for example, not authorized to users), otherwise, the deletion will fail. | POST | /api/securelink/idaas/webapp/delete |
| Deletetunnelapplications | This API is used to delete tunnel access applications. After a tunnel access application is taken offline, this API can be used to delete the application. Before deleting a tunnel access application, it is necessary to ensure that the application is not in use (for example, not authorized to users), otherwise, the deletion will fail. | POST | /api/securelink/idaas/tunnelapp/delete |
| Queryapplicationdetail | This API is used to query detailed information about tunnel access applications or web access applications. It can be used to query the application's content, application administrators, associated permission groups, and directly authorized users/user groups. | POST | /api/securelink/idaas/application/query |
| Authorizeapplicationforuser | This API is used to directly authorize specified applications to users/user groups. It allows adding additional authorized users for the application or overriding users who are already authorized. Directly authorizing applications to users makes it easier for enterprise administrators to manage application permissions. | POST | /api/securelink/idaas/application/grantToUser |
| Authorizeuserapplication | This API is used to directly authorize applications for specified users. It allows adding additional authorized applications for users or overriding the applications that users are already authorized for. Directly authorizing applications for users facilitates enterprise administrators in managing user application permissions. | POST | /api/securelink/idaas/application/user-bind |
| Describeauthorizedapplicationsofuser | This API is used to query the list of applications currently authorized for a specified user. When an administrator needs to confirm the applications authorized for a user, this API can be used to verify whether the user's application permissions are appropriate. | POST | /api/securelink/idaas/application/user-resource |
| Createapp | Create an application to integrate with Android or iOS applications, and return the application ID. | POST | /mah/v1/app/create |
| Adddebugfingerprint | Add debugging fingerprints for application debugging, Android applications only. | POST | /mah/v1/app/add-debug-fingerprint |
| Deleteapp | Delete application; specify application ID to remove the corresponding application | POST | /mah/v1/app/delete |