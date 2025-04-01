# Wangsu SDK for Python

This SDK provides Python interfaces to interact with Wangsu API services.

## Installation

Install the SDK using pip:

```bash
pip install wangsu-sdk-python
```

Install the SDK for a specific product category using pip:

```bash
pip install wangsu-sdk-python-webhooks
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
from wangsu.webhooks.models import *

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
| GetAListOfWebhooks | GetAListOfWebhooks that have been defined. You can reference a webhook when creating a deployment task, creating a purge request, creating a prefetch request, or creating a validation task. | GET | /cdn/webhooks |
| GetAWebhook | This API returns details about a webhook including its URL and metadata about its use. | GET | /cdn/webhooks/* |
| DeleteAWebhook | DeleteAWebhook. If an asychronous task using it is still in progress, the webhook may not be called when the task completes. | DELETE | /cdn/webhooks/* |
| UpdateAWebhook | UpdateAWebhook. Only the fields in the request body will be updated. | PATCH | /cdn/webhooks/* |
| CreateAWebhook | CreateAWebhook. It can be used to notify you when an asynchronous task completes. You can reference a webhook when creating a deployment task, creating a purge request, creating a prefetch request, or creating a validation task. | POST | /cdn/webhooks |