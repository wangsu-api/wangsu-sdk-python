# Wangsu SDK for Python

This SDK provides Python interfaces to interact with Wangsu API services.

## Installation

Install the SDK using pip:

```bash
pip install wangsu-sdk-python
```

Install the SDK for a specific product category using pip:

```bash
pip install wangsu-sdk-python-configcenter
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
from wangsu.configcenter.models import *

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
| Createconfigmap | create configmap | POST | /api/v1/namespaces/*/configmaps |
| Listconfigmap | query list of configmap | GET | /api/v1/namespaces/*/configmaps |
| Getconfigmap | query details of configmap | GET | /api/v1/namespaces/*/configmaps/* |
| Updateconfigmap | update configmap | PUT | /api/v1/namespaces/*/configmaps/* |
| Deleteconfigmap | delete configmap | DELETE | /api/v1/namespaces/*/configmaps/* |
| Listsecret | query list of secret | GET | /api/v1/namespaces/*/secrets |
| Getsecret | query details of secret | GET | /api/v1/namespaces/*/secrets/* |
| Createsecret | create secret | POST | /api/v1/namespaces/*/secrets |
| Updatesecret | update secret | PUT | /api/v1/namespaces/*/secrets/* |
| Deletesecret | delete secret | DELETE | /api/v1/namespaces/*/secrets/* |
| Putpatchconfigmap | partial update configmap | PUT | /api/v1/namespaces/*/configmaps/*/ws/patch |
| Putpatchsecret | partial update secret | PUT | /api/v1/namespaces/*/secrets/*/ws/patch |
| Gettoken | get authentication token | GET | /openapi/custom/api/v1/token |