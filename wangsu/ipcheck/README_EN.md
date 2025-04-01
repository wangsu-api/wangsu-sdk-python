# Wangsu SDK for Python

This SDK provides Python interfaces to interact with Wangsu API services.

## Installation

Install the SDK using pip:

```bash
pip install wangsu-sdk-python
```

Install the SDK for a specific product category using pip:

```bash
pip install wangsu-sdk-python-ipcheck
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
from wangsu.ipcheck.models import *

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
| Querycdnservicerealip | This interface is used to obtain the real IP list of the CDN service, which is particularly suitable for scenarios where the source station has set whitelist restrictions. Users can obtain the IP whitelist of the CDN node provided by our company for back-to-source by calling this interface, so as to correctly configure and ensure that the data request can smoothly reach the source station through the CDN. | GET | /api/si/report/whiteip-list |
| Queryspecificipbelong | Query whether a given IP address belongs to our CDN IP. The user needs to provide a list of IP addresses. The returned result includes whether each IP address belongs to our CDN IP. | POST | /api/si/tools/ipCheck |
| Ipinfoservice | This API is used to query the affiliation information of specific IP addresses. Users can provide one or more IP addresses to check if they belong to the company CDN nodes, as well as their affiliated country, province, city, and carrier information. The returned results include an identifier indicating whether the IP is a company CDN node; if not, it will return 'unknown'. This API applies when users want to check if an IP is our company's IP. | POST | /api/tools/ip-info |
| Checkiscuswhiteip | This interface is used to supplement the CDN acceleration IP query functionality. It mainly provides customers with the ability to check whether an IP is a real service node resource pool IP that provides acceleration services. | GET | /task/api/customers/whitelist-check |