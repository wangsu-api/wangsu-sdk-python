# Wangsu SDK for Python

This SDK provides Python interfaces to interact with Wangsu API services.

## Installation

Install the SDK using pip:

```bash
pip install wangsu-sdk-python
```

Install the SDK for a specific product category using pip:

```bash
pip install wangsu-sdk-python-security
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
from wangsu.security.models import *

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
| Vmpcreatesshkey | When creating an instance, it can specify the use of key pairs. Before that, it need to create a key pair. | POST | /vmp/osKeypairs |
| Vmpquerysshkey | Query all key pairs. | GET | /vmp/osKeypairs |
| Vmpremovesshkey | Delete the specified key pair by name. The instances created using this key pair are not affected and cannot be found on the query interface after deletion, nor can new instances be created using this key pair. | DELETE | /vmp/osKeypairs/* |
| Vmpquerysecuritygroup | Used to query the basic information of security groups created by customers. | GET | /vmp/security-group |
| Vmpbindsecuritygroup | Use to change the binding relationship between an instance and a security group. Only virtual instances support binding security groups, not bare metal instances. | PUT | /vmp/security-group/server |
| Deletionsecuritygrouprules | Used to delete security group rule information. | DELETE | /vmp/security-group/rule/* |
| Editsecuritygrouprules | Used to modify security group rule information. | PUT | /vmp/security-group/rule |
| Addsecuritygrouprules | Used to add security group rule information.<br>1) Within the same security group, the content of different rules cannot be completely the same;<br>2) When adding multiple rules in bulk, the result is either successful or failed addition. | POST | /vmp/security-group/rule |
| Deletesecuritygroup | Used to delete security group information. If the security group has defined rules, they will be deleted together with the rules.<br>Explanation:<br>1) If there is currently an instance bound to a security group, the deletion of the security group fails;<br>2) When deleting multiple security groups in bulk, if one security group fails to be deleted, it does not affect the normal deletion of other security groups. | DELETE | /vmp/security-group/* |
| Editsecuritygroup | Used to modify the security group name or comment information. | PUT | /vmp/security-group |
| Addsecuritygroup | Used to add a security group. | POST | /vmp/security-group |