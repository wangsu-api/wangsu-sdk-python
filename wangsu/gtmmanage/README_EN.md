# Wangsu SDK for Python

This SDK provides Python interfaces to interact with Wangsu API services.

## Installation

Install the SDK using pip:

```bash
pip install wangsu-sdk-python
```

Install the SDK for a specific product category using pip:

```bash
pip install wangsu-sdk-python-gtmmanage
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
from wangsu.gtmmanage.models import *

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
| Deldispatchpolicy | q | POST | /clouddns/Deldispatchpolicy |
| Controldispatchpolicy | Use to batch enable/disable dispatch policies. Takes one minute to take effect. | POST | /clouddns/Controldispatchpolicy |
| Querydispatchpolicydetail | Used to query the detailed information of dispatch policy. Takes one minute to take effect. | POST | /clouddns/Querydispatchpolicydetail |
| Savedispatchpolicy | Used to add dispatch policy, and the interface used is the same to the one to midify dispatch policy, but the two use different json formats. Takes one minute to take effect. | POST | /clouddns/Savedispatchpolicy |
| Querydispatchpolicies | Used to query dispatch policy information by page. Takes one minute to take effect. | POST | /clouddns/Querydispatchpolicies |
| Controldispatchresource | Start or stop scheduling resources | POST | /clouddns/Controldispatchresource |
| Controlresourcecluster | Scheduling policy enable/disable primary source | POST | /clouddns/Controlresourcecluster |