# Wangsu SDK for Python

此 SDK 提供与网宿 API 服务交互的 Python 接口。

## 安装

使用 pip 安装 SDK：

```bash
pip install wangsu-sdk-python
```
使用 pip 安装特定产品分类的 SDK：

```bash
pip install wangsu-sdk-python-devicemanagement
```


## 要求

- Python 3.6 或更高版本
- 依赖项：
  - requests >= 2.10.0
  - alibabacloud_tea >= 0.3.3
  - alibabacloud_tea_openapi >= 0.3.6
  - alibabacloud_tea_console >= 0.0.1
  - alibabacloud_tea_util >= 0.3.8

## 快速开始

### 示例

SDK 使用 AKSK 认证。您需要配置您的访问密钥和密钥：

```python
import json
from wangsu.common.auth.AkSkConfig import AkSkConfig
from wangsu.common.auth.AkSkAuth import AkSkAuth
from wangsu.devicemanagement.models import *

# 参考本文档最后的API列表，修改一下对应的{ActionName}、Method、Uri
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


## API列表
有关详细的 API 文档和可用方法，请参阅[官方 Wangsu API 文档](https://www.wangsu.com/document/api-doc/Overview?productType=all)。

| ActionName | description | client_methods | uri |
| --- | --- | --- | --- |
| Getstreamurl | 获取通道播放url | POST | /ivcs/devicemanage/getStreamUrl |
| Editdevice | 编辑设备信息 | POST | /ivcs/devicemanage/editDevice |
| Getdeviceslist | 获取设备列表 | POST | /ivcs/devicemanage/getDevicesList |
| Invitepush | 邀请设备通道推流 | POST | /ivcs/devicemanage/invitePush |
| Stoppush | 停止设备通道推流 | POST | /ivcs/devicemanage/stopPush |
| Createdevice | 新增设备 | POST | /ivcs/devicemanage/createDevice |
| Deletedevice | 删除设备 | POST | /ivcs/devicemanage/deleteDevice |
| Querychannellist | 获取通道列表 | POST | /ivcs/devicemanage/getChnList |
| Editchannelinfo | 编辑通道信息 | POST | /ivcs/devicemanage/editChnInfo |
| Ptzcontrol | 云台控制 | POST | /ivcs/devicemanage/Ptzcontrol |
| ChannelControl | 通道禁用/启用 | POST | /ivcs/devicemanage/channelControl |
| ChannelStatusUpdate | 该接口用于更新通道信息，可以通过该接口主动更新设备下的通道列表和通道状态。主要用于设备在通道新增、删除、或者上下线时没有向平台汇报，或者汇报失败，用户可以通过改接口主动让设备再重新更新汇报一次。 | POST | /ivcs/devicemanage/channelStatusUpdate |