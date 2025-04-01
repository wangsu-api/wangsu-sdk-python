# Wangsu SDK for Python

此 SDK 提供与网宿 API 服务交互的 Python 接口。

## 安装

使用 pip 安装 SDK：

```bash
pip install wangsu-sdk-python
```
使用 pip 安装特定产品分类的 SDK：

```bash
pip install wangsu-sdk-python-securitypolicy
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
from wangsu.securitypolicy.models import *

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
| Queryprotectionmodeforwafdomain | 查询WAF域名防护模式。 | POST | /api/waf/domain/query-domain-st |
| Getblockpagesetting | 查询拦截页面定义。 | POST | /api/waf/domain/query-block-page-conf |
| Updateblockpagesetting | 修改拦截页面定义。 | POST | /api/waf/domain/update-block-page-conf |
| Getbuiltinrulelist | 查询内置规则列表。 | POST | /api/waf/template/rule/list-page |
| Getbuiltinruleinfo | 查询内置规则详情。 | POST | /api/waf/template/rule/detail |
| Createbuiltinrule | 新增内置规则。 | POST | /api/waf/template/rule/add |
| Updatebuiltinrule | 修改内置规则。 | POST | /api/waf/template/rule/update |
| Associatedomainsforbuiltinrule | 添加内置规则关联域名。 | POST | /api/waf/template/rule/add-rela |
| Removedomainsforbuiltinrule | 从指定的内置规则中移除对应的域名。 | POST | /api/waf/template/rule/remove-rela |
| Getcustomrulelist | 查询自定义规则列表。 | POST | /api/waf/custom/rule/list-page |
| Createcustomrule | 新增自定义规则。 | POST | /api/waf/custom/rule/add |
| Updatecustomrule | 修改自定义规则。 | POST | /api/waf/custom/rule/update |
| Deletecustomrule | 删除自定义规则。 | POST | /api/waf/custom/rule/delete |
| Associatedomainsforcustomrule | 添加自定义规则关联域名。 | POST | /api/waf/custom/rule/add-rela |
| Removedomainsforcustomrule | 从指定的自定义规则中移除对应的域名。 | POST | /api/waf/custom/rule/remove-rela |
| Getruleexceptionlist | 查询规则例外的规则列表。 | POST | /api/waf/template/rule/white/list-page |
| Createruleexception | 新增规则例外。 | POST | /api/waf/template/rule/white/add |
| Updateruleexception | 修改规则例外。 | POST | /api/waf/template/rule/white/update |
| Deleteruleexception | 删除规则例外。 | POST | /api/waf/template/rule/white/delete |
| Associatedomainsforruleexception | 添加规则例外关联域名。 | POST | /api/waf/template/rule/white/add-rela |
| Removedomainsforruleexception | 从指定的规则例外中移除对应的域名。 | POST | /api/waf/template/rule/white/remove-rela |
| Querycustomruleconfiguration | 查询自定义规则配置（安全策略-频率限制-自定义规则） | POST | /dms/api/getDomainRateLimitConfig |
| Updateaslconfig | 修改自定义规则配置（仅支持单个域名） | POST | /dms/api/UpdateL7DomainAslConfig |
| Getcrawlergood | 查询Bot情报 | POST | /api/bot/domainConfig/get-crawler-good |
| Querybotfeatureverification | 查询Bot特性检测 | POST | /api/bot/domainConfig/get-bot-challenge |
| Queryfingerprintanalysis | 查询指纹分析 | POST | /api/bot/domainConfig/get-fingerprint-challenge |
| Querycaptchaverification | 查询验证码校验 | POST | /api/bot/domainConfig/get-captcha-challenge |
| Getbehavioranalyse | 查询业务流分析 | POST | /api/bot/domainConfig/get-behavior-analyse |
| Getblockpage | 查询拦截页面 | POST | /api/bot/domainConfig/get-block-page |
| Deploycrawlergood | 部署Bot情报。注:该接口需要全量提交数据 | POST | /api/bot/domainConfig/deploy-crawler-good |
| Deploybotfeatureverification | 部署Bot特性检测 | POST | /api/bot/domainConfig/deploy-bot-challenge |
| Deployfingerprintanalysis | 部署指纹分析 | POST | /api/bot/domainConfig/deploy-fingerprint-challenge |
| Deploycaptchaverification | 部署验证码校验 | POST | /api/bot/domainConfig/deploy-captcha-challenge |
| Deploybehavioranalyse | 部署业务流分析。注:该接口需要全量提交数据 | POST | /api/bot/domainConfig/deploy-behavior-analyse |
| Deployblockpage | 部署拦截页面 | POST | /api/bot/domainConfig/deploy-block-page |
| Createconsumer | 新增消费方。 | POST | /api/sam/consumers/add |
| Editconsumer | 编辑消费方。 | POST | /api/sam/consumers/edit |
| Deleteconsumer | 删除消费方。 | POST | /api/sam/consumers/delete |
| Getconsumerlist | 获取消费方列表。 | POST | /api/sam/consumers/list |
| Getconsumerinfo | 获取消费方信息。 | GET | /api/sam/consumers |
| Getapiassetlist | 获取API资产列表 | POST | /api/sam/api-discovery/list |
| Getapiassetdetail | 获取API资产详情。 | POST | /api/sam/api-discovery/detail |
| Reportincorrectapiasset | 上报错误的API资产发现数据。 | POST | /api/sam/api-discovery/false-marking |
| Createandactiveapi | 新增并激活API。 | POST | /api/sam/api/add-active |
| Createquotarule | 新增配额规则。 | POST | /api/sam/policy-quota/add |
| Editquotarule | 修改配额规则。 | POST | /api/sam/policy-quota/edit |
| Deletequotarule | 删除配额规则。 | POST | /api/sam/policy-quota/delete |
| Getapilist | 获取api列表。 | POST | /api/sam/api/list |
| Getquotarulelist | 获取配额规则列表。 | GET | /api/sam/policy-quota/list |
| Deleteapi | 删除API。 | POST | /api/sam/api/delete |
| Editandactiveapi | 编辑API并部署激活。 | POST | /api/sam/api/edit |
| Createconcurrencylimitrule | 新增限流规则。 | POST | /api/sam/policy-flow/add |
| Editconcurrencylimitrule | 修改限流规则。 | POST | /api/sam/policy-flow/edit |
| Deleteconcurrencylimitrule | 删除限流规则。 | POST | /api/sam/policy-flow/delete |
| Getconcurrencylimitrulelist | 获取限流规则列表。 | GET | /api/sam/policy-flow/list |
| Queryaccesscontrolrulelist | 查询Bot规则 | POST | /api/bot/customAccessControl/get-rule-listcmm |
| Wssmpnetworkserviceadd | 非网站业务规则新增 | POST | /soc/WssMPTcpService/add |
| Wssmpnetworkservicedelete | 非网站业务规则删除 | POST | /soc/WssMPTcpService/delete |
| Wssmpnetworkserviceupdate | 非网站业务规则修改 | POST | /soc/WssMPTcpService/update |
| Wssmpnetworkservicequery | 非网站业务规则查询 | POST | /soc/WssMPTcpService/query |
| Deletebuiltinrule | 删除内置规则。 | POST | /api/waf/policy/delete-builtInRule |
| Setdefaultbuiltinrule | 设置默认内置规则。<br> | POST | /api/waf/policy/set-default-builtInRule |
| Getintelligentanalysislist | 查询规则托管列表。 | POST | /api/waf/policy/get-intelligentAnalysis-list |
| Rejectintelligentanalysis | 拒绝规则托管建议。 | POST | /api/waf/policy/reject-intelligentAnalysis |
| Deleteintelligentanalysis | 删除规则托管建议。 | POST | /api/waf/policy/delete-intelligentAnalysis |
| Queryexactrulelist(accessControl) | 查询规则列表（精准访问控制） | POST | /api/bot/exact/query-exact-rule-list |
| Querydomainlistbyrulename(accessControl) | 查询规则关联域名列表（精准访问控制） | POST | /api/bot/exact/query-domainlist-by-rulename |
| Addexactrule(accessControl) | 添加规则（精准访问控制） | POST | /api/bot/exact/add-exact-rule |
| Editexactrule(accessControl) | 编辑规则（精准访问控制） | POST | /api/bot/exact/edit-exact-rule |
| Deleteexactrule(accessControl) | 删除规则（精准访问控制） | POST | /api/bot/exact/delete-exact-rule |
| Batchassiociatedexactrule(accessControl) | 批量添加域名（精准访问控制） | POST | /api/bot/exact/batch-assiociated-exact-rule |
| Batchremoveexactrule(accessControl) | 批量移除域名（精准访问控制） | POST | /api/bot/exact/batch-remove-exact-rule |
| Queryexactrulelistbydomain(accessControl) | 根据域名查询规则列表（精准访问控制） | POST | /api/bot/exact/query-exact-rulelist-by-domain |
| CcAttackTopIp | CC攻击TOP IP接口 | POST | /soc/wss_report/threatenAnalysis/attackIps |
| Updatedomainbaseinfo | 修改域名基础开关/模式信息。 | POST | /api/v1/dms/ddosProtect/updateDomainBaseInfo |
| Querydomainbuiltinrules | 查询域名内置规则 | POST | /api/v1/dms/ddosProtect/queryDomainBuiltInRules |
| Updatedomainbuiltinrules | 修改域名内置规则 | POST | /api/v1/dms/ddosProtect/updateDomainBuiltInRules |
| Sharedomainbaseprotectconfig | 跨域名部署基础配置 | POST | /api/v1/dms/ddosProtect/shareDomainBaseProtectConfig |
| Sharedmsbuiltinrulesconfig | 跨域名部署全局内置规则 | POST | /api/v1/dms/ddosProtect/shareDmsBuiltInRulesConfig |
| Sharedmsnativeappapiconfig | 跨域名部署例外api | POST | /api/v1/dms/ddosProtect/shareDmsNativeAppApiConfig |
| Queryhostnamebaseinfo | 查询域名基础策略。 | POST | /api/v1/dms/ddosProtect/queryDomainBaseInfo |
| Queryadaptiveprotectionrules | 查询域名AI智能防护规则。 | POST | /api/v1/dms/ddosProtect/queryDomainAIRules |
| Updateadaptiveprotectionrules | 修改域名AI智能防护规则 | POST | /api/v1/dms/ddosProtect/updateDomainAIRules |
| Queryhostnameappapiexceptions | 查询域名关联的共享配置-App/API例外 | POST | /api/v1/dms/ddosProtect/queryDomainAppApiExceptionRules |
| Removehostnameappapiexceptions | 域名移除共享配置-APP/API例外 | POST | /api/v1/dms/ddosProtect/removeDomainAppApiExceptionRules |
| Hostnameimportappapiexceptions | 域名引入App/API例外 | POST | /api/v1/dms/ddosProtect/relateDomainAppApiExceptionRules |
| Addcustomrule | 域名新增新增自定义规则（频率限制） | POST | /api/v1/dms/ddosProtect/addCustomRule |
| Updatecustomrule | 修改自定义规则（频率限制） | POST | /api/v1/dms/ddosProtect/updateCustomRule |
| Deletecustomrule | 删除自定义规则（频率限制） | POST | /api/v1/dms/ddosProtect/deleteCustomRule |
| Customblockedpagesettings | 域名自定义拦截页面设置 | POST | /api/v1/dms/ddosProtect/customBlockedPageSettings |
| Listnonsharedwafruleexceptionsforwafrules | 返回WAF规则的例外配置，包括“来源：手动添加”和“来源：建议”的例外配置。 | POST | /api/v1/waf/rule-exception/list-normal |
| Listhosnamesofnonlatestrulesetversion | 返回规则集版本不是最新版本的域名。 | GET | /api/v1/waf/conf/base/get-upgrade-domain-list |
| Listupgradedetails | 返回指定域名待更新的WAF规则信息，包括规则的名称、规则类型、描述等信息。 | POST | /api/v1/waf/rule/get-upgrade-rule-list |
| Upgradewafruleset | 将指定域名的WAF规则集升级到最新版本。 | POST | /api/v1/waf/rule/batch/upgrade |
| Listwafrules | 根据规则ID/规则名称/规则描述/漏洞编号查询特定的WAF规则。 | POST | /api/v1/waf/rule/get-rule-list |
| Updateactionforwafmanagedrules | 修改WAF内置规则的动作。 | POST | /api/v1/waf/rule/batch/update |
| Listwafbasicconfigofhostnames | 返回指定域名的WAF防护模式、规则集模式和规则集版本号。 | POST | /api/v1/waf/conf/base/get-basic-conf-list |
| Updatemodeofwaf | 修改指定域名的防护模式和规则集模式。 | POST | /api/v1/waf/conf/base/update-basic-conf |
| Createexceptiontowafmanagedrules | 新增WAF内置规则的例外配置。 | POST | /api/v1/waf/rule-exception/add-normal |
| Associatesharewafruleexception | 将共享配置中的WAF例外关联给指定域名。 | POST | /api/v1/waf/rule-exception/add-share |
| Deleteexceptionforwafmanagedrules | 删除WAF内置规则的WAF规则例外。 | POST | /api/v1/waf/rule-exception/delete-normal |
| Updateexceptionforwafmanagedrules | 修改WAF内置规则的WAF规则例外。 | POST | /api/v1/waf/rule-exception/update |
| Deletesharedwafexceptionsassociatedwithwafmanagedrules | 删除WAF规则例外（来源：共享配置）。 | POST | /api/v1/waf/rule-exception/delete-share |
| Applyrecommendations | 将建议添加到例外。 | POST | /api/v1/waf/ai-rule-result/apply |
| Rejectrecommendations | 拒绝WAF规则例外建议。 | POST | /api/v1/waf/ai-rule-result/reject |
| Listrecommendations | 返回指定WAF规则的建议，包括待处理和已拒绝的建议。 | POST | /api/v1/waf/ai-rule-result/list |
| Listsharedwafruleexceptionsforwafrules | 返回指定WAF规则ID下的的例外配置（来源：共享配置）。 | POST | /api/v1/waf/rule-exception/list-share |
| Listdomaininfos | 获取域名信息列表。 | POST | /api/v1/common/sys-domain-info/get-list |
| Usingexistinghostnametoaddnewhostname | 使用已接入防护域名的配置接入新的域名。 | POST | /api/v1/common/sys-domain-info/add-refer-to-other-domain |
| Copypoliciestootherhostnames | 将指定域名的策略复制给其他域名。<br>注意：<br>1. 不允许复制给未开启防护的策略；<br>2. 自定义规则和频率限制中有引用已定义API的规则不支持复制，策略复制过程中将跳过此类规则。 | POST | /api/v1/common/sys-domain-info/copy-domain |
| Modifypolicystatus | 修改策略开关。 | POST | /api/v1/common/sys-domain-info/update-switch |
| Removeprotectedhostname | 移除“防护中”状态的域名。 | GET | /api/v1/common/sys-domain-info/remove |
| Usingsystemrecommendedaccessdomain | 使用系统建议接入域名。 | POST | /api/v1/common/sys-domain-info/add-sys-domain |
| Getbotfunctionswitch | 查询Bot管理功能开关。 | POST | /api/v1/bot-manage/get-function-switch |
| Updatebotfunctionswitch | 修改Bot管理功能开关。 | POST | /api/v1/bot-manage/update-function-switch |
| Creatratelimitingrule | 新增频率限制规则。 | POST | /api/v1/rate-limit/add-rule |
| Createwhitelistrule | 新增白名单规则。 | POST | /api/v1/common/whitelist/add |
| Updateratelimitingrule | 修改频率限制规则的配置。 | POST | /api/v1/rate-limit/update-rule |
| Updatewhitelistrule | 修改白名单规则的配置。 | POST | /api/v1/common/whitelist/update |
| Deletewhitelistrules | 删除白名单规则。 | POST | /api/v1/common/whitelist/delete |
| Addworkflowrule | 新增业业务流检测规则。 | POST | /api/v1/bot-manage/behavior/add-rule |
| Listratelimitingrules | 获取频率限制的规则列表。 | POST | /api/v1/rate-limit/get-rule-list |
| Updateworkflowrule | 修改业务流检测规则。 | POST | /api/v1/bot-manage/behavior/update-rule |
| Deleteratelimitingrules | 删除频率限制规则。 | POST | /api/v1/rate-limit/delete-rule-by-ids |
| Listworkflowrules | 查询业务流检测规则列表。 | POST | /api/v1/bot-manage/behavior/get-rule |
| Getratelimitingrulesforthesharedconfigurationasociatedwithhostname | 获取域名关联的共享配置的频率限制规则。 | POST | /api/v1/rate-limit/get-relation-by-domain |
| Deleteworkflowrule | 删除业务流检测规则。 | POST | /api/v1/bot-manage/behavior/delete-rule |
| Getthreatintelligencedomainconfig | 获取威胁情报域名配置。 | POST | /api/v1/common/intelligence/query-list |
| Updatethreatintelligencedomainconfig | 修改威胁情报域名配置。 | POST | /api/v1/common/intelligence/update |
| Getdomainapisecurityconfiguration | 获取域名API安全配置。 | POST | /api/v1/sam/api-defend/get-list-by-domains |
| Updatedomainapisecurityconfiguration | 修改域名API安全配置。 | POST | /api/v1/sam/api-defend/update-defend-action |
| Addcustomizerule | 新增自定义规则。 | POST | /api/v1/customize-rule/add |
| Listwhitelistrules | 获取白名单规则列表。 | POST | /api/v1/common/whitelist/query-list |
| Getwhitelistrulesforthesharedconfigurationasociatedwithhostname | 获取域名关联的共享配置的白名单规则。 | GET | /api/v1/common/whitelist/get-imported-share-config |
| Updateipblocksettings | 更新IP封禁的配置，拦截特定IP/IP段发起的请求。注意：将覆盖原来的配置。 | POST | /api/v1/policy-block/save-deploy-ip-block |
| Updatecustomrule | 修改自定义规则的配置。 | POST | /api/v1/customize-rule/update |
| Deletecustomrule | 删除自定义规则。 | POST | /api/v1/customize-rule/delete |
| Listcustomrules | 获取自定义规则列表。 | POST | /api/v1/customize-rule/get-list |
| Listipblocksettings | 返回指定域名已拦截的IP/IP段。 | POST | /api/v1/policy-block/get-ip-block-list |
| Listgeoblocksettings | 返回指定域名已拦截的国家和地区。 | POST | /api/v1/policy-block/get-geo-block-list |
| Listcustomrulesforsharedconfigurationassociatedwithhostname | 获取域名关联的共享配置的自定义规则。 | POST | /api/v1/customize-rule/get-import-share-rule |
| Updategeoblocksettings | 拦截来自特定国家/地区的请求。注意：将覆盖原来的配置。 | POST | /api/v1/policy-block/save-deploy-geo-block |
| Listdomaincustomizebots | 查询域名的自定义Bot列表。 | POST | /api/v1/bot-manage/get-domain-customize-bots-list |
| Updateconfigurationofattackerippunishment | 修改指定攻击IP惩罚规则的配置 。 | POST | /api/v1/waf/waf/ip-punishment/update |
| Listconfigurationofattackerippunishment | 获取指定域名的攻击IP惩罚配置。 | POST | /api/v1/waf/waf/ip-punishment/list |
| Disableallpolicies | 禁用指定域名的全部安全策略，被禁用的域名将不再进行安全检测。 | POST | /api/v1/common/sys-domain-info/close-all-policy-switch |
| Addwafcustomrule | 新增WAF自定义规则。 | POST | /api/v1/waf/waf/custom-rule/add-waf-domain-rule-custom |
| Deletewafcustomrule | 删除WAF自定义规则。 | POST | /api/v1/waf/waf/custom-rule/del-waf-domain-rule-custom-list |
| Updatewafcustomrule | 修改WAF自定义规则。 | POST | /api/v1/waf/waf/custom-rule/update-waf-domain-rule-custom |
| Listwafcustom | 查询WAF自定义规则列表。 | POST | /api/v1/waf/waf/custom-rule/get-waf-domain-rule-custom-list |
| Getwafcustomruledetails | 获取WAF自定义规则详情。 | POST | /api/v1/waf/waf/custom-rule/get-waf-domain-rule-custom-detail |
| Updateknownbotsselectbotnames | 批量修改生效的已知Bot小类。 | POST | /api/v1/bot-manage/update-known-bots-select-bot-names |
| Listknownbots | 查询已知Bot列表。 | POST | /api/v1/bot-manage/get-known-bots |
| Updateknownbotsact | 批量修改已知Bot处理动作。 | POST | /api/v1/bot-manage/update-known-bots-act |
| Listuabots | 查询UA特征检测列表。 | POST | /api/v1/bot-manage/get-ua-bots |
| Updateuabotsselectbotnames | 批量修改生效的UA特征检测小类。 | POST | /api/v1/bot-manage/update-ua-bots-select-bot-names |
| Updateuabotsact | 批量修改UA特征检测处理动作。 | POST | /api/v1/bot-manage/update-ua-bots-act |
| Getresponsepageofdenyactiondetail | 获取基础配置-自定义拦截响应详情 | POST | /api/v1/other/sys-domain-basic/response/detail |
| Updateresponsepageofdenyactiondetail | 修改基础配置-自定义拦截响应详情 | POST | /api/v1/other/sys-domain-basic/response/update |
| Listhistoricalhostnames | 查询历史防护的域名。 | POST | /api/v1/other/domain/get-permanent-domain-list |