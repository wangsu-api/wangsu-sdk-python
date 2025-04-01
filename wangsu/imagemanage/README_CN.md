# Wangsu SDK for Python

此 SDK 提供与网宿 API 服务交互的 Python 接口。

## 安装

使用 pip 安装 SDK：

```bash
pip install wangsu-sdk-python
```
使用 pip 安装特定产品分类的 SDK：

```bash
pip install wangsu-sdk-python-imagemanage
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
from wangsu.imagemanage.models import *

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
| Vmpqueryimage | 查询用户可以使用的镜像列表。显示出的镜像资源列表包括用户自定义的镜像及边缘计算平台提供的公共镜像。 | GET | /vmp/images |
| Vmpcreateimage | 支持将某个虚拟机系统盘制作成镜像，之后便可将其用于创建新的虚拟机。建议在制作镜像期间关闭虚拟机或者停止虚拟机上的应用或服务，以免影响镜像数据的完整性，待镜像制作完成，再启动虚拟机及其应用。此类操作创建的镜像在镜像查询接口中返回的镜像属主是SNAPSHOT，表示用虚拟机快照做的镜像。 | POST | /vmp/images |
| Vmpremoveimage | 删除您自定义镜像，删除镜像不影响已经创建的虚拟机，只是后续不能再使用该镜像创建新的虚拟机。您只能删除自己创建的自定义镜像，其他客户的自定义镜像以及公共镜像不能删除。 | DELETE | /vmp/images/* |
| Deployvmpimagepreheating | 用于提取预热客户私有镜像，该接口为异步接口，镜像预热结果需另外查询 | PUT | /vmp/images/preHeating |
| Queryvmpimagepreheatingstate | 用于查询镜像预热状态 | GET | /vmp/images/preHeatingInfo/* |
| Createharborproject | 创建harbor项目 | POST | /openapi/custom/v1/harbors/project |
| Updateharborproject | 更新harbor项目 | PUT | /openapi/custom/v1/harbors/project |
| Deleteharborproject | 删除harbor项目 | DELETE | /openapi/custom/v1/harbors/project/* |
| Getharborproject | 查询harbor项目详情 | GET | /openapi/custom/v1/harbors/project/* |
| Listharborproject | 查询harbor项目列表 | GET | /openapi/custom/v1/harbors/project |
| Createharboruser | 创建harbor用户 | POST | /openapi/custom/v1/harbors/user |
| Resetharboruserpwd | 重置harbor用户密码 | PUT | /openapi/custom/v1/harbors/user |
| Deleteharboruser | 删除harbor用户 | DELETE | /openapi/custom/v1/harbors/user/* |
| Getharboruser | 查询harbor用户详情 | GET | /openapi/custom/v1/harbors/user/* |
| Listharboruser | 查询harbor用户列表 | GET | /openapi/custom/v1/harbors/user |
| Getimagedetail | 查询镜像详细信息 | GET | /openapi/custom/v1/harbors/images/detail |
| Listimagepulljob | 列出用户所有ImagePullJob | GET | /apis/apps.kruise.io/v1alpha1/namespaces/*/imagepulljobs |
| Getimagepulljob | 查询ImagePullJob的详细信息 | GET | /apis/apps.kruise.io/v1alpha1/namespaces/*/imagepulljobs/* |
| Createimagepulljob | 创建ImagePullJob | POST | /apis/apps.kruise.io/v1alpha1/namespaces/*/imagepulljobs |
| Updateimagepulljob | 替换ImagePullJob | PUT | /apis/apps.kruise.io/v1alpha1/namespaces/*/imagepulljobs/* |
| Deleteimagepulljob | 删除ImagePullJob | DELETE | /apis/apps.kruise.io/v1alpha1/namespaces/*/imagepulljobs/* |
| Patchimagepulljob | 部分更新ImagePullJob | PATCH | /apis/apps.kruise.io/v1alpha1/namespaces/*/imagepulljobs/* |
| Deleteimagetag | 删除镜像 | DELETE | /openapi/custom/v1/harbors/images/tag |
| Createoemimage | 通过该接口可以为某个实例创建OEM镜像。 | POST | /ephone/oemImages/create |
| Queryoemimage | 用于查询指定的边缘云手机OEM镜像列表 | GET | /ephone/oemImages/list |
| Manageoemimage | 指定边缘云手机OEM镜像进行操作，目前仅支持删除操作 | POST | /ephone/oemImages/action |