# Wangsu SDK for Python

This SDK provides Python interfaces to interact with Wangsu API services.

## Installation

Install the SDK using pip:

```bash
pip install wangsu-sdk-python
```

Install the SDK for a specific product category using pip:

```bash
pip install wangsu-sdk-python-channelsmanagement
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
from wangsu.channelsmanagement.models import *

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
| Getpullchannelconfigure | This interface gets the name of a created source pull channel specified on the platform, the source pull URL,<br>Configure information such as the URL.<br>Note: This interface can only obtain the channel configuration information of the source pull mode | POST | /live/channelManage/getPullChannelConfigure |
| Getpullchannellist | This interface is used to obtain information about all created source pull channels, including the channel name, pull ID, and creation time | POST | /live/channelManage/getPullChannelList |
| Setchannelstaterealtimeback | The real-time channel status feedback function can be enabled or disabled through this interface, and the status callback address can be set. The cloud video background sends GET requests to the callback address through the HTTP interface, and the status of the video stream successfully pushed or disconnected is reported to the user in real time. | POST | /live/channelManage/setChannelStateRealtimeBack |
| Createrecordtask | This interface is used to create a live recording task. Within the specified time period, all live events on the specified channel are generated<br>Is recorded and saved. If the channel to which the live recording task belongs is the source stream mode, the stream cannot be pulled after the task starts<br>If a recording task cannot be performed, a maximum of nine times will be performed again. If the recording fails after the last retry, the system will retry again<br>A retry will not be initiated until the scheduled recording end time.<br>After the ejector sends the rtmp stop flag signal, normal services stop recording. If the customer is in some special<br>In a given service scenario (interactive live stream switching), if the rtmp stop flag signal is sent and the recording is required to continue,<br>Use http pull stream recording. For details, see the httpPullRecord parameter. | POST | /live/channelManage/createRecordTask |
| Endrecordtask | This interface allows you to terminate live recording tasks in real time | POST | /live/channelManage/endRecordTask |
| Recordtaskquery | Users can obtain recording status information through callback and recording status query interfaces | POST | /live/channelManage/recordTaskQuery |
| Directorycreate | This interface is used to create a new recording directory. A channel specifies the directory created by this interface to broadcast live videos of the channel<br>Will be stored in this directory | POST | /live/recordDirectoryManage/directoryCreate |
| Getdirectorylist | This interface is used to obtain the record directory list | POST | /live/recordDirectoryManage/getDirectoryList |
| Getdirectory | This interface is used to obtain information about the specified recorded directory | POST | /live/recordDirectoryManage/getDirectory |
| Getchannelshareurl | Obtain the URL of the live broadcast sharing page | POST | /live/channelManage/getChannelShareUrl |
| Getrecordfileinfo | Obtain information about the live broadcast recording file. Information about the recording file generated in the 2.19 interface for Creating a Live Recording Task is displayed. | POST | /live/channelManage/getRecordFileInfo |
| Disconnectstream | After the successful call, the channel's live streaming address will be interrupted. If the channel is pushing the stream, the performance<br>The connection is interrupted. The flow recovers automatically after being pushed again. Note that this interface is not suitable for source-end pull stream channels. | POST | /live/channelManage/disconnectStream |
| Startforwardtask | Create a ForwardTask | POST | /live/forwardTask/startForwardTask |
| Endforwardtask | End ForwardTask | POST | /live/forwardTask/endForwardTask |
| Getforwardtasklist | Query the forwarding task list | POST | /live/forwardTask/getForwardTaskList |
| Createchannel | Through this interface to create a channel on the platform, the system generates a push stream address and several corresponding pull stream addresses and related resources.<br>The system will assign a globally unique pullId to the channel as its unique identifier. | POST | /live/channelManage/createChannel |
| Getchannelconf | This interface is used to obtain configuration information such as the name of a created channel specified on the platform, the URL for pushing streams, and the URL for pulling streams at the player end. | POST | /live/channelManage/getChannelConfigure |
| Getchannellist | This interface is used to obtain information about all created channels, including channel name, pull stream ID, channel live status, and creation time. | POST | /live/channelManage/getChannelList |
| Deletechannel | Using this interface, you can permanently delete one or more created cloud live channels. | POST | /live/channelManage/deleteChannel |
| Getchannellivestate | Obtain the real-time status of a designated channel, including 'live streaming', 'not live streaming', and 'banned'. | POST | /live/channelManage/getChannelLiveState |
| Batchchannellivestate | The live broadcast status of a specified channel or multiple channels can be obtained through this interface. The status mainly includes "live broadcast", "not live broadcast", and "Forbidden broadcast". | POST | /live/channelManage/batchChannelLiveState |
| Channelforbidden | This interface can be used to trigger a Prompt stream forbidding on one or more specified Domain . After the ban, the Domain can no longer stream pushing. The ban lasts for 7 days and is automatically restored after 7 days. If you want to restore in advance, you can Invoke the Domain replay interface. | POST | /live/channelManage/channelForbidden |
| Channelrebrodcast | Through this interface, the specified one or more banned channels can be triggered to replay. After replay, the channels can successfully push streams. | POST | /live/channelManage/channelReBrodcast |
| Channeledit | Through this interface, you can edit and modify the specified created channel, change the channel name, refresh the URL of the push stream, etc | POST | /live/channelManage/channelEdit |
| Getsinglepullcode | Through this interface can obtain a specified channel playback code, mainly  swf code, js code, video url. | POST | /live/channelManage/getSinglePullCode |
| Setpushtsatc | Through this interface to set the push time stamp for a specified channel anti-leech link; This interface is effective only when the timestamp anti-leech function is configured for the name of the push basin. | POST | /live/channelManage/setPushTsatc |
| Createpullchannel | You need to enable the source stream pulling service and create a live stream channel in source stream pulling mode through this interface. When the player receives a request, the system automatically pulls back the specified source stream from the interface. | POST | /live/channelManage/createPullChannel |
| Editpullchannel | Through this interface, you can edit and modify the specified created source pull channel, change the channel name and source pull url, etc.<br>Note: Only source pull mode channel configuration information can be configured on this interface. | POST | /live/channelManage/editPullChannel |
| Setpulltsatc | Through the interface for a specified channel to set the pull time stamp anti-leaver link; This interface is valid only when the timestamp anti-theft link function is configured for the name of the push basin | POST | /live/channelManage/setPullTsatc |