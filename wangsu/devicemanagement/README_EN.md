# Wangsu SDK for Python

This SDK provides Python interfaces to interact with Wangsu API services.

## Installation

Install the SDK using pip:

```bash
pip install wangsu-sdk-python
```

Install the SDK for a specific product category using pip:

```bash
pip install wangsu-sdk-python-devicemanagement
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
from wangsu.devicemanagement.models import *

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
| Getstreamurl | Get the channel playback URL | POST | /ivcs/devicemanage/getStreamUrl |
| Editdevice | Edit device info | POST | /ivcs/devicemanage/editDevice |
| Getdeviceslist | Obtain the list of devices | POST | /ivcs/devicemanage/getDevicesList |
| Invitepush | Invitepush | POST | /ivcs/devicemanage/invitePush |
| Stoppush | Stoppush | POST | /ivcs/devicemanage/stopPush |
| Createdevice | Add new device | POST | /ivcs/devicemanage/createDevice |
| Deletedevice | Deleting a device | POST | /ivcs/devicemanage/deleteDevice |
| Querychannellist | Get channel list | POST | /ivcs/devicemanage/getChnList |
| Editchannelinfo | edit channel info | POST | /ivcs/devicemanage/editChnInfo |
| Ptzcontrol | ptz control | POST | /ivcs/devicemanage/Ptzcontrol |
| ChannelControl | Channel disable/enable | POST | /ivcs/devicemanage/channelControl |
| ChannelStatusUpdate | This interface is used to update channel information. You can use this interface to actively update the channel list and channel status of the device. It is mainly used when the device does not report to the platform when adding, deleting, or going online or offline, or the report fails. Users can use this interface to actively let the device update and report again. | POST | /ivcs/devicemanage/channelStatusUpdate |