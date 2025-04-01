# Wangsu SDK for Python

This SDK provides Python interfaces to interact with Wangsu API services.

## Installation

Install the SDK using pip:

```bash
pip install wangsu-sdk-python
```

Install the SDK for a specific product category using pip:

```bash
pip install wangsu-sdk-python-edgekv
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
from wangsu.edgekv.models import *

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
| Deletekeyvalue | Delete multiple KV pairs from the namespace.  | DELETE | /edgekv/kv |
| Setkeyvalue | Write kv pairs to the specified namespace | PUT | /edgekv/kv |
| Getkeyvalue | get key value  from the specified namespace | POST | /edgekv/kv |
| Createshorturl | Short Url Create | POST | /short-urls/create |
| Getshorturl | query long url by short url | POST | /short-urls/query |
| Delshorturl | delete  short url | POST | /short-urls/del |
| Ecakvinfo | Query edge KV storage information, including: storage capacity, read request count, write request count, delete request count. | POST | /myview/Ecakvinfo |
| Sharkletvisit | Number of edge application requests, including basic application requests, medium-sized application requests, and special application requests | POST | /myview/sharkletVisit |