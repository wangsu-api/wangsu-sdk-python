# Wangsu SDK for Python

This SDK provides Python interfaces to interact with Wangsu API services.

## Installation

Install the SDK using pip:

```bash
pip install wangsu-sdk-python
```

Install the SDK for a specific product category using pip:

```bash
pip install wangsu-sdk-python-cacherefresh
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
from wangsu.cacherefresh.models import *

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
| Querypurgestatus | Query the purge task status. Use this API to check if the task has been completed successfully throughout the global CDN. | POST | /ccm/purge/ItemIdQuery |
| Purgefilewithtag | Push the file with the tag in the domain name with the tag switch enabled under the customer | POST | /api/content/tag/purge |
| Regexurlpurge | The content of the file cached on the CDN node is cleared according to the regular url method, and the entire network takes effect within 1 minute. | POST | /api/content/regular-url/purge |
| Purge | Refresh the files cached on the CDN nodes, which takes effect throughout the whole CDN within about 10 minutes. | POST | /ccm/purge/ItemIdReceiver |
| Querypurgelimit | query purge daily limit | POST | /ccm/purge/limit |
| Querypurgeresiduals | Query url purge , directory purge and prefetch daily limit . | GET | /ccm/upperQuery |