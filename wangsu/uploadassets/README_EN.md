# Wangsu SDK for Python

This SDK provides Python interfaces to interact with Wangsu API services.

## Installation

Install the SDK using pip:

```bash
pip install wangsu-sdk-python
```

Install the SDK for a specific product category using pip:

```bash
pip install wangsu-sdk-python-uploadassets
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
from wangsu.uploadassets.models import *

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
| Getuploadtoken | Invoke getUploadToken to obtain the video file upload address and credentials | POST | /vod/videoManage/getUploadToken |
| Getaudiouploadtoken | You can invoke getAudioUploadToken to obtain audio file upload addresses and credentials. You can obtain a maximum of 50 audio file upload addresses and credentials in batches. | GET | /vod/audioManage/getAudioUploadToken |
| Getmaterialuploadtoken | Call getMaterialUploadToken to obtain the upload address and credentials of materials. You can batch obtain a maximum of 50 material addresses and credentials. | POST | /vod/material/getMaterialUploadToken |
| Pullvideo | Call pullVideo to set the url of the video to be pulled to the background. The background automatically pulls and saves url videos from third-party platforms. You can set pull tasks in batches. | POST | /vod/videoManage/pullVideo |
| Pullvideoquery | You can query the completion of pullVideoQuery. | POST | /vod/videoManage/pullVideoQuery |