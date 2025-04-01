# Wangsu SDK for Python

This SDK provides Python interfaces to interact with Wangsu API services.

## Installation

Install the SDK using pip:

```bash
pip install wangsu-sdk-python
```

Install the SDK for a specific product category using pip:

```bash
pip install wangsu-sdk-python-reportiplist
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
from wangsu.reportiplist.models import *

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
| Reportserveripispprovinceservice | Query the service IP list of CDN in each ISP and each province | POST | /api/report/server-ip/isp-province |
| Reportserveripexistflowservice | This interface can obtain the corresponding CDN service IP list with Traffic by providing the CDN domain . This function is suitable for scenarios where you need to understand the actual accelerated use of the domain service IP. | POST | /api/report/server-list/exist-flow |
| Querycdniplist | This interface is used to query the coverage node IP list corresponding to each specified domain name in the CDN service. Users can obtain the node IP information of multiple domain names under their account by submitting relevant requests, which is mainly used for traffic scheduling and optimization management. The returned data shows the detailed coverage node IP of each domain name, helping users understand and monitor the node distribution of CDN services. | POST | /api/report/server-list |
| Reportserverlistservice | Query the IP list of a specific domain in the CDN service and its affiliated ISP and region information. Through this interface, users can obtain detailed information about the CDN service node associated with the domain. | GET | /api/report/server-list/ip-isp-area |