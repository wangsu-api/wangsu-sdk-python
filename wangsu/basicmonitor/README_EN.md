# Wangsu SDK for Python

This SDK provides Python interfaces to interact with Wangsu API services.

## Installation

Install the SDK using pip:

```bash
pip install wangsu-sdk-python
```

Install the SDK for a specific product category using pip:

```bash
pip install wangsu-sdk-python-basicmonitor
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
from wangsu.basicmonitor.models import *

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
| Reportflowdomainispprovinceiaasservice | This interface is used to query the traffic data of edge servers in various ISPs and provinces, and supports returning Chinese or English data according to the request header Accept-Language. Users need to provide the query time range, domain name, ISP and province information, and the returned content includes the traffic details of each ISP and province, in MB, and displayed at a time granularity of 5 minutes. It is suitable for users who need to analyze the traffic distribution of different regions and operators to help optimize network resources and improve service efficiency. | POST | /api/report/flow/domain-isp-province/iaas |
| Vmpqueryservermetric | Query the CPU usage, memory usage, and bandwidth usage of the virtual machine instance in order to access its own monitoring system and control the operation of the virtual machine. Provide monitoring data queries for nearly 90 days, with a single query range of no more than 3 days and a data granularity of 5 minutes. If it is a bare metal instance, currently only bandwidth query is supported, and CPU and memory query is not supported. | GET | /vmp/servers/metric |