# Wangsu SDK for Python

This SDK provides Python interfaces to interact with Wangsu API services.

## Installation

Install the SDK using pip:

```bash
pip install wangsu-sdk-python
```

Install the SDK for a specific product category using pip:

```bash
pip install wangsu-sdk-python-edgehostname
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
from wangsu.edgehostname.models import *

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
| Deleteedgehostname | This API is used to delete a specified Edge Hostname. If the Edge Hostname has never been deployed, calling the API directly deletes the record. If the Edge Hostname is in a deployed state, calling this API will trigger the removal of the deployment and return the deployment task ID. | DELETE | /api/edge-hostnames/* |
| Deployakcdnedgehostname | This API is used to deploy the specified Edge Hostname and returns the deployment task ID. | POST | /api/edge-hostnames/*/deploy |
| Disableedgehostname | This API is used to disable a specified edge hostname. Only edge hostnames that are active are eligible for disabling. Disabling will trigger the deletion of the edge hostname deployment but will not remove the edge hostname record. The API returns the deployment task ID. | POST | /api/edge-hostnames/*/disable |
| Enableedgehostname | This API is used to enable a specific Edge Hostname. Only Edge Hostnames that are in a disabled state can be enabled. Enabling it will trigger an Edge Hostname deployment, and the API will return the deployment task ID. | POST | /api/edge-hostnames/*/enable |
| Queryedgehostname | This API is used to enable a specific Edge Hostname. Only Edge Hostnames that are in a disabled state can be enabled. Enabling it will trigger an Edge Hostname deployment, and the API will return the deployment task ID. | GET | /api/edge-hostnames/* |
| Queryedgehostnames | This API is used to query the list of Edge Hostnames, returning all Edge Hostnames under the account along with their CNAME status and deployment status, with support for pagination. | GET | /api/edge-hostnames |
| Updateedgehostname | This interface is used to modify the basic configuration of the Edge Hostname, enabling self-service control over the routing effects, including remarks, acceleration region restrictions, and region configuration. | PUT | /api/edge-hostnames/* |