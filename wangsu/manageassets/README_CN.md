# Wangsu SDK for Python

此 SDK 提供与网宿 API 服务交互的 Python 接口。

## 安装

使用 pip 安装 SDK：

```bash
pip install wangsu-sdk-python
```
使用 pip 安装特定产品分类的 SDK：

```bash
pip install wangsu-sdk-python-manageassets
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
from wangsu.manageassets.models import *

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
| Getvideolist | 调用getVideoList客户获取已上传视频的信息列表（包含：上传时间、视频名称、视频ID、视频状态等） | POST | /vod/videoManage/getVideoList |
| Videoedit | 调用videoEdit可以对单个视频的基础信息进行编辑。 | POST | /vod/videoManage/videoEdit |
| Videoblock | 调用videoBlock对已上传视频进行屏蔽禁用，被禁用的时候将不能再继续观看。 | POST | /vod/videoManage/videoBlock |
| Videoenable | 调用videoEnable对已禁用的视频进行重新启用。 | POST | /vod/videoManage/videoEnable |
| Deletevideo | 调用deleteVideo对已上传的视频进行删除。 | POST | /vod/videoManage/deleteVideo |
| Getmateriallist | 调用getMaterialList获取已上传素材的信息列表里 | POST | /vod/material/getMaterialList |
| Materialedit | 调用materialEdit可以对单个素材文件的基础信息进行编辑。 | POST | /vod/material/materialEdit |
| Deletematerial | 调用deleteVideo对已上传的素材文件进行删除。 | POST | /vod/material/deleteMaterial |
| Getaudiolist | 查询音频文件列表，按照上传时间倒序排序。支持分页去获取列表 | POST | /vod/audioManage/getAudioList |
| Editaudio | 对指定单个音频频的基础信息进行编辑 | POST | /vod/audioManage/editAudio |
| Deleteaudio | 通过该接口删除指定音频。 | POST | /vod/audioManage/deleteAudio |
| Getcategorylist | 获取标签分类列表 | POST | /vod/videoCategory/getCategoryList |
| Createcategory | 创建标签分类 | POST | /vod/videoCategory/createCategory |
| Deletecategory | 删除标签分类 | POST | /vod/videoCategory/deleteCategory |
| Deletevideobycategory | 根据标签分类删除视频 | POST | /vod/videoCategory/deleteVideoByCategory |