# Wangsu SDK for Python

This SDK provides Python interfaces to interact with Wangsu API services.

## Installation

Install the SDK using pip:

```bash
pip install wangsu-sdk-python
```

Install the SDK for a specific product category using pip:

```bash
pip install wangsu-sdk-python-reportflow
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
from wangsu.reportflow.models import *

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
| Querydirectorybandwidthtrafficunderlivestreamdomain | Query traffic or bandwidth statistics for each directory under the live push and pull streaming domains. Users need to provide the start and end time, domain name, and can specify a directory for querying. By default, the data is aggregated every 5 minutes. The returned results include the total traffic or bandwidth peak for each directory, along with detailed data for each time segment. | POST | /api/report/flow/dir/detail |
| Reportflowdirinfoservice | This interface is used to query the bandwidth and total traffic of multiple directories under multiple domain names, mainly for web pages, downloads, and on-demand domain names, and is limited to the acceleration area in mainland China. Users need to provide the query time range and directory level information, and can query data for the past six months at most. The returned results include the total directory traffic and bandwidth peak for each domain name. This interface helps users analyze website traffic distribution and bandwidth usage, and helps optimize resource allocation and improve service performance. | POST | /api/report/flow/dir/info |
| Reportflowhitrateispprovinceservice | Query the Byte Hit Rate and Hit Traffic of Multiple Domains of Each ISP in Each Province. Around 5-15 minutes of data delay. It's recommended that the call frequency is no higher than 30/5min.<br>Support language request header Accept Language, only support zh-CN and en-US, default to zh-CN. Accept Language: en-US, both the province and isp input and return are in code, otherwise the return is in Chinese. | POST | /api/report/flow/hit-rate/isp-province |
| Querydomaintrafficunderspecificsettlementarea | Traffic summarized statistics by settlement area of an acceleration domain. Around 5-15 minutes of data delay. It's recommended that the call frequency is no higher than 30/5min. | POST | /api/report/flow/area |
| Querydomaintotaltraffic | This interface is used to obtain traffic summary information of multiple domain names. Users need to provide a time range and domain name, and the data granularity can be selected as five minutes, one hour, or one day. The returned content includes the total traffic and the traffic value of each time node. This interface helps users monitor and analyze the traffic of multiple domain names, so as to grasp the overall traffic trend and changes. | POST | /api/report/domainflow |
| Reportfloworiginispprovinceservice | This API provides back-to-origin traffic data for multiple domains by province and ISP, with a 5 to 15-minute data delay. Users can group queries by domain, ISP, and province, and specify time range and data granularity. Results include detailed traffic and bandwidth information to analyze regional and ISP performance. It supports `Accept-Language` header options: `zh-CN` (default) and `en-US`. With `en-US`, province and ISP data are encoded; otherwise, they are in Chinese. | POST | /api/report/flow/origin/isp-province |
| Querystreamtrafficundermalbdomain | This interface is used to query the traffic or bandwidth data of live streaming under a domain name within a specified time period. The user needs to provide the time range, domain name and stream name, as well as data type and granularity options. The interface returns the traffic or bandwidth details of each stream under each domain name, including total traffic and peak bandwidth. It helps users monitor live streaming traffic to optimize resource allocation. | POST | /api/report/flow/stream/detail |
| Reportflowexactdomainservice | This interface is used to query the traffic data of precise domain names, especially for the traffic analysis of specific domain names corresponding to wildcard domain names. Users need to provide the time range and domain name to obtain traffic data. The returned results include the traffic data of each precise domain name in different time slices. It helps users understand the traffic situation of domain names and helps optimize domain name configuration and network resources. Note that the data is delayed by 3 to 5 hours, and it is recommended to query the data 24 hours ago. | POST | /api/report/flow/exact-domain |
| Reportflowispprovincebyteservice | Query the traffic of multiple domain names in each ISP province (Byte).<br>Support language request header Accept Language, only support zh-CN and en-US, default to zh-CN. Accept Language: en-US, both the province and isp input and return are in code, otherwise the return is in Chinese. | POST | /api/report/flow/isp-province/byte |
| Reportfloworiginispprovincebyteservice | Query multiple domain names in all ISP provinces to return traffic.<br>Support language request header Accept Language, only support zh-CN and en-US, default to zh-CN. Accept Language: en-US, both the province and isp input and return are in code, otherwise the return is in Chinese. | POST | /api/report/flow/origin/isp-province/byte |
| Querytrafficrequestintotalandpeakvalue | This interface is used to query the traffic request count and peak bandwidth of multiple domain names. Users need to provide a time range and a domain name list to obtain the total traffic, total request count, peak bandwidth and its occurrence time of each domain name, as well as detailed traffic and request count for each time period. This helps users understand the access status of the website and effectively adjust strategies to meet different traffic requirements. | POST | /api/report/flow-request |
| Queryoutputtrafficundershieldpop | Query the downstream traffic data of the Relay node of multiple domain . Users can obtain detailed Traffic data reports by providing the start time, end time, and domain list. The return value includes the total Traffic of each domain and provides the Traffic value of each time slice. This interface is suitable for monitoring and analyzing the Traffic profile and change trend of CDN Relay node. It's recommended that the call frequency is no higher than 30/5min. | POST | /api/report/flow/parent-node |
| Querytrafficbyspecificprotocol | This API is used to query the Traffic data of multiple domain under the specified transmission protocol. The query is for the data of all Edge node. The user needs to specify the domain, start and end time, transmission protocol and other parameters, and can select the data granularity and grouping dimension. By default, the query will return the Traffic data of the HTTPS protocol, and the output result is the Traffic value of each domain at different time points. This interface is suitable for scenarios where you need to query and analyze the Traffic of multiple domain with different transmission protocols. | POST | /api/report/flow/protocol |
| Reportflowispprovinceservice | This interface is used to query the traffic and bandwidth data of multiple domain names in various operators and provinces. It supports returning Chinese or English data according to the request header Accept-Language. Users need to provide the query time range and domain name list, and can choose to group by ISP and province. The returned content includes the traffic and bandwidth data of each domain name in each province and operator. This interface helps users analyze network performance in different regions and operators, and helps optimize resource allocation and improve service quality. | POST | /api/report/flow/isp-province |
| Querybacktoorigintrafficandrequest | This interface is designed to query the back-to-source traffic and number of requests for multiple domain names. Users can obtain this data by entering information such as the start time, end time, and specified domain name. The interface returns the total traffic, total number of requests, request and bandwidth peaks for each domain name and their corresponding time points, and supports providing detailed traffic, request, and bandwidth data at a minute granularity. This feature helps users monitor and analyze website back-to-source traffic.<br>Limitation: Generally, data is delayed by 5 to 15 minutes. | POST | /api/report/flow-request/origin |
| Querysumuptrafficunderaccount | Query Traffic summary for all domains under a user account. Users specify start and end times to obtain detailed Traffic data, with granularity options of 5 minutes, 1 hour, or 1 day. This helps users analyze CDN Traffic usage for each domain within the specified period. | GET | /api/report/flow |
| Reportflowispprovincetotalservice | Querying the minutes-level traffic summary for provincial ISP.<br>Support language request header Accept Language, only support zh-CN and en-US, default to zh-CN. Accept Language: en-US, both the province and isp input and return are in code, otherwise the return is in Chinese. | POST | /api/report/flow/isp-province/total |
| Queryispprovincehitrate | Querying provincial ISP's rate of traffic hits and number of requests hit rates at the minute level.<br>Support language request header Accept Language, only support zh-CN and en-US, default to zh-CN. Accept Language: en-US, both the province and isp input and return are in code, otherwise the return is in Chinese. | POST | /api/report/flow/isp-province/hit-rate/total |
| Queryrequesbandwidthtsavingratio | Query bandwidth savings for a specified period. Users provide start and end times and the domain, with data available in five-minute, hourly, or daily granularity .The results include average total bandwidth savings and actual savings per time slice, ideal for monitoring and analyzing CDN cache hit savings. | POST | /api/report/request/saving-bandwidth/total |
| Querymultiplestreamtrafficandbandwidthunderthedomain | This interface is used to query the traffic and bandwidth information of live streams under multiple domain names within a specified time period. Users can enter the start time, end time, and domain name to obtain detailed data, including the total traffic of each stream under each domain name, peak bandwidth, traffic or bandwidth data at each time point, and (optional) the number of online users at a time point. This is suitable for monitoring live stream network performance and user interaction, optimizing network configuration and resource allocation through data analysis, and improving the quality of live broadcast services. | POST | /api/report/flow-bandwidth/stream/detail |
| Reportflowhitrateispprovincebyteservice | This interface is used to query the byte hit rate of multiple domain names in different operators and provinces. Users can specify the date range, domain name, operator and province, and support output of 5-minute or 1-hour granularity data. The returned results include the byte hit rate details of each domain name in each operator and province. Help users analyze the cache performance of websites in specific regions and operator environments. | POST | /api/report/flow/hit-rate/isp-province/byte |
| Reportflowdomaincountryservice | Query the traffic bandwidth distribution of a domain across countries and regions. Users input a time range and domain list to view data by domain, country, or domestic vs. foreign. Results include total regional traffic, its percentage, and traffic and bandwidth per time segment, aiding in global website traffic analysis and management. Query data from 24 hours prior is recommended. | POST | /api/report/flow/domain-country |
| Flowchannel | Query the minute granularity traffic value of the channel | POST | /myview/Flowchannel |
| Wctquery | Query the 5-minute granularity statistics of various types and gradients of customer on-demand transcoding | POST | /myview/Wctquery |
| Reportflowispprovincehitratedetailservice | This interface is used to query the minute-level traffic and request hit rate of the province and ISP dimensions, and supports returning Chinese or English information based on the request header Accept-Language. The user provides the time range, domain name, ISP, and province information. The returned results include the detailed traffic or request hit rate of the ISP in each province. It helps users analyze the network performance of each region, thereby optimizing content distribution strategies and improving network service quality. | POST | /api/report/flow/isp-province/hit-rate/detail |
| Reportflowrequestmultiipversionservice | Query the bandwidth/number of requests of multi-domain IPv6/IPv4 | POST | /api/report/flow-request/multi-ip-version |
| Reportflowp2pshareratioservice | Query the P2P share rate for multiple domains. Users provide a start time, end time, and domain list to get share rate data for each domain or aggregated statistics. Data can be returned in minute or five-minute granularity, including share rates for each time slice. It's ideal for monitoring and analyzing domain P2P usage efficiency. | POST | /api/report/flow/p2p/share-ratio |
| Flowday | Display channel traffic data by day, output date, peak time, peak bandwidth, total traffic. | POST | /myview/flow-day |
| Querydatatransferforalldomainbyte | ReportFlowAllForByteService | POST | /api/report/flow/byte |
| Reportflowispprovinceshorttimeservice | Query of the traffic of multiple domains of each ISP in each province, only supports queries with a short time span. | POST | /api/report/flow/isp-province/shorttime |
| Queryedgebytehitratioservice | Query the hit rate of cache traffic at the edge node for multiple domains at the minute level | POST | /api/report/flow/edge-hit-ratio/total |
| Reportupflowdomaincountryservice | Query the upload traffic bandwidth distribution of a domain across countries and regions. Users input a time range and domain list to view data by domain, country, or domestic vs. foreign. Results include total region traffic, its percentage, and traffic and bandwidth per time segment, aiding in global website traffic analysis and management. Query data from 24 hours prior is recommended. | POST | /api/report/up-flow/domain-country |