# Wangsu SDK for Python

This SDK provides Python interfaces to interact with Wangsu API services.

## Installation

Install the SDK using pip:

```bash
pip install wangsu-sdk-python
```

Install the SDK for a specific product category using pip:

```bash
pip install wangsu-sdk-python-reporturl
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
from wangsu.reporturl.models import *

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
| Querytoprankingurl | This interface is used to count the number of URL requests and traffic of a domain name within each hour, and generate a ranking list of up to TOP500. Users need to provide the time return and domain name to obtain the total number of URL requests, total traffic, number of hit requests, number of failed requests, and details of different status codes. The interface supports sorting by total number of requests or total traffic to quickly identify high-frequency access or high-traffic URLs. This interface helps users monitor URL access frequency and traffic to adjust corresponding network policies. | POST | /api/report/url/top |
| Reporturloriginservice | Query URL information for Back-to-origin requests across multiple domains. By providing a list of domains and a time range, users can obtain URLs with Back-to-origin requests and the request count for each domain. It's useful for monitoring and analyzing these requests. | POST | /api/report/url/origin |
| Reporturlcustomtopdailyservice | Query the URL ranking for specified domains within a given time range. Users can specify the ranking criteria by either traffic or request count, with the default being sorted by request count. The API returns data that includes the ranking of each URL, the respective URL, the total traffic, and the total request count for each URL, assisting users in identifying URLs with concentrated traffic and request volumes. | POST | /api/report/url/custom-top/daily |
| Reportdomainrefererurlservice | This interface is used to query the URL source rankings of multiple domain names, It only supports data query in the East 8th District. Users can set the query time range and domain name list to obtain the corresponding ranking information. The interface will return the top 10 URL sources ranked by the number of requests or traffic value, and a maximum of the top 200 can be queried. This helps users identify URL source addresses with high traffic or high request counts for data analysis and performance optimization. | POST | /api/report/domain/referer-url |
| Reportdomainrefererwebsiteservice | Query the website referer ranking of multiple domains | POST | /api/report/domain/referer-website |