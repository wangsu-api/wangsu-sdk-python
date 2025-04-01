# Wangsu SDK for Python

此 SDK 提供与网宿 API 服务交互的 Python 接口。

## 安装

使用 pip 安装 SDK：

```bash
pip install wangsu-sdk-python
```
使用 pip 安装特定产品分类的 SDK：

```bash
pip install wangsu-sdk-python-nglogconfiguration
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
from wangsu.nglogconfiguration.models import *

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
| GetAListOfLogConfigurations | 获取已创建的日志配置列表。 | GET | /cdn/report/logConfigs |
| CreateALogConfiguration | 创建日志配置，用于定义访问日志的输出格式。同一个日志配置可适用于一个或多个域名。每个域名必须有指定的日志配置，才能获取到该域名的日志。创建日志配置后，大约需要等待40分钟才会生效。 | POST | /cdn/report/logConfigs |
| GetALogConfiguration | 获取日志配置的详细信息。 | GET | /cdn/report/logConfigs/* |
| UpdateALogConfiguration | 更新日志配置。配置更新后，大约需要等待40分钟才会生效。 | PATCH | /cdn/report/logConfigs/* |
| DeleteALogConfiguration | 删除日志配置。 | DELETE | /cdn/report/logConfigs/* |
| GetAccessLogsForHostnames | 获取已部署的一个或多个加速域名的访问日志。这些日志是2小时或更早时间之前客户端请求所产生的日志。默认情况下，只能查询近14天内的日志。这些日志被切割成多个文件供下载。<br><br>要获取加速域名的日志，必须首先通过“创建日志投递配置”接口定义日志格式。注意：必须先创建日志投递配置，访问日志才会被收集。如未创建日志投递配置，则无法下载日志。<br><br>日志格式示例:<br>%cltip %rmtuser [%utctime] "%method %url %protocol" %statuscode %rspsize "%referer" "%ua" %rsptime<br><br>调用该接口时，将返回如下的日志信息和下载链接:<br>{<br>  "logs":[<br>          {<br>          "dateFrom":"2021-10-31T00:00:00Z",<br>          "dateTo":"2021-10-31T00:29:59Z",<br>          "fileSize":105878,<br>          "logUrl":"https://abc.example.com/logd/v2/download/0621c8fc885089805kea5f610797ff8ba92bc98c049c2bb308cbdb?traceId=ac6d696c657765625f74657374cf0000018dd01d89e8cd06d3",<br>          "hostname":"mydomain.domain.info"<br>          }<br>        ]<br>}<br><br>其中，logUrl字段返回日志文件（经过gzip压缩）的下载链接。下载链接有效期为24个小时。如链接已过期，需重新调用接口获取链接。日志文件内容示例：<br>9.8.7.6 - [31/Oct/2021:19:59:57 +0000] "GET http://mydomain.domain.info/i/js/tab.js HTTP/1.1" 304 529 "http://mydomain.domain.info/?q=downloads" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36" 76<br><br> | POST | /cdn/report/logDownload |