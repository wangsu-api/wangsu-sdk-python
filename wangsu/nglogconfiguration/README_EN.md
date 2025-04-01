# Wangsu SDK for Python

This SDK provides Python interfaces to interact with Wangsu API services.

## Installation

Install the SDK using pip:

```bash
pip install wangsu-sdk-python
```

Install the SDK for a specific product category using pip:

```bash
pip install wangsu-sdk-python-nglogconfiguration
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
from wangsu.nglogconfiguration.models import *

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
| GetAListOfLogConfigurations | Obtain a list of log configurations you have created. | GET | /cdn/report/logConfigs |
| CreateALogConfiguration | CreateALogConfiguration used to format the access logs for one or more hostnames. An applicable log configuration must exist for you to obtain logs for a hostname. It takes around 40 minutes for a newly created log configuration to take effect. | POST | /cdn/report/logConfigs |
| GetALogConfiguration | Retrieve a log configuration. | GET | /cdn/report/logConfigs/* |
| UpdateALogConfiguration | UpdateALogConfiguration's settings. It takes around 40 minutes for an updated configuration to take effect. | PATCH | /cdn/report/logConfigs/* |
| DeleteALogConfiguration | DeleteALogConfiguration. | DELETE | /cdn/report/logConfigs/* |
| GetAccessLogsForHostnames | Get access logs representing requests to one or more hostnames in your deployed properties. These logs contain data from requests made 2 or more hours earlier. By default, only logs within the past 14 days are available, and they are separated into files each covering part of a day.<br><br>To obtain logs for a hostname, you must first specify the format of the logs by creating a log configuration that applies to the hostname. Requests to your content made after the applicable log configuration has been created will be logged. Otherwise, no logs will be available for download.<br><br>For example, suppose you define a log configuration format as follows:<br>%cltip %rmtuser [%utctime] "%method %url %protocol" %statuscode %rspsize "%referer" "%ua" %rsptime<br><br>This API will return a list of available logs such as:<br>{<br>  "logs":[<br>          {<br>          "dateFrom":"2021-10-31T00:00:00Z",<br>          "dateTo":"2021-10-31T00:29:59Z",<br>          "fileSize":105878,<br>          "logUrl":"https://abc.example.com/logd/v2/download/0621c8fc885089805kea5f610797ff8ba92bc98c049c2bb308cbdb?traceId=ac6d696c657765625f74657374cf0000018dd01d89e8cd06d3",<br>          "hostname":"mydomain.domain.info"<br>          }<br>        ]<br>}<br><br>The logUrl field contains a URL to a gzip-compressed log file. The url will expire in 24 hours. Please call the API to fetch a new url if it expires. The log file consists of rows such as the following:<br>9.8.7.6 - [31/Oct/2021:19:59:57 +0000] "GET http://mydomain.domain.info/i/js/tab.js HTTP/1.1" 304 529 "http://mydomain.domain.info/?q=downloads" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36" 76<br><br> | POST | /cdn/report/logDownload |