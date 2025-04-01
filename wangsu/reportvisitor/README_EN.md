# Wangsu SDK for Python

This SDK provides Python interfaces to interact with Wangsu API services.

## Installation

Install the SDK using pip:

```bash
pip install wangsu-sdk-python
```

Install the SDK for a specific product category using pip:

```bash
pip install wangsu-sdk-python-reportvisitor
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
from wangsu.reportvisitor.models import *

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
| Querytotalnumberofuniqueipundersingledomain | This interface is used to query the number of independent IP addresses for each stream name within a single domain name. The user provides a specific domain name and time to obtain information about the specified stream during this period (in days). The results returned by the interface include statistics on independent IP addresses for the domain name and its corresponding stream name. This helps users understand the distribution of visitors to each stream, thereby optimizing traffic configuration or evaluating the use of streaming media services. | POST | /api/report/visitor/total/stream |
| Reportuvispprovinceservice | Query unique visitor IPs for multiple domains by province and ISP. Users can specify time range, domain, province, ISP, and choose grouping by domain, province, or ISP. Results aid in analyzing access trends and optimizing content distribution. Supports Accept-Language (zh-CN, en-US), default is zh-CN. With en-US, province and ISP are in codes; otherwise, in Chinese. | POST | /api/report/uv/isp-province |
| Reportiptopdetailsservice | Query 5 minute details of multiple domain names. TOP IP | POST | /api/report/ip/top-details |
| Reportreferrertopdetailsservice | This interface is used to query the top visitor source details of a domain name every 5 minutes. The user needs to provide the domain name and time range, and the returned content includes detailed data of each referral source. The optional values include traffic, bandwidth, and number of requests. This interface helps users analyze site traffic and make corresponding business decisions. | POST | /api/report/referrer/top-details |
| Reporturltopdetailsservice | This interface is used to count the top URL information of multiple domain names within 5 minutes. The user needs to provide the time range and domain name. The returned content includes the traffic, bandwidth or number of requests of the top URL of the domain name. It helps users understand the popular access links and optimize resource allocation. | POST | /api/report/url/top-details |
| Reportvisitorcustomtopdailyservice | Reportvisitorcustomtopdailyservice | POST | /api/report/visitor/custom-top/daily |