# Wangsu SDK for Python

This SDK provides Python interfaces to interact with Wangsu API services.

## Installation

Install the SDK using pip:

```bash
pip install wangsu-sdk-python
```

Install the SDK for a specific product category using pip:

```bash
pip install wangsu-sdk-python-domainconfigurtion
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
from wangsu.domainconfigurtion.models import *

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
| Updatedomainsrcstrategyforwplus | Set the back-to-origin configuration policy of the domain, including: advanced source, Rangel back-to-origin, 301 and 302 back-to-origin follow. | POST | /api/domain/setsrcconfig |
| Editdomainconfig | To modify configuration of the specified domain; both domain name and domain name ID are supported. | PUT | /api/domain/* |
| Updatetimecontrolservice | Modify Time anti-theft chain custom configuration item content | PUT | /api/config/timecontrol/* |
| Querytimecontrolservice | Query Time anti-theft chain custom configuration item content | GET | /api/config/timecontrol/* |
| Editdomainredirectconfig | Self-service through interface, url redirection function | PUT | /api/config/InnerRedirect/* |
| Edithttpheaderconfig | Through the interface self-implementation http header additions and deletions to the function, can be achieved in the cdn layer of personalized http header control, so that customers do not need to modify the source stationin this case, a custom http header and speedup are implemented. The interface * can be domain name or domain id. | PUT | /api/config/headermodify/* |
| Queryhttpheaderconfig | Query http header configuration via interface self - service. The interface * can be domain name or domain id. | GET | /api/config/headermodify/* |
| Editcachetimeconfig | The interface self-help implementation modifies the domain name cache time configuration, realizes the custom cache function according to the customer's request. Node cache is divided into regular cache and query string URl cache, where you can set the ca | PUT | /api/config/cachetime/* |
| Editantihotlinkingconfig | Modify the IP whitelist configuration under the domain name anti-theft chain through the interface self-service, and implement whitelist or blacklist control on the specific access IP. The interface * can be domain name or domain id. | PUT | /api/config/visitcontrol/* |
| Queryantihotlinkingconfig | Self-checking IP black and white list anti-theft chain configuration through interface. The interface * can be domain name or domain id. | GET | /api/config/visitcontrol/* |
| Updatesourceverificationconfig | Retweet back to the source with parameter authentication through the interface self-service, realize rtmp retweet back to the source, the edge can simulate the client with timestamp anti-leech parameters according to the encryption rules to retweet back to the source. | PUT | /api/config/sourceverification/* |
| Querysourceverificationconfig | Query retweet back to the source with parameter authentication configuration. | GET | /api/config/sourceverification/* |
| Updatecachebyresponseheaderconfig | The self-service implementation through the interface follows the source site caching rules. When there is a cache head, it is cached according to the source site caching head. When there is no cache head, it is not cached. | PUT | /api/config/cachebyrespheader/* |
| Querycachebyresponseheaderconfig | Self-query response header content caching rules through the interface. | GET | /api/config/cachebyrespheader/* |
| Addbanurltodomian | xxx | PUT | /api/basicconfig/illegalinformation |
| Predeploycachetimeconfig | Self-query node cache configuration configuration through interface | PUT | /api/predeploy/cachetime/* |
| Predeployredirectconfig | View internal redirect configuration | PUT | /api/predeploy/InnerRedirect/* |
| Queryapideployservice | Requests for new, modified, enabled, disabled, cancelled, restored, deleted, etc. for domain names | POST | /api/request/* |
| Updatecompressionconfig | Modify compress setting configurations. | PUT | /api/config/compresssetting/* |
| Querycompressionconfig | Get compress setting configurations. | GET | /api/config/compresssetting/* |
| Predeploycompressionconfig | Get compress setting configurations. | PUT | /api/predeploy/compresssetting/* |
| Queryhttpcodecasheconfig | Get http code cache configurations. | GET | /api/config/httpcodecache/* |
| Queryipv6config | Get whether a domain uses ipv6 resources. | GET | /api/domain/ipv6/* |
| Queryaccessspeedconfig | Get access speed limitation configurations. | GET | /api/config/accessspeed/* |
| Queryafterredirect | Query the file after the pull jump | GET | /api/config/afterredirect/* |
| Updateafterredirect | Modify the pull jump after the file | PUT | /api/config/afterredirect/* |
| Queryinnerredirect | View internal redirect configuration | GET | /api/config/InnerRedirect/* |
| Querycachetime | Self-service query of node cache configuration configuration through the interface. The * of the interface calling url can be the domain name or domain id. | GET | /api/config/cachetime/* |
| Editquerystringurlconfig | Modify query string setting configurations. | PUT | /api/config/querystring/* |
| Queryquerystringurlconfig | Through the interface, the query string settings can be modified by self-service, realizing the customized cache function. With the query string URL, you can set whether to cache multiple copies or cache the URL after removing the question mark (to increase the hit rate), and you can set whether to use the original request to return to the source, etc. The * of the interface calling url can be the domain name or domain id. | GET | /api/config/querystring/* |
| Updatetosauthorizationconfig | Modify tos access authorization configurations. The interface * can be domain name or domain id. | PUT | /api/config/tosaccess/* |
| Querytosauthorizationconfig | Get tos access authorization  configurations. The interface * can be domain name or domain id. | GET | /api/config/tosaccess/* |
| Edithttpcodecache | Modify http code cache configurations. | PUT | /api/config/httpcodecache/* |
| Queryamazons3authorizationconfig | Get amazon s3 access authorization  configurations. The interface * can be domain name or domain id. | GET | /api/config/amazons3access/* |
| Updateamazons3authorizationconfig | Modify amazon s3 access authorization configurations. The interface * can be domain name or domain id. | PUT | /api/config/amazons3access/* |
| Updatealiyunossauthorizationconfig | Modify Aliyun OSS access authorization configurations. The interface * can be domain name or domain id. | PUT | /api/config/ossaccess/* |
| Queryaliyunossauthorizationconfig | Get Aliyun OSS access authorization  configurations. The interface * can be domain name or domain id. | GET | /api/config/ossaccess/* |
| Editdomainproperty | Modify domain name properties, such as back source IP, back source host, and back source port. | POST | /api/domain/property/* |
| Queryignoreprotocol | Protocol caching and push configuration are ignored through interface self-service queries | GET | /api/config/ignoreprotocol/* |
| Editignoreprotocol | Modify ignore protocol cache and push configuration. | PUT | /api/config/ignoreprotocol/* |
| Editoriginuriandhost | Modify the source URI and host rewrite | PUT | /api/config/originrulesrewrites/* |
| Queryoriginuriandhost | Query back source URI and host rewrite | GET | /api/config/originrulesrewrites/* |
| Editwebsocketconfig | Self-modify the websocket switch configuration through the interface. The interface * can be domain name or domain id. | PUT | /api/config/websocket/* |
| Querywebsocketconfig | Self-query the websocket switch configuration via the interface. The interface * can be domain name or domain id. | GET | /api/config/websocket/* |
| Deletebanurls | the interface of delete the illegal masking | DELETE | /api/basicconfig/illegalinformation |
| Batchaddillegalinformation | Batch add domain's illegal information url. | PUT | /api/config/Batchaddillegalinformation |
| Batchdelillegalinformation | Batch delete domain's illegal information url. | DELETE | /api/config/Batchdelillegalinformation |
| Updatesingletranscodingconfigforwplus | Update Single Transcoding Configuration. The interface * can be domain name or domain id. | PUT | /api/config/transcodes/* |
| Querysingletranscodingconfigforwplus | Query Single Transcoding Configuration. The interface * can be domain name or domain id. | GET | /api/config/transcodes/* |
| Updateglobaltranscodingconfigforwplus | Update Global Transcoding Configuration. The interface * can be domain name or domain id. | PUT | /api/config/transcodeswitch/* |
| Queryglobaltranscodingconfigforwplus | Query Global Transcoding Configuration. The interface * can be domain name or domain id. | GET | /api/config/transcodeswitch/* |
| Querylivestreamingantihotlinkingconfig | Self-query the live-visitcontrol configuration via the interface. The interface * can be domain name or domain id. | GET | /api/config/live-visitcontrol/* |
| Updatelivevisitcontrolconfig | Self-modify the live-visitcontrol configuration through the interface. The interface * can be domain name or domain id. | PUT | /api/config/live-visitcontrol/* |
| Querylivestreamingtimestampantihotlinkingconfig | Query streaming media timestamp visit control. The interface * can be domain name or domain id. | GET | /api/config/live-timestampvisitcontrol/* |
| Editlivestreamingtimestampantihotlinkingconfig | Update streaming media timestamp visit control. The interface * can be domain name or domain id. | PUT | /api/config/live-timestampvisitcontrol/* |
| PredeployedStreamingTimestampVisitControl | PredeployedStreamingTimestampVisitControl. The interface * can be domain name or domain id. | PUT | /api/predeploy/live-timestampvisitcontrol/* |
| QueryCloudStorageBasicConfiguration | QueryCloudStorageBasicConfiguration.The interface * can be domain name or domain id. | GET | /api/config/cloudstorage/* |
| UpdateCloudStorageBasicConfiguration | Update recording basic configuration.The interface * can be domain name or domain id. | PUT | /api/config/cloudstorage/* |
| QueryRecordingBasicConfiguration | QueryRecordingBasicConfiguration.The interface * can be domain name or domain id. | GET | /api/config/recording/* |
| UpdateRecordingBasicConfiguration | UpdateRecordingBasicConfiguration.The interface * can be domain name or domain id. | PUT | /api/config/recording/* |
| Getbasicconfigurationofdomain | View the configuration of the specified domain. Both domain name and domain name ID are supported. | GET | /api/domain/* |
| UpdateScreenshotConfiguration | Modify screenshot basic configuration.The interface * can be domain name or domain id. | PUT | /api/config/screenshot/* |
| QueryScreenshotConfiguration | Query screenshot basic configuration.The interface * can be domain name or domain id. | GET | /api/config/screenshot/* |
| Queryappadomainportinfoforwplus | Get APPA domain config. | GET | /api/domainlist/appa |
| QueryBanUrlByDomain | query the blocked url list under a specified account, whick calls this api | POST | /api/config/banurl |
| Queryhttp2settingsconfigforwplus | Queryhttp2settingsconfigforwplus. The interface * can be domain name or domain id. | GET | /api/config/http2/* |
| Updatehttp2settingsconfigforwplus | Updatehttp2settingsconfigforwplus. The interface * can be domain name or domain id. | PUT | /api/config/http2/* |
| Enableordisablewafprotection | Enable or disable WAF protection | PUT | /api/domain/wafsecurity |
| Enableordisablebotprotection | Enable or disable Bot protection | PUT | /api/domain/botsecurity |
| UpdateCacheKeyConfiguration | UpdateCacheKeyConfiguration.The interface * can be domain name or domain id. | PUT | /api/config/cachekey/* |
| QueryCacheKeyConfiguration | QueryCacheKeyConfiguration.The interface * can be domain name or domain id. | GET | /api/config/cachekey/* |
| Editaccessspeedlimit | Editaccessspeedlimit | POST | /api/config/accessspeed/* |
| Enableordisabledmsprotection | UpdateDomainDmsStatusServiceForWplus | PUT | /api/domain/dmssecurity |
| Editback2originprotocolrewriteconfig | Update Back2Origin Protocol Rewrite Config	 | PUT | /api/config/back2originrewrite/* |
| Queryback2originprotocolrewriteconfig | Update Back2Origin Protocol Rewrite Config. | GET | /api/config/back2originrewrite/* |
| Updatestreamnotificationconfig | Update Stream Notification Config (Normal) | PUT | /api/config/streamnotification/* |
| Querystreamnotificationconfig | Query Stream Notification Config (Normal) | GET | /api/config/streamnotification/* |
| Querydomainbillingarea | Get domain's billing areas. | GET | /api/domain/billingarea/* |
| Updatedomaincertconfig | Set domain's certificate config, support SNI only. | PUT | /api/config/certificate/* |
| Addappadomain | Add APPA domain. | POST | /api/domain/appa |
| Updateappadomain | Update APPA domain. | PUT | /api/domain/appa/* |
| Getappadomainconfig | Get APPA domain config. | GET | /api/domain/appa/* |
| Querydomaincertconfig | Get domain's certificate config, support SNI only. | GET | /api/config/certificate/* |
| Pushnotifyaddress | Push notify address | PUT | /api/notifyaddress |
| Queryappacarryclientipconfig | Query APPA carry clientip config for specified domain. | GET | /api/config/appacarryclientip/* |
| Updatedomainmulticertconfig | Set domain's certificate config, support SNI and mutil SNI. | PUT | /api/config/certificate/v2/* |
| Updateipversionconfig | Set IPv4 and IPv6 resource for your domain. | PUT | /api/config/ipversion/* |
| Querylivedomainorigins | Query Live Domain Origins | GET | /live/domains/*/origins |
| Updatelivedomainorigins | Update Live Domain Origins | PUT | /live/domains/*/origins |
| Querylivedomainpagination | Query Live Domain Pagination | GET | /live/domains |
| Querylivedomaintls | Query Live Domain TLS | GET | /live/domains/*/tls |
| Updatelivedomaintls | Update Live Domain TLS | PUT | /live/domains/*/tls |
| Querylivedomainheaderrules | Query Live Domain Header Rules | GET | /live/domains/*/headerRules |
| Updatelivedomainheaderrules | Update Live Domain Header Rules | PUT | /live/domains/*/headerRules |
| Querylivedomainaccessctrls | Query Live Domain Access Ctrls | GET | /live/domains/*/accessCtrls |
| Updatelivedomainaccessctrls | Update Live Domain Access Ctrls | PUT | /live/domains/*/accessCtrls |
| Querylivedomainhls | Query Live Domain HLS Config | GET | /live/domains/*/hls |
| Updatelivedomainhls | Update Live Domain HLS Config | PUT | /live/domains/*/hls |
| Querylivedomainmisc | Query Live Domain Misc Configuration | GET | /live/domains/*/misc |
| Updatelivedomainmisc | Update Live Domain Misc Configuration | PUT | /live/domains/*/misc |
| Querylivedomainpublishreports | Query Live Domain Publish Reports Configuration | GET | /live/domains/*/publishReports |
| Updatelivedomainpublishreports | Update Live Domain Publishing Reports Configuration | PUT | /live/domains/*/publishReports |
| Querylivedomaindetail | Query Live Domain Detail Config | GET | /live/domains/* |
| Addlivedomain | Add Live Domain | POST | /live/domains |
| Updatelivedomain | Update Live Domain Configurations | PUT | /live/domains/* |
| Querydomainrangefollowconfig | Query the back-to-origin configuration policy of the domain, including: angel back-to-origin, 301 and 302 back-to-origin follow. | GET | /api/domain/range-follow-config/* |
| Updatevariableconfig | Update variable config. The interface * can be domain name or domain id.<br> | PUT | /api/config/variable/* |
| Queryvariableconfig | Query variable config. The interface * can be domain name or domain id. | GET | /api/config/variable/* |
| Querydomain | query domain configuration. | GET | /api/si/domain |
| Querycdnwcontractdomains | Querycdnwcontractdomains | GET | /api/cdnw/contract/domains |
| Querycdnwcontractdomainsbycustomer | Querycdnwcontractdomainsbycustomer | POST | /api/cdnw/contract/domain |