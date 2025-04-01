# Wangsu SDK for Python

This SDK provides Python interfaces to interact with Wangsu API services.

## Installation

Install the SDK using pip:

```bash
pip install wangsu-sdk-python
```

Install the SDK for a specific product category using pip:

```bash
pip install wangsu-sdk-python-reportrequest
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
from wangsu.reportrequest.models import *

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
| Querydomaintotalrequest | This interface is used to query the total number of requests for multiple domain names. Users provide information such as time and domain name, and the interface will return the number of requests in each time segment, supporting data of different granularities (such as data every five minutes, every hour, or every day). This interface helps users monitor website access and follow up and optimize abnormal situations in a timely manner. | POST | /api/report/domainhit |
| Reportrequestispprovinceservice | Query the number of requests and QPS of multiple domains of each ISP in each province.<br>Data latency is around 5-15 minutes.<br>Support language request header Accept Language, only support zh-CN and en-US, default to zh-CN. Accept Language: en-US, both the province and isp input and return are in code, otherwise the return is in Chinese. | POST | /api/report/request/isp-province |
| Reportrequesthitrateispprovinceservice | This interface allows users to query the hit rate of the number of requests for a domain name in different operators and provinces, and supports returning Chinese or English data based on the request header Accept-Language. Users need to provide parameters such as time range and domain name to obtain data in different time dimensions. The returned content includes the hit rate of the number of requests for each domain name in different operators and provinces. It helps users analyze the distribution of network requests. | POST | /api/report/request/hit-rate/isp-province |
| Queryrequestnumbersundershieldpop | This interface is used to query the number of requests for multiple domain names on the parent node. The user provides the query time range and domain name list, and can choose whether to group the output by domain name. The returned results include the total number of requests, the peak number of requests, and the number of requests every 5 minutes. This interface is helpful for users who need to analyze the number of visits to the domain name on the parent node to adjust the cache strategy. | POST | /api/report/request/parent-node |
| Queryrequestbyspecificprotocol | This interface is used to count the number of requests for a specified transport protocol on edge nodes for multiple domain names. Users need to provide a query time range and a domain name list, and select a protocol type. The returned content includes the number of requests for each domain name with a specified protocol. This interface helps users monitor and analyze traffic under different transport protocols to optimize network performance and improve service quality. | POST | /api/report/request/protocol |
| Queryipv6requestofeachispandprovince | According to the visitor visit log, query request numberof domain in each ISP each province different IP type.<br>Support language request header Accept Language, only support zh-CN and en-US, default to zh-CN. Accept Language: en-US, both the province and isp input and return are in code, otherwise the return is in Chinese. | POST | /api/report/request/isp-province/ipv6 |
| Reporthitservice | This interface is used to query the request count summary information of all accelerated domain names under the account. Users can obtain the total number of requests in a specified time period and detailed data on the number of requests in each time segment by calling this interface. By using this interface, users can easily monitor and analyze the number of requests for domain names in different time periods to optimize resource allocation and improve performance. | GET | /api/report/hit |
| Queryrequesthitratio | Query minute-level request cache hit ratios for a specified period. Provide start time, end time, and domain to get data. Granularity options are 1 minute, 5 minutes, 1 hour, or 1 day. It returns cache hit ratios for each minute, helping evaluate domain cache performance on the CDN. | POST | /api/report/request/hit-ratio/total |
| Reportstreamtasknumberservice | This interface is used to query the number of live transcoding tasks within a specified time period. Users need to provide the query time range and domain name to obtain detailed data of transcoding tasks. The interface returns content including the encoding format used, the number of transcodings, the duration of each transcoding, etc. This interface helps users monitor the number and efficiency of live transcoding tasks, thereby optimizing the resource allocation and performance improvement of live service. | POST | /api/report/stream/task-number |
| Hit | Query the number of requests and output the number of requests data at a minute granularity. | POST | /myview/Hit |
| Dispatchdomainareatimereport | Get the amount of scheduled domain name resolution | POST | /clouddns/Dispatchdomainareatimereport |
| Policydetailreport | Get scheduling report | POST | /clouddns/Policydetailreport |
| Reportrequesthttphttpsservice | Query the requests of HTTP and HTTPS per minute for multiple domain in a specified time period. The user enters the start and end time and the domain, and the returned data can be grouped or merged by domain name. The interface will return the number of HTTP and HTTPS requests per minute for the domain. | POST | /api/report/request/http/https |
| Reportrequestquicservice | This interface is used to query the number of QUIC requests and the total number of requests for multiple domain names. Users need to provide the start time, end time, and domain name list to obtain data. The data returned by the interface includes the number of QUIC requests and the total number of requests for each timestamp. It helps users analyze the usage of QUIC and adjust strategies to improve the response speed and user experience of the website. | POST | /api/report/request/quic |
| Reportuserrequestispprovinceservice | This interface is used to query the number of requests for multiple domain names in various provinces and operators in mainland China. It supports returning Chinese or English data based on the request header Accept-Language. Users need to provide the domain name and query time range, and can specify ISPs and provinces for detailed analysis. The returned results include the number of requests for each domain name in each province and ISP and the total number. It helps users analyze the distribution of regional and operator requests, optimize traffic management, and improve service efficiency. | POST | /api/report/domain/request/isp-province |
| Reportuserrequestcountryservice | Query the number of requests for multiple domain names in each country and region. (Statistics by visitor IP) | POST | /api/report/request/country |
| Reportprotocolrequestservice | This interface is used to query the number of requests for multiple domain names grouped by protocol within a specific time period. The user needs to provide the query time range, domain name, and data query granularity (such as 1 minute, 5 minutes, 1 hour, 1 day). The returned results include the total number of requests for each domain name in each time slice, as well as the number of requests for the corresponding protocols of HTTP and HTTPS. It helps users analyze the request status under different protocols and provide data support for website performance optimization and traffic analysis. | POST | /api/report/protocol/request |
| Reportprotocoloriginrequestservice | This interface is used to query the number of back-to-source requests for multiple domain names according to the protocol. Users can query by specifying the time range and domain name. The returned content includes the number of back-to-source requests for each domain name in each time slice and different protocols. It helps users analyze network access and back-to-source data traffic, thereby optimizing website performance and resource allocation. | POST | /api/report/protocol/origin/request |
| Reportminuteuserrequestispprovinceservice | Query the number of requests for multiple domain names in each ISP and each province, including only Chinese user informatio | POST | /api/minute/report/domain/request/isp-province |
| Queryedgerequesthitratioservice | Query the hit rate of cache requests at the edge node for multiple domains at the minute level | POST | /api/report/request/edge-hit-ratio/total |