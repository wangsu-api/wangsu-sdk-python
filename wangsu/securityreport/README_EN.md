# Wangsu SDK for Python

This SDK provides Python interfaces to interact with Wangsu API services.

## Installation

Install the SDK using pip:

```bash
pip install wangsu-sdk-python
```

Install the SDK for a specific product category using pip:

```bash
pip install wangsu-sdk-python-securityreport
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
from wangsu.securityreport.models import *

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
| Queryccattackqps | Query CC Attack QPS | POST | /soc/api/report/Queryccattackqps |
| Getwafrequestandattackevent | Query the requests statistics and key incidents statistics. | POST | /api/waf/report/query-total-request |
| Getwafattacktrend | Query the trend of waf attack. | POST | /api/waf/report/query-attack-hit-trend |
| Getwafattackevent | Query the key incidents of domain. | POST | /api/waf/report/query-attack-event-list |
| Getwafattackeddomain | Query the attacked domain. | POST | /api/waf/report/query-attacked-domain-list |
| Getwafattackedurl | Query the attacked url. | POST | /api/waf/report/query-attacked-url-list |
| Getdistributionofwafattacktype | Query the distribution of waf attack type. | POST | /api/waf/report/query-top-by-attack-type |
| Getwaftriggerrulelist | Query the triggered rules and policies. | POST | /api/waf/report/query-trrigger-rule-list |
| Getwafpolicydetails | Query the configuration of waf policy. | POST | /api/waf/report/query-last-attack-info |
| Getwafattackip | Query the top attack ip of waf. | POST | /api/waf/report/query-attack-ip-list |
| Getdistributionofwafattacksource | Query the distribution of waf attack source. | POST | /api/waf/report/query-attack-country-list |
| Getwafdomainhistory | Query waf historical domains. | POST | /api/waf/report/query-waf-history-domain-list |
| Queryccattackdetails | CC Attack Details | POST | /soc/wss_report/shieldOverview/ccAttackDetails |
| Queryddosattackdetails | DDoS Attack Details | POST | /soc/wss_report/shieldOverview/ddosAttackDetails |
| Getdomainbotvisitdetails | Get the total number of domain requests, bot requests, bot relief attack requests, and Top5 bot type requests | POST | /api/bot/report/bot-visit-domain |
| Getbotrequestoverviewdata | Get the overview data, including: total requests, known bot type attacks, unknown bot type attacks, and bot relief attacks | POST | /api/bot/report/request-visit |
| Getbotrequeststatisticperdomain | Get the top number of  bot  requests  by domain | POST | /api/bot/report/bot-visit-domain-top |
| Getbotrequesttypedistributedata | Get the bot request type distribution data of the specified domain | POST | /api/bot/report/attack-type-distribute |
| Getbotaccessurltopdata | Get the TOP data of the request URL of the specified domain | POST | /api/bot/report/top-url |
| Getbotrequestsourceiptopdata | get the bot request IP TOP data of the specified domain | POST | /api/bot/report/top-ip |
| Getbotrequestreferertopdata | Get the request  Referer TOP data | POST | /api/bot/report/top-referer |
| GetbotrequestuseragentTopdata | Get the  request top data for user agent | POST | /api/bot/report/top-ua |
| Getbotrequestsourcedistributiondata | Getbotrequestsourcedistributiondata | POST | /api/bot/report/top-area |
| Getbotrequesttrendsandtriggerrulesdata | Get Bot Request Trends And Rules Top Data | POST | /api/bot/report/trend-rule |
| Getacttypedistributiondata | Get the bot protection action type distribution data | POST | /api/bot/report/act-type-distribute |
| Getbotruletypetopdata | Get the bot rule data | POST | /api/bot/report/top-rule-type |
| Getapieventlogs | Get API event logs. | POST | /api/sam/attack-log/query-attack-log |
| Getapinumber | The number of defined api. | POST | /api/sam/view-api-count |
| Getriskeventnumber | The number of risk events. | POST | /api/sam/view-attack-count |
| Getriskeventtop5 | Get risk event Top5 | POST | /api/sam/view-attack-type-top5 |
| Getactiveapitop5 | Get active APITop5. | POST | /api/sam/view-call-api-top5 |
| Getprivacystatusdistribution | Get privacy status distribution. | POST | /api/sam/view-conceal-count |
| Getconsumernumber | The number of consumers. | POST | /api/sam/view-consumer-count |
| Getrequesttrend | The trend of requests | POST | /api/sam/view-request-trend |
| Gettotalrequestnumber | The total number of requests | POST | /api/sam/view-total-call-count |
| Getrulestatusstatistics | Query the rule status statistics.<br> | POST | /api/waf/report/get-ruleStatus-statistics |
| Queryeventtrend | Query traffic trends (by requests). | POST | /api/v1/overview/trend-info |
| Listattacklogs | Query attack logs by policy type or by specified hostnames. | POST | /api/v1/attack-log/attack-log-list |
| Gettrendsbyrps | Get traffic trends (by rps). | POST | /api/v1/overview/trend-info-qps |
| Queryattacklogdetailinfo | Query attack log details. | POST | /api/v1/attack-log/all-detail-info |
| Getoriginalrequestinformation | Get the original request information of the attack log. | POST | /api/v1/attack-log/original-request-info |
| Gettriggeredwafmanagedrules | Return a list of WAF managed rules that have been triggered and how many times they have been triggered. | POST | /api/v1/situation/waf-rule-hit |
| Gettriggeredddosmanagedrules | Return a list of DDoS managed rules that have been triggered and how many times they have been triggered. | POST | /api/v1/situation/ddos-rule-hit |
| Gettriggeredratelimitingrules | Return a list of Rate limiting rules that have been triggered and how many times they have been triggered. | POST | /api/v1/situation/rate-limit-rule-hit |
| Gettriggeredcustomrules | Return a list of custom rules that have been triggered and how many times they have been triggered. | POST | /api/v1/situation/customize-rule-hit |
| Gettopattacktargetsbyhostname | Get the most attacked hostnames. | POST | /api/v1/situation/target-domain |
| Gettopattacktargetsbypath | Get the most attacked path. | POST | /api/v1/situation/target-url |
| Gettopattacksourcesforclientips | Obtain the Top data of attack sources, you can see which client IPs the attack requests come from. | POST | /api/v1/situation/source-ip-top |
| Gettopattacksourcesforglobal | Obtain the Top data of global attack sources, you can see which countries/regions the attack requests come from. | POST | /api/v1/situation/source-country-top |
| Gettopattacksourcesforchinamainland | Obtain the Top data of attack sources in Mainland China, you can see which cities the attack requests come from. | POST | /api/v1/situation/source-province-top |
| Getsummaryrequests | Get the number of requests, including total requests, mitigated requests, monitored requests, and the whitelisted requests. | POST | /api/v1/overview/event-summary |
| Dmsthreatenanalysisattackedurls | url | POST | /api/v1/dms-threaten-analysis/attacked-urls |
| Getinfrastructureloglist | Get a list of infrastructure protection logs. | POST | /api/v1/csec-attack-log/get-infrastructure-log-list |
| Getl7ddosanalysisattackiplistv2 | Obtain attack ip list(L7 DDoS Analysis). | POST | /api/v2/dms-threaten-analysis/v2/attack-ips |
| Getl7ddosanalysisattackedhostnamelistv2 | Obtain attacked hostname list(L7 DDoS Analysis). | POST | /api/v2/dms-threaten-analysis/v2/attacked-domains |
| Getl7ddosanalysisattackedurllistv2 | Obtain attacked url list(L7 DDoS Analysis) | POST | /api/v2/dms-threaten-analysis/v2/attacked-urls |
| L4ddosevent | Obtain L3/4 DDOS events. | POST | /api/v1/dms-overview/ddos-event |
| L4ddostrend | Obtain data related to the L3/4 DDoS attack trend. | POST | /api/v1/dms-overview/ddos-trend |
| L7ddosevents | <br>Obtain L7 DDoS events. | POST | /api/v2/dms-overview/v2/cc-event |
| L7ddostrend | Obtain data related to the L7 DDoS attack trend. | POST | /api/v2/dms-overview/v2/cc-trend |
| Gettoppoliciestriggered | Gets the number of triggers for each policy type. | POST | /api/v1/overview/event-distribution |