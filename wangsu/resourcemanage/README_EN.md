# Wangsu SDK for Python

This SDK provides Python interfaces to interact with Wangsu API services.

## Installation

Install the SDK using pip:

```bash
pip install wangsu-sdk-python
```

Install the SDK for a specific product category using pip:

```bash
pip install wangsu-sdk-python-resourcemanage
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
from wangsu.resourcemanage.models import *

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
| Vmpqueryflavor | You can use this interface to query the specification list of instances that a certain region can provide, and then create instances using this specification. | GET | /vmp/flavors |
| Vmpquerynode | Query which nodes of the edge computing platform can provide services. | GET | /vmp/nodes |
| Vmpquerybandwidth | Query the real-time redundant bandwidth of all the nodes you are using. Nodes with redundant bandwidth will return True, while nodes without redundant bandwidth will return False. If the bandwidth data collection results of the node are insufficient to support the timeliness requirements of the interface, that is, if the bandwidth statistics data is old and does not meet the timeliness requirements, undefined will be returned.<br>The judgment method for whether a node has redundant bandwidth: the upper limit bandwidth of the node is greater than the real-time usage bandwidth of the node. Data granularity: 5 minutes. | POST | /vmp/redundant-bandwidth |
| Noderedundantbandwidth4pstatp | Query for node redundant bandwidth | GET | /vmp/nodeRedundantBandwidth4Pstatp |