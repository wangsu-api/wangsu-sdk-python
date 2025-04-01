# Wangsu SDK for Python

This SDK provides Python interfaces to interact with Wangsu API services.

## Installation

Install the SDK using pip:

```bash
pip install wangsu-sdk-python
```

Install the SDK for a specific product category using pip:

```bash
pip install wangsu-sdk-python-reportbandwidth
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
from wangsu.reportbandwidth.models import *

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
| Queryp2pbandwidth | Query CDN bandwidth, P2P bandwidth, total bandwidth and billing value | POST | /myview/BandWidthP2p |
| Bandwidthchannelprotocol | Query the bandwidth of different protocals. | POST | /myview/Bandwidthchannelprotocol |
| Channelvaluesum | Query the sum of charge values group by channels' charge method. | POST | /myview/Channelvaluesum |
| Bandwidthmiddle | Query the bandwidth of middle cache. | POST | /myview/bandwidth-middle |
| Querydomainbandwidth | This interface is used to collect statistics on bandwidth summary information of multiple domain names within a specified time. Users need to provide acceleration domain names and time parameters to generate summary data, and the returned content includes bandwidth summary data for each time slice. This interface helps users monitor and analyze the traffic usage of domain names to better optimize the network and control costs. | POST | /api/report/domainbandwidth |
| Billingorder | Query customer's formal order billing information, including billing method description, billing value, details, etc. | POST | /myview/Billingorder |
| Queryipv6bandwidthofeachispandprovince | According to the visitor visit log, query bandwidth of domain in each ISP each province different IP type.<br>Support language request header Accept Language, only support zh-CN and en-US, default to zh-CN. Accept Language: en-US, both the province and isp input and return are in code, otherwise the return is in Chinese. | POST | /api/report/bandwidth/isp-province/ipv6 |
| Getbandwidthlog | Query the log bandwidth. | POST | /myview/bandwidth-log |
| Bandwidthpeakranking | Rank the channel in the order of bandwidth's  peak value. | POST | /myview/bandwidth-peak-ranking |
| Bandwidthchannel | Query the channels' bandwidth. | POST | /myview/bandwidth-channel |
| Reportbandwidthrealtimeedgeservice | This interface is used to query the edge bandwidth summary data of multiple domain names at minute granularity. The user needs to provide the start time, end time, domain name list and desired data granularity. The interface returns information including the edge bandwidth value per minute, peak time, peak bandwidth and total traffic. The interface is helpful for users to monitor and analyze the bandwidth and traffic fluctuations of multiple domain names, so as to optimize the use of bandwidth resources and adjust network policies. | POST | /api/report/bandwidth/real-time/edge |
| Querybandwidthbyispprovince | This interface is used to query the bandwidth information of visitor IPs in various provinces and ISPs in mainland China. Users can specify parameters such as time period, domain name, region, and ISP to obtain bandwidth data with a granularity of 5 minutes in Mbps. The interface returns a timestamp and the corresponding bandwidth value to help users analyze the bandwidth usage of different regions and ISPs, thereby optimizing network resource allocation and improving user experience. | POST | /api/report/bandwidth/area/isp-province |
| Querybandwidthoforiginminutely | Query minute-level back-to-origin bandwidth for multiple domains. Users must provide start and end times, domain(s), and data granularity.The results include bandwidth peak, total back-to-origin traffic, and per-minute back-to-origin bandwidth for each domain. | POST | /api/report/bandwidth/multi-domain/real-time/origin |
| Querybandwidthminutely | Query real-time bandwidth for multiple domains at the minute level. Users provide a time span and domain list, with a maximum query range of 30 minutes. It returns peak bandwidth and per-minute values, ideal for detailed real-time bandwidth monitoring of different domains. | POST | /api/report/bandwidth/multi-domain/real-time |
| Querycpsbandwidth | The channels' bandwidth of  dedicated line | POST | /myview/bandwidth-HK |
| Bandwidthvm | Query the channels' bandwidth and the charge info | POST | /api/bandwidth-vm |
| Queryrealtimebandwidthformultidomain | This interface is used to query the minute-level edge bandwidth of a domain name. Users need to provide a time range and domain name to obtain detailed bandwidth usage data. The returned content includes the total traffic of each domain name, minute-level bandwidth data, and bandwidth peak, etc. It helps users analyze the traffic of websites or applications, thereby optimizing resource management and improving performance. | POST | /api/report/bandwidth/multi-domain/real-time/edge |
| Reportlogflowispprovinceservice | This interface is used to query the log bandwidth and traffic data of multiple domain names in different ISPs and provinces. The return results in Chinese or English can be obtained according to the request header Accept-Language. Users need to provide the query time range, domain name, province, and ISP to obtain data. The return results include the bandwidth and traffic of each domain name in each ISP and province. This interface helps users analyze network performance and traffic distribution to optimize resource allocation and improve service quality. | POST | /api/report/flow/log/isp-province |
| Reportbandwidthwildcarddomainservice | Query Wildcard Domain Bandwidth | POST | /api/report/bandwidth/wildcard-domain |
| Reportp2pbandwidthdomainservice | This interface is used to query the detailed domain name P2P bandwidth data of real accelerated domain names (including wildcard domain names and real domain names that are not wildcard domain names). Users need to provide the query time and relevant domain name information to obtain the results. The returned data includes the CDN bandwidth, P2P bandwidth, and IPv6 bandwidth in P2P bandwidth of each detailed domain name, all displayed in Mbps. It helps users monitor and manage the network environment of domain names, analyze network traffic, and optimize domain name resources. | POST | /api/report/p2p/bandwidth |
| Bandwidthtotal | Query total traffic of channels | POST | /myview/bandwidth-total |
| Reportlowdelaycountrybandwidthservice | Query bandwidth data for specified domains in different countries over a specific time period. It supports queries for selected countries and regions, returning bandwidth values for each domain at corresponding times in various countries. Ideal for monitoring and analyzing bandwidth conditions with low data latency across regions. | POST | /api/report/low-delay/country-bandwidth |
| Perzonebilling | Query the perzone data | POST | /myview/perzone-billing |
| Reportcountryserverbandwidthservice | This interface is used to query the bandwidth details of the country to which the server IP belongs. The user needs to provide the time range, domain name, country code, and data granularity. The return content includes the edge traffic and bandwidth values at each time point in the specified time period. This interface helps users understand the current service traffic distribution and usage in different countries around the world. | POST | /api/report/server/country-bandwidth |
| Reportipv6bandwidthservice | This interface is used to query the IPV6 bandwidth and traffic data of multiple domain names. The user provides the time range and domain name to obtain the corresponding data. The returned content includes the detailed traffic (in MB) and bandwidth (in Mbps) of each domain name. It helps users to monitor traffic and bandwidth separately, optimize network resources in time and detect abnormal traffic. | POST | /api/report/ipv6-bandwidth |
| Reportlogbandwidthmultidomainecdnedgeservice | Query the minute-level log bandwidth details of ECDN nodes for multiple domain. Users need to provide the start time and end time, can specify the domain and region to query, and can choose whether to group the query results by domain dimension. The interface returns the total edge Traffic, bandwidth peak value and peak value time of the ECDN node of the domain , as well as detailed bandwidth data with a granularity of five minutes. | POST | /api/report/bandwidth/multi-domain/log/ecdnedge |
| Bandwidthecdn | Query the cust's ecdn bandwidth | POST | /myview/Bandwidthecdn |
| Bandwidthlogecdn | Query the cust's ecdn log bandwidth | POST | /myview/Bandwidthlogecdn |
| Wsiinfo | Query the information of the whole site isolation, including: the average number of domain names, bandwidth, and number of requests | POST | /myview/Wsiinfo |
| Reportp2sporiginbandwidthwildcarddomainservice | This interface is used to query the on-demand P2SP back-to-source bandwidth data under a specific wildcard domain name. Users can obtain specific back-to-source bandwidth information by providing the query time range and the specified wildcard domain name. The returned data includes the back-to-source bandwidth and bandwidth value for each wildcard domain name and its detailed domain name in each time slice. It helps users monitor and analyze the bandwidth usage of different domain names in a specified time period, thereby optimizing bandwidth resources and improving service quality. | POST | /api/report/p2sp/wildcard-origin-bandwidth |
| Reportdirbandwidthinfoservice | Query the bandwidth and flow details of multi-level directories under the domains. | POST | /api/report/flow-bandwidth/dir/info |
| Reportdomainoriginresponsetimeservice | This interface is used to query the back-to-origin response time of a specific domain name. Users can obtain the corresponding data by providing the domain name, start time, and end time. The returned information includes the response time data of each domain name per minute, in milliseconds, accurate to two decimal places. This interface is crucial for understanding the back-to-origin performance of the website. Users can optimize performance and troubleshoot problems based on the query results. | POST | /api/report/origin/response-time |
| Reportbandwidthrequestbyipispprovince | This API is used to query IPv6/IPv4 bandwidth or request counts for provinces and ISPs based on visitors' IPs for multiple domains within a specified time range. Provide the time range and domain to query. You can group results by domain, province, or ISP and get data at 1-minute or 5-minute intervals. The response shows the bandwidth or request counts for each domain, province, and ISP. | POST | /api/report/bandwidth-request/isp-province/multi-ip-version |