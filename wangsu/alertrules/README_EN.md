# Wangsu SDK for Python

This SDK provides Python interfaces to interact with Wangsu API services.

## Installation

Install the SDK using pip:

```bash
pip install wangsu-sdk-python
```

Install the SDK for a specific product category using pip:

```bash
pip install wangsu-sdk-python-alertrules
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
from wangsu.alertrules.models import *

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
| Createcloudmonitorrealtimealarmrule | Create real-time monitoring alarm rules for cloud monitoring. Users can provide the monitoring rule name, monitored resource object, alarm trigger threshold, and alarm contact information to generate real-time monitoring rules. This is suitable for scenarios where timely attention to monitoring data changes of cloud products on the console is required. The interface for creating monitoring rules currently only supports some CDN monitoring items by domain name.  | POST | /api/cloudmonitor/alarm/real-time/add |
| Editcloudmonitorrealtimealarmrule | Edit the real-time monitoring alarm rules of Cloud monitoring. This interface modifies the rules in an overwrite manner. Users can pass in the monitoring rule ID, the name of the monitoring rule to be modified, the monitoring resource object, the alarm trigger condition threshold, the alarm contact person and other information to overwrite and modify the monitoring rule.<br><br>Interface management monitoring rules currently only support some monitoring items by domain. | POST | /api/cloudmonitor/alarm/real-time/edit |
| Querycloudmonitorrealtimealarmrule | Query the real-time monitoring alarm rules of Cloud monitoring. Users can enter the monitoring rule ID, query the monitoring rule name, monitoring resource object, alarm trigger condition threshold, alarm contact and other monitoring rule details.<br><br>Interface management monitoring rules currently only support some monitoring items by domain. | POST | /api/cloudmonitor/alarm/real-time/query |
| Deletecloudmonitorrealtimealarmrule | Delete the real-time monitoring alarm rule of Cloud monitoring. Users can pass in the monitoring rule ID to delete the specified monitoring rule. | POST | /api/cloudmonitor/alarm/real-time/delete |