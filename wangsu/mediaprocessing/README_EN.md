# Wangsu SDK for Python

This SDK provides Python interfaces to interact with Wangsu API services.

## Installation

Install the SDK using pip:

```bash
pip install wangsu-sdk-python
```

Install the SDK for a specific product category using pip:

```bash
pip install wangsu-sdk-python-mediaprocessing
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
from wangsu.mediaprocessing.models import *

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
| Videoclip | Call videoClip to cut the uploaded video interval and convert key parameters. | POST | /vod/videoManage/videoClip |
| Videoclipquery | Call videoClip to query the clipping result of the clipping task. | POST | /vod/videoManage/videoClipQuery |
| Videoconcat | Call videoConcat to splice multiple videos according to the specified sequence to generate a new video file. | POST | /vod/videoManage/videoConcat |
| Videoconcatquery | The videoConcatQuery command is used to query the result of the video stitching task | POST | /vod/videoManage/videoConcatQuery |
| Createclearadtask | Call createClearAdTask to create AI de-advertising task for the specified video, and the system will automatically conduct AI de-advertising operation for the video (value-added service function, if necessary, please contact customer service to open the value-added service of "AI de-advertising"). | POST | /vod/ai/createClearAdTask |
| Clearadtaskquery | Query AI clear AD task status and results | POST | /vod/ai/clearAdTaskQuery |
| Transcode | Use the transCode method to convert the specified video, mainly including transcoding the resolution and adding watermarks. | POST | /vod/videoManage/transCode |