# Wangsu SDK for Python

此 SDK 提供与网宿 API 服务交互的 Python 接口。

## 安装

使用 pip 安装 SDK：

```bash
pip install wangsu-sdk-python
```
使用 pip 安装特定产品分类的 SDK：

```bash
pip install wangsu-sdk-python-domainconfigurtion
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
from wangsu.domainconfigurtion.models import *

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
| Updatedomainsrcstrategyforwplus | 设置域名的回源配置策略，包括：高级源、Rangel回源、301和302回源跟随。 | POST | /api/domain/setsrcconfig |
| Editdomainconfig | 修改指定加速域名的基础配置。接口调用url的*可为域名名称或域名ID | PUT | /api/domain/* |
| Updatetimecontrolservice | 修改时间戳防盗链 | PUT | /api/config/timecontrol/* |
| Querytimecontrolservice | 查看时间戳防盗链 | GET | /api/config/timecontrol/* |
| Editdomainredirectconfig | 通过接口自助实现，url重定向功能 | PUT | /api/config/InnerRedirect/* |
| Edithttpheaderconfig | 通过接口自助实现http头部增删改功能，可通过在cdn层对客户实现个性化http头部控制，让客户在不需要修改源站的情况下，实现定制化的http头部和加速效果的提升。接口url的*可为域名名称或域名id。 | PUT | /api/config/headermodify/* |
| Queryhttpheaderconfig | 通过接口自助查询http头部配置。接口url的*可为域名名称或域名id。 | GET | /api/config/headermodify/* |
| Editcachetimeconfig | 通过接口自助实现修改域名缓存时间配置，实现针对客户的请求实现定制缓存功能。节点缓存分为常规缓存和带查询串URl缓存，在常规缓存里您可以设置缓存时间以及对某些影响缓存的头进行忽略处理，以及是否缓存空文件等，带查询串Url可以设置缓存成多份还是缓存成去掉问号后的url（增加命中率）。接口调用url的*可为域名名称或域名id | PUT | /api/config/cachetime/* |
| Editantihotlinkingconfig | 通过接口自助实现修改域名防盗链下IP白名单配置、referer防盗链配置，实现对具体访问IP做白名单或黑名单控制或referer控制。接口url的*可为域名名称或域名id。 | PUT | /api/config/visitcontrol/* |
| Queryantihotlinkingconfig | 通过接口自助查询防盗链配置。接口url的*可为域名名称或域名id。 | GET | /api/config/visitcontrol/* |
| Updatesourceverificationconfig | 通过接口自助实现转推回源带参数鉴权，实现rtmp转推回源，边缘能够根据加密规则，模拟客户端带上时间戳防盗链的参数进行转推回源 | PUT | /api/config/sourceverification/* |
| Querysourceverificationconfig | 通过接口自助查询转推回源带参数鉴权配置 | GET | /api/config/sourceverification/* |
| Updatecachebyresponseheaderconfig | 通过接口自助实现遵循源站缓存规则，有缓存头的时候按源站缓存头缓存，无缓存头时不缓存。 | PUT | /api/config/cachebyrespheader/* |
| Querycachebyresponseheaderconfig | 通过接口自助查询响应头内容缓存规则。 | GET | /api/config/cachebyrespheader/* |
| Addbanurltodomian | 通过接口自助新增URL屏蔽的功能。客户可以根据自己的需求调用接口，新增URL屏蔽内容 | PUT | /api/basicconfig/illegalinformation |
| Predeploycachetimeconfig | 通过接口自助查询节点缓存配置配置 | PUT | /api/predeploy/cachetime/* |
| Predeployredirectconfig | 查看内部重定向配置 | PUT | /api/predeploy/InnerRedirect/* |
| Queryapideployservice | 对于域名的新增、修改、启用、禁用、取消、恢复、删除等请求 | POST | /api/request/* |
| Updatecompressionconfig | 通过接口自助实现压缩响应功能 | PUT | /api/config/compresssetting/* |
| Querycompressionconfig | 通过接口自助查询压缩响应配置 | GET | /api/config/compresssetting/* |
| Predeploycompressionconfig | 通过接口自助查询压缩响应配置 | PUT | /api/predeploy/compresssetting/* |
| Queryhttpcodecasheconfig | 通过接口自助查询状态码缓存配置 | GET | /api/config/httpcodecache/* |
| Queryipv6config | 通过接口自助查询域名是否使用ipv6资源 | GET | /api/domain/ipv6/* |
| Queryaccessspeedconfig | 通过接口自助查询访问限速配置 | GET | /api/config/accessspeed/* |
| Queryafterredirect | 查看拉取跳转后的文件 | GET | /api/config/afterredirect/* |
| Updateafterredirect | 修改拉取跳转后的文件 | PUT | /api/config/afterredirect/* |
| Queryinnerredirect | 查看内部重定向配置 | GET | /api/config/InnerRedirect/* |
| Querycachetime | 通过接口自助查询节点缓存配置配置。接口调用url的*可为域名名称或域名id。 | GET | /api/config/cachetime/* |
| Editquerystringurlconfig | 通过接口自助实现查询串设置功能 | PUT | /api/config/querystring/* |
| Queryquerystringurlconfig | 通过接口自助实现修改域名的查询串设置，实现针对客户的请求实现定制缓存功能。带查询串Url可以设置缓存成多份还是缓存成去掉问号后的url（增加命中率），可以设置是否用原始请求回源等。接口调用url的*可为域名名称或域名id。 | GET | /api/config/querystring/* |
| Updatetosauthorizationconfig | 通过接口自助实现TOS回源鉴权配置功能。接口url的*可为域名名称或域名id。 | PUT | /api/config/tosaccess/* |
| Querytosauthorizationconfig | 通过接口自助查询TOS回源鉴权配置。接口url的*可为域名名称或域名id。 | GET | /api/config/tosaccess/* |
| Edithttpcodecache | 通过接口自助实现状态码缓存设置功能 | PUT | /api/config/httpcodecache/* |
| Queryamazons3authorizationconfig | 通过接口自助查询Amazon S3鉴权配置。接口url的*可为域名名称或域名id。 | GET | /api/config/amazons3access/* |
| Updateamazons3authorizationconfig | 通过接口自助实现Amazon S3鉴权配置功能。接口url的*可为域名名称或域名id。 | PUT | /api/config/amazons3access/* |
| Updatealiyunossauthorizationconfig | 通过接口自助实现Aliyun OSS鉴权功能。接口url的*可为域名名称或域名id。 | PUT | /api/config/ossaccess/* |
| Queryaliyunossauthorizationconfig | 通过接口自助查询Aliyun OSS鉴权配置。接口url的*可为域名名称或域名id。 | GET | /api/config/ossaccess/* |
| Editdomainproperty | 修改域名属性，如回源IP、回源host、回源端口。 | POST | /api/domain/property/* |
| Queryignoreprotocol | 通过接口自助查询忽略协议缓存和推送配置 | GET | /api/config/ignoreprotocol/* |
| Editignoreprotocol | 通过接口自助修改忽略协议缓存和推送配置 | PUT | /api/config/ignoreprotocol/* |
| Editoriginuriandhost | 修改回源uri和host改写 | PUT | /api/config/originrulesrewrites/* |
| Queryoriginuriandhost | 查询回源uri和host改写 | GET | /api/config/originrulesrewrites/* |
| Editwebsocketconfig | 通过接口自助修改websocket开关配置。接口url的*可为域名名称或域名id。 | PUT | /api/config/websocket/* |
| Querywebsocketconfig | 通过接口自助查询websocket开关配置。接口url的*可为域名名称或域名id。 | GET | /api/config/websocket/* |
| Deletebanurls | 删除非法屏蔽url接口 | DELETE | /api/basicconfig/illegalinformation |
| Batchaddillegalinformation | 批量新增域名封禁URL | PUT | /api/config/Batchaddillegalinformation |
| Batchdelillegalinformation | 批量删除域名封禁URL | DELETE | /api/config/Batchdelillegalinformation |
| Updatesingletranscodingconfigforwplus | 更新单条转码配置。接口url的*可为域名名称或域名id。 | PUT | /api/config/transcodes/* |
| Querysingletranscodingconfigforwplus | 查询单条转码配置。接口url的*可为域名名称或域名id。 | GET | /api/config/transcodes/* |
| Updateglobaltranscodingconfigforwplus | 更新转码全局配置。接口url的*可为域名名称或域名id。 | PUT | /api/config/transcodeswitch/* |
| Queryglobaltranscodingconfigforwplus | 查询转码全局配置。接口url的*可为域名名称或域名id。 | GET | /api/config/transcodeswitch/* |
| Querylivestreamingantihotlinkingconfig | 通过接口自助查询流媒体普通防盗链配置。接口url的*可为域名名称或域名id。 | GET | /api/config/live-visitcontrol/* |
| Updatelivevisitcontrolconfig | 通过接口自助修改流媒体普通防盗链配置。接口url的*可为域名名称或域名id。 | PUT | /api/config/live-visitcontrol/* |
| Querylivestreamingtimestampantihotlinkingconfig | 通过接口自助查询流媒体时间戳防盗链配置。接口url的*可为域名名称或域名id。 | GET | /api/config/live-timestampvisitcontrol/* |
| Editlivestreamingtimestampantihotlinkingconfig | 通过接口自助修改流媒体防盗链配置。接口url的*可为域名名称或域名id。 | PUT | /api/config/live-timestampvisitcontrol/* |
| PredeployedStreamingTimestampVisitControl | 通过接口自助预部署流媒体时间戳防盗链。接口url的*可为域名名称或域名id。 | PUT | /api/predeploy/live-timestampvisitcontrol/* |
| QueryCloudStorageBasicConfiguration | 查询录制截图云存储配置。接口url的*可为域名名称或域名id。 | GET | /api/config/cloudstorage/* |
| UpdateCloudStorageBasicConfiguration | 修改录制截图云存储配置。接口url的*可为域名名称或域名id。 | PUT | /api/config/cloudstorage/* |
| QueryRecordingBasicConfiguration | 查询录制基础配置。接口url的*可为域名名称或域名id。 | GET | /api/config/recording/* |
| UpdateRecordingBasicConfiguration | 修改录制基础配置。接口url的*可为域名名称或域名id。 | PUT | /api/config/recording/* |
| Getbasicconfigurationofdomain | 查看指定加速域名的基础配置。 | GET | /api/domain/* |
| UpdateScreenshotConfiguration | 修改截图基础配置。接口url的*可为域名名称或域名id。 | PUT | /api/config/screenshot/* |
| QueryScreenshotConfiguration | 查询截图基础配置。接口url的*可为域名名称或域名id。 | GET | /api/config/screenshot/* |
| Queryappadomainportinfoforwplus | 获取客户APPA域名配置 | GET | /api/domainlist/appa |
| QueryBanUrlByDomain | 查询账号下所有封禁的url信息，这里的账号，为调用接口并鉴权的账号 | POST | /api/config/banurl |
| Queryhttp2settingsconfigforwplus | 查询Http2.0配置接口。接口url的*可为域名名称或域名id。 | GET | /api/config/http2/* |
| Updatehttp2settingsconfigforwplus | 修改http2.0开关配置接口。接口url的*可为域名名称或域名id。 | PUT | /api/config/http2/* |
| Enableordisablewafprotection | 开启或关闭域名的WAF服务 | PUT | /api/domain/wafsecurity |
| Enableordisablebotprotection | 开启或关闭域名Bot防护 | PUT | /api/domain/botsecurity |
| UpdateCacheKeyConfiguration | 修改缓存key配置。接口url的*可为域名名称或域名id。 | PUT | /api/config/cachekey/* |
| QueryCacheKeyConfiguration | 查询缓存key配置。接口url的*可为域名名称或域名id。 | GET | /api/config/cachekey/* |
| Editaccessspeedlimit | 修改访问限速配置 | POST | /api/config/accessspeed/* |
| Enableordisabledmsprotection | 开启或关闭域名Dms防护 | PUT | /api/domain/dmssecurity |
| Editback2originprotocolrewriteconfig | 支持修改回源协议和端口	 | PUT | /api/config/back2originrewrite/* |
| Queryback2originprotocolrewriteconfig | 支持查询回源协议和端口	 | GET | /api/config/back2originrewrite/* |
| Updatestreamnotificationconfig | 修改流状态反馈配置。接口url的*可为域名名称或域名id。 | PUT | /api/config/streamnotification/* |
| Querystreamnotificationconfig | 查询流状态反馈配置。接口url的*可为域名名称或域名id。 | GET | /api/config/streamnotification/* |
| Querydomainbillingarea | 查询域名的计费区域 | GET | /api/domain/billingarea/* |
| Updatedomaincertconfig | 为CDN加速域名配置证书，仅支持SNI。 | PUT | /api/config/certificate/* |
| Addappadomain | 新增应用加速域名 | POST | /api/domain/appa |
| Updateappadomain | 修改应用加速域名 | PUT | /api/domain/appa/* |
| Getappadomainconfig | 查询应用加速域名 | GET | /api/domain/appa/* |
| Querydomaincertconfig | 为CDN加速域名查询配置证书，仅支持SNI。 | GET | /api/config/certificate/* |
| Pushnotifyaddress | 推送地址变更 | PUT | /api/notifyaddress |
| Queryappacarryclientipconfig | 查询指定加速域名的携带用户IP回源配置信息 | GET | /api/config/appacarryclientip/* |
| Updatedomainmulticertconfig | 为CDN加速域名配置证书，支持SNI和多SNI。 | PUT | /api/config/certificate/v2/* |
| Updateipversionconfig | 域名默认使用V4资源，可以设置域名V6或V4+V6。 | PUT | /api/config/ipversion/* |
| Querylivedomainorigins | 查询直播域名源站配置 | GET | /live/domains/*/origins |
| Updatelivedomainorigins | 修改直播域名源站配置 | PUT | /live/domains/*/origins |
| Querylivedomainpagination | 查询直播域名列表 | GET | /live/domains |
| Querylivedomaintls | 查询直播域名TLS配置 | GET | /live/domains/*/tls |
| Updatelivedomaintls | 修改直播域名TLS配置 | PUT | /live/domains/*/tls |
| Querylivedomainheaderrules | 查询直播域名HTTP头部控制配置 | GET | /live/domains/*/headerRules |
| Updatelivedomainheaderrules | 修改直播域名HTTP头部控制配置 | PUT | /live/domains/*/headerRules |
| Querylivedomainaccessctrls | 查询直播域名访问控制配置 | GET | /live/domains/*/accessCtrls |
| Updatelivedomainaccessctrls | 修改直播域名访问控制配置 | PUT | /live/domains/*/accessCtrls |
| Querylivedomainhls | 查询直播域名HLS配置 | GET | /live/domains/*/hls |
| Updatelivedomainhls | 修改直播域名HLS配置 | PUT | /live/domains/*/hls |
| Querylivedomainmisc | 查询直播域名Misc配置 | GET | /live/domains/*/misc |
| Updatelivedomainmisc | 修改直播域名Misc配置 | PUT | /live/domains/*/misc |
| Querylivedomainpublishreports | 查询直播域名推流汇报 | GET | /live/domains/*/publishReports |
| Updatelivedomainpublishreports | 修改直播域名推流汇报 | PUT | /live/domains/*/publishReports |
| Querylivedomaindetail | 查询直播域名详情 | GET | /live/domains/* |
| Addlivedomain | 新增直播域名 | POST | /live/domains |
| Updatelivedomain | 修改直播域名配置 | PUT | /live/domains/* |
| Querydomainrangefollowconfig | 查询域名的回源策略。包括：Rangel回源、301和302回源跟随 | GET | /api/domain/range-follow-config/* |
| Updatevariableconfig | 通过接口自助修改【变量】配置。接口url的*可为域名名称或域名id。 | PUT | /api/config/variable/* |
| Queryvariableconfig | 通过接口自助查询【变量】配置。接口url的*可为域名名称或域名id。 | GET | /api/config/variable/* |
| Querydomain | 查询域名配置 | GET | /api/si/domain |
| Querycdnwcontractdomains | 查询韩分合同与域名关系 | GET | /api/cdnw/contract/domains |
| Querycdnwcontractdomainsbycustomer | 查询韩分合同与域名关系（按客户） | POST | /api/cdnw/contract/domain |