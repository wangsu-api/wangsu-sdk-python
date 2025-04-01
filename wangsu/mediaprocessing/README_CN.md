# Wangsu SDK for Python

此 SDK 提供与网宿 API 服务交互的 Python 接口。

## 安装

使用 pip 安装 SDK：

```bash
pip install wangsu-sdk-python
```
使用 pip 安装特定产品分类的 SDK：

```bash
pip install wangsu-sdk-python-mediaprocessing
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
from wangsu.mediaprocessing.models import *

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
| Videoclip | 调用videoClip对已上传的视频进行按时间区间剪切视频并转换关键参数。 | POST | /vod/videoManage/videoClip |
| Videoclipquery | 调用videoClip查询剪切任务的剪切结果。 | POST | /vod/videoManage/videoClipQuery |
| Videoconcat | 调用videoConcat对多个视频按指定的顺序进行拼接，生成新的视频文件。 | POST | /vod/videoManage/videoConcat |
| Videoconcatquery | 调用videoConcatQuery查询视频拼接任务结果 | POST | /vod/videoManage/videoConcatQuery |
| Createclearadtask | 调用createClearAdTask为指定视频创建AI去广告任务，系统会自动针对该视频进行AI去广告操作（增值服务功能，如若需要请联系客服开通“AI清除广告”增值服务）。 | POST | /vod/ai/createClearAdTask |
| Clearadtaskquery | 调用clearAdTaskQuery查询AI去广告任务处理状态和结果。 | POST | /vod/ai/clearAdTaskQuery |
| Transcode | 调用transCode对指定的视频进行转码（主要包含：分辨率转码、加水印转码） | POST | /vod/videoManage/transCode |