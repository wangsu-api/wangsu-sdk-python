# Wangsu SDK for Python

This SDK provides Python interfaces to interact with Wangsu API services.

## Installation

Install the SDK using pip:

```bash
pip install wangsu-sdk-python
```

Install the SDK for a specific product category using pip:

```bash
pip install wangsu-sdk-python-ngreports
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
from wangsu.ngreports.models import *

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
| GetEdgeTrafficVolume | Get the edge traffic volume in megabytes during a time period. Query parameters let you specify the time period and scheme. Filter the results further by passing a filters object in the request. This report's data has a latency of less than two minutes.<br> | POST | /cdn/report/vol |
| GetEdgeRequests | Gets the number of requests to CDN Pro edge servers during a time period. Query parameters let you specify the time period and scheme. Filter the results further by passing a filters object in the request. This report's data has a latency of less than two minutes. | POST | /cdn/report/req |
| GetEdgeBandwidth | Get the bandwidth in Mbps to CDN Pro edge servers during a time period. Query parameters let you specify the time period and scheme. Filter the results further by passing a filters object in the request. This report's data has a latency of less than two minutes.<br> | POST | /cdn/report/bandwidth |
| GetOriginFastRouteTrafficVolume | Return the traffic to your origin server that uses our <a href="/cdn/docs/edge-logic/supported-directives#origin_fast_route">fast route feature</a> to make the connections faster and more reliable. | POST | /cdn/report/fastOriginVol |
| GetASummaryOfRequests | GetASummaryOfRequests during a time period. You can filter and group results by hostnames or server groups. If you are a reseller, you can also filter and group by customerIds to distinguish your child customers' requests. | POST | /cdn/report/reqSummary |
| GetASummaryOfTrafficBandwidth | GetASummaryOfTrafficBandwidth during a time period. You can filter and group results by hostnames or server groups. If you are a reseller, you can also filter and group by customerIds to distinguish your child customers' traffic. | POST | /cdn/report/bandwidthSummary |
| GetOriginTrafficVolume | Gets the origin traffic volume in megabytes during a time period. Query parameters let you specify the time period and scheme. Filter the results further by passing a filters object in the request. This report's data has a latency of less than two minutes.<br><br>Note: The overhead of TCP, IP, and MAC headers is not included in this API's results. | POST | /cdn/report/volOrigin |
| GetEdgeStatusCodeDetails | Gets details about HTTP status codes returned by requests to CDN Pro edge servers during a time period. Query parameters let you specify the time period, scheme, and granularity so you can monitor changes during the period. Filter the results further by passing a filters object in the request. This report's data has a latency of up to thirty minutes. | POST | /cdn/report/statusCodeDetails |
| GetTheNumberOfRequestsToOrigin | Get the number of requests to your origin servers during a time period. Query parameters let you specify the time period and scheme. Filter the results further by passing a filters object in the request. This report's data has a latency of less than two minutes. | POST | /cdn/report/reqOrigin |
| GetOriginStatusCodeDetails | Gets details about HTTP status codes returned by requests to your origin servers during a time period. Query parameters let you specify the time period, scheme, and granularity so you can monitor changes during the period. Filter the results further by passing a filters object in the request. This report's data has a latency of up to thirty minutes. | POST | /cdn/report/statusCodeDetailsOrigin |
| GetTheIntermediateTrafficVolume | GetTheIntermediateTrafficVolume in megabytes during a time period. Intermediate traffic is traffic between CDN Pro servers. Query parameters let you specify the time period and scheme. Filter the results further by passing a filters object in the request. This report's data has a latency of less than two minutes.<br> | POST | /cdn/report/volInterm |
| GetTheEdgeUploadTrafficVolume | Gets the traffic volume in megabytes uploaded to edge servers during a time period. Query parameters let you specify the time period and scheme. Filter the results further by passing a filters object in the request. This report's data has a latency of less than two minutes.<br><br>Note: The overhead of TCP, IP, and MAC headers is not included in this API's results. | POST | /cdn/report/upVol |
| GetASummaryOfStatusCodesReturnedByEdgeServers | Gets a summary of HTTP status codes returned by requests to the CDN Pro edge servers during a time period. Query parameters let you specify the time period and scheme. Filter the results further by passing a filters object in the request. This report's data has a latency of up to thirty minutes. | POST | /cdn/report/edgeStatusSummary |
| GetASummaryOfStatusCodesReturnedByOriginServers | Gets a summary of HTTP status codes returned by requests to your origin servers during a time period. Query parameters let you specify the time period and scheme. Filter the results further by passing a filters object in the request. This report's data has a latency of up to thirty minutes. | POST | /cdn/report/originStatusSummary |
| GetASummaryOfCpuUsage | Obtain a summary of CPU usage by edge and intermediate servers. | POST | /cdn/report/cpuSummary |
| GetOriginFastRouteRequests | Return the number of requests to your origin server that uses our <a href="/cdn/docs/edge-logic/supported-directives#origin_fast_route">fast route feature</a> to make the connections faster and more reliable. | POST | /cdn/report/fastOriginReq |
| GetEdgeHostnameSummaryStatistics | Obtain a summary of DNS requests for one or more edge hostnames during a time period. This API allows you to see the actual number of requests for each edge hostname. | POST | /cdn/report/edgeHostnameReqSummary |
| GetCpuTimeUsed | Get the amount of CPU time in seconds used to handle requests for your content. | POST | /cdn/report/cpuTime |
| GetASummaryOfTrafficVolume | Get a summary of edge, intermediate (between CDN Pro servers), and origin traffic volume during a time period. You can filter and group results by hostnames or server groups. If you are a reseller, you can also filter and group by customerIds to distinguish your child customers' traffic.<br> | POST | /cdn/report/volSummary |
| Getedgehostnamestatistics | Get the number of DNS requests to resolve your edge hostnames during a time period. | POST | /cdn/report/edgeHostnameReq |