# Wangsu SDK for Python

This SDK provides Python interfaces to interact with Wangsu API services.

## Installation

Install the SDK using pip:

```bash
pip install wangsu-sdk-python
```

Install the SDK for a specific product category using pip:

```bash
pip install wangsu-sdk-python-logdownload
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
from wangsu.logdownload.models import *

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
| Querydomainlogdownloadaddress | Report Log Multi-Domain Service Interface description Query the log download address of multiple domains. <br>The default granularity of log file is 24 hours and data are returned according to the actual configurations.<br>Around 3-5 hours of data delay | POST | /api/report/log/downloadLink |
| Querytranscodingdurationlogdownloadaddress | This interface is used to provide the download address of the transcoding duration log file of multiple domain names. Users can obtain the transcoding log information related to each domain name by specifying the time range and domain name list. The returned content includes the start and end time of the log file, download address, file name, file size, and expiration time of the download address. This interface helps users accurately grasp the transcoding details of each domain name within the specified time and make corresponding optimizations. | POST | /api/report/log/download-file/transcoding |