# Wangsu SDK for Python

This SDK provides Python interfaces to interact with Wangsu API services.

## Installation

Install the SDK using pip:

```bash
pip install wangsu-sdk-python
```

Install the SDK for a specific product category using pip:

```bash
pip install wangsu-sdk-python-ngcontentmanagement
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
from wangsu.ngcontentmanagement.models import *

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
| CreateAPurgeRequest | CreateAPurgeRequest to force a refresh of the content stored in the CDN Pro cache servers.  You may wish to do this if you just updated content on your origin server and want visitors to see the changes right away rather than wait for the updates to propagate according to the schedule defined in your property configuration. | POST | /cdn/purges |
| GetListOfPurgeRequests | Get a list of purge requests. The API only returns purge requests that were created in the past 15 days. | GET | /cdn/purges |
| GetPurgeSummary | Returns a summary of purge requests that were made during a time period. Query parameters let you specify the timeframe and target environment. | GET | /cdn/purges/purgeSummary |
| GetPurgeRequestStatus | Gets information about a purge request including its associated hostnames and status. | GET | /cdn/purges/* |
| CreateAPrefetchRequest | CreateAPrefetchRequest to warm up the CDN Pro cache with contents from your origin in anticipation of visitors. This is helpful to prevent a sudden influx of requests to your origin servers. The URLs you prefetch must be for hostnames of properties deployed to production.<br> | POST | /cdn/prefetches |
| GetListOfPrefetchRequests | Get a list of prefetch requests. The API only returns prefetch requests that were created in the past 15 days. | GET | /cdn/prefetches |
| GetPrefetchRequestStatus | Get details on the status of a prefetch request. | GET | /cdn/prefetches/* |
| GetAvailablePurgeRequests | This API indicates the number of directory and file purge requests you can make in the staging or production environments. Your service quota specifies a daily limit on file and directory purges for production and staging environments. You can temporarily exceed the limit during a day, but it will reduce the number of purges available during the next day. | GET | /cdn/purges/purgeTokens |