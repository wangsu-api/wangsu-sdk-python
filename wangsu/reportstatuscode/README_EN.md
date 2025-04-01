# Wangsu SDK for Python

This SDK provides Python interfaces to interact with Wangsu API services.

## Installation

Install the SDK using pip:

```bash
pip install wangsu-sdk-python
```

Install the SDK for a specific product category using pip:

```bash
pip install wangsu-sdk-python-reportstatuscode
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
from wangsu.reportstatuscode.models import *

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
| Querystatuscodedistributionofeachispandprovince | Query the status code distribution for multiple domains across various ISPs and provinces. Users provide a time range and a list of domains, with optional selection of ISP and province. Results display the status code distribution by domain, ISP, and province, supporting queries at 1-minute/5-minute/1-hour granularity. The API supports the `Accept-Language` request header, with `zh-CN` and `en-US` as the only options; `zh-CN` is the default. When `en-US` is selected, provinces and ISPs are shown in code, otherwise in Chinese. | POST | /api/report/status-code/isp-province |
| Querystatuscodedistribution | This interface is used to count the edge status code data of multiple domain names. Users can select the query time range and domain name list to obtain data. The returned content includes the status code distribution of each domain name and its corresponding number of requests. It helps users analyze the domain name access status and optimize content distribution strategies. | POST | /api/report/status-code |
| Queryoriginstatuscodedistribution | Statistics of the distribution of origin status codes of multiple domains, and the statistics contain the origin data of all nodes. Around 5-15 minutes of data delay. It's recommended that the call frequency is no higher than 30/5min. | POST | /api/report/status-code/origin |
| Reportstatuscodenodeoriginservice | Query the back to origin status code distribution for multiple domains at CDN nodes. Users specify a time range and domain list, with an option to return results by domain. It provides status codes and request counts for each time slice, useful for monitoring origin requests from edge nodes. Data latency is 5 to 15 minutes. | POST | /api/report/status-code/node/origin |
| Reportstatuscoderealtimeoriginservice | This interface is used to query the minute-level edge-only back-to-source status code information of a domain name. The user needs to provide the query time range and domain name list, and the returned content includes the number of requests and timestamps for each status code. It helps users monitor website availability and optimize service quality. | POST | /api/report/status-code/real-time/origin |
| Queryipv6statusofeachispandprovince | Query IPV6 status codes for multiple domains across provinces and ISPs. Users can specify domains, provinces, ISPs, and IP protocol types, with time granularity of 5 minutes or 1 hour. It returns status codes and request counts for each domain by province and ISP, aiding in monitoring website access conditions by IP protocol.<br>Supports the Accept-Language header with "zh-CN" and "en-US" options; default is "zh-CN". When set to "en-US", provinces and operators use codes for input and output; otherwise, they are in Chinese. | POST | /api/report/statusCode/isp-province/ipv6 |
| Reportstatusallservice | This interface is used to query the status code summary distribution of all domain names under an account. The user provides a query time range to obtain the number of requests corresponding to each status code of all domain names under the account. This helps users understand the overall access status of all businesses. | GET | /api/report/status-code |
| Reportstatuscodeoriginfailrateservice | The function of this interface is to provide data on the number of back-to-origin requests and error rates at the minute level. Users need to provide the time range, domain name, and data granularity to obtain the total number of back-to-origin requests, the number of failed requests, and their failure rates per minute. This helps users monitor website performance, thereby improving service quality and user experience. | POST | /api/report/status-code/origin/fail-rate |
| Queryrealtimeoriginstatuscode | This interface is used to query the back-to-origin request status code every minute within a specified time range. Users need to provide a time interval and a domain name list, and can select query dimensions, such as specific status codes or status code types (success, redirection, server error, etc.). The returned data includes detailed information on the request time and total number of requests. This interface is used to monitor the health status of the website, optimize the response of the origin station, and help analyze and adjust the network architecture to improve service stability and visitor experience. | POST | /api/report/status-code/real-time/origin/total |
| Queryispprovincestatuscode | Querying the minutes-level status code summary of the provincial ISP.<br>Support language request header Accept Language, only support zh-CN and en-US, default to zh-CN. Accept Language: en-US, both the province and isp input and return are in code, otherwise the return is in Chinese. | POST | /api/report/status-code/isp-province/total |
| Reportstatuscoderealtimeedgeservice | Query minute-level data of edge status codes. Users can specify the start time, end time, and domain name to query the request count data corresponding to the status codes. The data granularity can be selected as either 1 minute or 5 minutes in the request. The return result includes the number of requests per minute for each status code. | POST | /api/report/status-code/real-time/edge |
| Reportflvstatuscoderealtimeorigintotalservice | Query minute granularity FLV back-to-source status code | POST | /api/report/flv/status-code/real-time/origin/total |
| Reportflowprotocolstatuscodeservice | Query the number of HTTP and HTTPS requests for each status code for multiple domain every 5 minutes within a specified time period. The user enters the start and end time and the domain, and the API will return the requests of HTTP and HTTPS for each status code of the domain every 5 minutes. | POST | /api/report/status-code/protocol-version |
| Reportflowipversionstatuscodeservice | This interface is used to query the IPv6 and IPv4 status code data of multiple domain names at a granularity of 5 minutes. The user needs to provide the query time range and domain name list to obtain the data. The return content includes detailed data of IPv4 and IPv6 for each status code under the domain name. This interface helps users monitor and analyze the status code distribution under different IP protocols to optimize network performance and improve service quality. | POST | /api/report/status-code/ip-version |
| Reportflowprotocoloneminstatuscodeservice | Query HTTP and HTTPS status code data of multiple domain with 1-minute granularity. The user specifies the time range and domain to obtain status code statistics. The returned results include a list of status codes for each domain and the number of HTTP and HTTPS status code requests corresponding to each time slice. It supports querying data for up to 180 days, with a data delay of about 5 minutes. | POST | /api/report/one-min/status-code/protocol-version |
| Reportstatuscodelogservice | Query the hourly granular status code distribution of multiple domain names | POST | /api/report/status-code/log |
| Querystatuscodedistributionincountries | Query status code distribution by country granularity (Statistics by CDN IP) | POST | /api/report/status-code/country |
| Querystatuscodedistributionofeachispandprovincebyuserip | Query of the traffic of multiple domains of each ISP in each province, Province and ISP are based on visitor IP ownership. | POST | /api/report/status-code/isp-province/user-ip |
| Reportstatuscodeurltopservice | Used to query the ranking of TOP URLs under domain names and status codes. Data latency: 3 hour. | POST | /api/report/domain/statuscode/url/top |