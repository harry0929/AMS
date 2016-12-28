# -*- coding: utf-8 -*-
import requests

from Web.models import Asset

url = "http://127.0.0.1:5000/api/v1/Asset/1"

# r = requests.get(url)
# r.encoding = 'utf-8'

# print(r.content)
#
# print dict["dept"]

# models = Asset.query.all()
#
# print len(models)
#
# if len(models) > 0:
#     arr = []
#     for m in models:
#         param = {}
#         param["id"] = m.id
#         param["code"] = m.code
#         param["name"] = m.name
#         param["supplier_name"] = None if m.supplier is None else m.supplier.name
#         param["manager_type"] = m.manager_type.name
#         param["asset_category"] = m.asset_category.name
#         param["purchase_date"] = m.purchase_date.strftime('%Y-%m-%d')
#         param["original_value"] = str(m.original_value)
#         param["depreciation_year"] = m.depreciation_year
#         param["department_name"] = m.department.name
#         param["position"] = m.position
#         param["remark"] = m.remark
#         arr.append(param)
#
#
# print json.dumps(arr, ensure_ascii= False)
#
# print type(models) == list

from Web.models import Asset

asset = Asset()
print(asset.validator(""))



