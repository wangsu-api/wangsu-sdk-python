# Wangsu SDK for Python

此 SDK 提供与网宿 API 服务交互的 Python 接口。

## 安装

使用 pip 安装 SDK：

```bash
pip install wangsu-sdk-python
```
使用 pip 安装特定产品分类的 SDK：

```bash
pip install wangsu-sdk-python-uploadassets
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
from wangsu.uploadassets.models import *

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
| Getuploadtoken | 调用getUploadToken获取视频文件上传地址和凭证 | POST | /vod/videoManage/getUploadToken |
| Getaudiouploadtoken | 调用getAudioUploadToken获取音频文件上传地址和凭证，支持批量获取多个音频上传地址和凭证（最多50个）。 | GET | /vod/audioManage/getAudioUploadToken |
| Getmaterialuploadtoken | 调用getMaterialUploadToken获取素材上传地址和凭证，支持批量获取多个素材地址和凭证（最多50个）。 | POST | /vod/material/getMaterialUploadToken |
| Pullvideo | 调用pullVideo向后台设置要拉取的视频url。后台定时自动完成第三方平台url视频拉取并保存。支持批量设置拉取任务。 | POST | /vod/videoManage/pullVideo |
| Pullvideoquery | 调用pullVideoQuery可以查询拉取任务完成情况。 | POST | /vod/videoManage/pullVideoQuery |