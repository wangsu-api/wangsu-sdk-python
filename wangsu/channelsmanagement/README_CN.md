# Wangsu SDK for Python

此 SDK 提供与网宿 API 服务交互的 Python 接口。

## 安装

使用 pip 安装 SDK：

```bash
pip install wangsu-sdk-python
```
使用 pip 安装特定产品分类的 SDK：

```bash
pip install wangsu-sdk-python-channelsmanagement
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
from wangsu.channelsmanagement.models import *

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
| Getpullchannelconfigure | 通过该接口获取平台上指定的一个已创建源拉流频道的名称、源拉流 URL、<br>拉流 URL 等配置信息。<br>注：该接口只能获取源拉流模式的频道配置信息 | POST | /live/channelManage/getPullChannelConfigure |
| Getpullchannellist | 通过该接口获取所有已创建的源拉流频道信息，包括频道名、拉流 ID、创建时间 | POST | /live/channelManage/getPullChannelList |
| Setchannelstaterealtimeback | 通过该接口开启/关闭频道状态实时反馈功能，同时可设置状态回调地址，云视频后台<br>通过 HTTP 接口向回调地址发送 GET 请求，将视频流推流成功、断流成功的状态实时反馈给<br>用户。 | POST | /live/channelManage/setChannelStateRealtimeBack |
| Createrecordtask | 通过该接口创建直播录制任务，在任务指定时间段内，指定的频道所有直播活动都会<br>被录制保存。若该直播录制任务所属频道为源端拉流模式，则在任务开始后，因为拉不到流<br>的情况导致的无法正常录制任务，最多会重试 9 次，如果最后一次重试后仍然录制失败，则<br>在计划录制结束时间前不会再去发起重试。<br>当推流端发送了 rtmp stop flag 信号后，正常业务是会停止录制的。若客户在某些特<br>定业务场景下（互动直播流切换），当发送了 rtmp stop flag 信号也要求继续录制的话，<br>请使用 http 拉流录制，具体见参数“httpPullRecord”。 | POST | /live/channelManage/createRecordTask |
| Endrecordtask | 通过该接口可实时终止直播录制任务 | POST | /live/channelManage/endRecordTask |
| Recordtaskquery | 用户可通过回调和录制状态查询接口来获取录制的状态信息 | POST | /live/channelManage/recordTaskQuery |
| Directorycreate | 通过该接口创建一个新录制目录，某频道指定了该接口创建的目录后，频道的直播视频<br>将存储在该目录下 | POST | /live/recordDirectoryManage/directoryCreate |
| Getdirectorylist | 通过该接口获取录制目录列表 | POST | /live/recordDirectoryManage/getDirectoryList |
| Getdirectory | 通过该接口获取指定录制目录信息 | POST | /live/recordDirectoryManage/getDirectory |
| Getchannelshareurl | 获取直播分享页面 URL | POST | /live/channelManage/getChannelShareUrl |
| Getrecordfileinfo | 获取直播录制文件信息。返回网页推流录制和 2.19 创建直播录制任务接口生成的录制<br>文件信息。 | POST | /live/channelManage/getRecordFileInfo |
| Disconnectstream | 调用成功后，会对该频道的直播推流地址进行一次断流。如果该频道正在推流，则表现<br>为连接中断。重新推流后自动恢复。注意该接口不适合源端拉流频道。 | POST | /live/channelManage/disconnectStream |
| Startforwardtask | 创建一个转推任务 | POST | /live/forwardTask/startForwardTask |
| Endforwardtask | 停止转推任务 | POST | /live/forwardTask/endForwardTask |
| Getforwardtasklist | 查询转推任务列表 | POST | /live/forwardTask/getForwardTaskList |
| Createchannel | 通过该接口在平台上创建一个频道，系统生成一个推流地址和对应的若干个拉流地址和相关资源。<br> 系统会为该频道分配全局唯一的 pullId，作为该频道唯一标识。 | POST | /live/channelManage/createChannel |
| Getchannelconf | 通过该接口获取平台上指定的一个已创建频道的名称、推流 URL、播放端拉流 URL 等配置信息。 | POST | /live/channelManage/getChannelConfigure |
| Getchannellist | 通过该接口获取所有已创建的频道信息，包括频道名、拉流 ID、频道直播状态、创建时间。 | POST | /live/channelManage/getChannelList |
| Deletechannel | 通过该接口可永久删除指定的一个或多个已创建的云直播频道。 | POST | /live/channelManage/deleteChannel |
| Getchannellivestate | 通过该接口获取指定的某一个频道的直播状态，状态主要有“直播中”“未直播”“禁<br>播”三种。 | POST | /live/channelManage/getChannelLiveState |
| Batchchannellivestate | 通过该接口获取指定一个或多个频道的直播状态，状态主要有“直播中”“未直播”“禁播”三种。 | POST | /live/channelManage/batchChannelLiveState |
| Channelforbidden | 通过该接口可对指定的一个或多个频道触发秒级禁播，禁播后频道不可再推流。禁播时长为7天，7天后自动恢复。如果要提前恢复可以调用频道复播接口。 | POST | /live/channelManage/channelForbidden |
| Channelrebrodcast | 通过该接口可对指定的一个或多个被禁播的频道触发复播，复播后频道可成功推流。 | POST | /live/channelManage/channelReBrodcast |
| Channeledit | 通过该接口可对指定的已创建的频道进行编辑修改，更改频道名称，刷新推流 URL 等 | POST | /live/channelManage/channelEdit |
| Getsinglepullcode | 通过该接口可获取指定的一个指定频道的播放代码，主要是swf 代码、js代码、视频 url。 | POST | /live/channelManage/getSinglePullCode |
| Setpushtsatc | 通过该接口为指定的一个频道设置推流时间戳防盗链；只有推流域名配置了时间戳防盗链功能该接口才有效。 | POST | /live/channelManage/setPushTsatc |
| Createpullchannel | 需开通源拉流服务，通过该接口创建一个源端拉流模式的直播频道，当播放端有请求时，系统自动回源拉取接口中指定的源直播流。 | POST | /live/channelManage/createPullChannel |
| Editpullchannel | 通过该接口可对指定的已创建的源拉流频道进行编辑修改，更改频道名称和源拉流 url等。<br>注：该接口只能配置源拉流模式频道配置信息。 | POST | /live/channelManage/editPullChannel |
| Setpulltsatc | 通过该接口为指定的一个频道设置拉流时间戳防盗链；只有推流域名配置了时间戳防盗 链功能该接口才有效。 | POST | /live/channelManage/setPullTsatc |