# Wangsu SDK for Python

This SDK provides Python interfaces to interact with Wangsu API services.

## Installation

Install the SDK using pip:

```bash
pip install wangsu-sdk-python
```

Install the SDK for a specific product category using pip:

```bash
pip install wangsu-sdk-python-productmanagement
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
from wangsu.productmanagement.models import *

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
| GetSystemConfiguration | This API returns system configuration settings including supported <a href="/cdn/docs/edge-logic/supported-directives">Edge Logic directives</a>, advanced Edge Logic directives, the default pricing for traffic, and nonstandard ports that can handle HTTP and HTTPS requests. Please note that your account may not have access to the advanced Edge Logic directives or features. Please contact our support team if you require access to a particular directive, feature, or port that is not listed. | GET | /cdn/systemConfigs |
| GetIpAddressesOfTheCdn | Get a list of IP addresses used by CDN Pro. If your property's origin configuration uses the directConnection setting 'noDirect', and its Edge Logic does not use the origin_fast_route directive, you can restrict access to your origin servers by updating your allow lists with these IP addresses. Since the CDN's IP addresses can periodically change, we recommend that you check once a day and update your allow lists. | GET | /cdn/publicIpList |
| GetAListOfOriginShields | Get a list of shields that can be used as an extra layer between the CDN Pro edge servers and your origin servers. A shield can further reduce the number of requests to your origin and limit the requests to a smaller set of servers. <br>This is an advanced feature. If you require this feature, please contact our support team. | GET | /cdn/shields |
| GetAShieldByItsId | Obtain information about a shield which can be used as an extra layer between the CDN Pro edge servers and your origin servers. This is an advanced feature. If you require this feature, please contact our support team. | GET | /cdn/shields/* |
| CheckIfIpAddressesBelongToTheCdnProPlatform | This API allows you to check whether one or more IP addresses belong to the CDN Pro platform. | POST | /ngadmin/ipDetails |
| GetOriginFastRouteIpList | This API returns a list of IP addresses used by our origin fast route servers. If you use our origin_fast_route feature to make the connections faster and more reliable and wish to restrict access to your origin servers, add these IP addresses to your allow lists.<br> | GET | /cdn/originFastRouteIpList |
| GetStagingServersList | This API returns a list of IP addresses of servers that can be used to test deployments of properties and certificates to 'staging'. We recommend deploying to 'staging' and testing before deploying to 'production'. | GET | /cdn/stagingServers |