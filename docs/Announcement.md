# Announcement


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sequence_number** | **str** | 一連番号 | 
**registrated_number** | **str** | 登録番号 | 
**process** | **str** | 事業者処理区分 | 
**correct** | **str** | 訂正区分 | 
**kind** | **str** | 人格区分 | 
**country** | **str** | 国内外区分 | 
**latest** | **str** | 最新履歴 | 
**registration_date** | **date** | 登録年月日 | 
**update_date** | **date** | 更新年月日 | 
**disposal_date** | **str** | 取消年月日 | 
**expire_date** | **str** | 失効年月日 | 
**address** | **str** | 本店又は主たる事務所の所在地（法人） | 
**address_prefecture_code** | **str** | 本店又は主たる事務所の所在地都道府県コード（法人） | 
**address_city_code** | **str** | 本店又は主たる事務所の所在地市区町村コード（法人） | 
**address_request** | **str** | 本店又は主たる事務所の所在地（公表申出） | 
**address_request_prefecture_code** | **str** | 本店又は主たる事務所の所在地都道府県コード（公表申出） | 
**address_request_city_code** | **str** | 本店又は主たる事務所の所在地市区町村コード（公表申出） | 
**kana** | **str** | 日本語（カナ） | 
**name** | **str** | 氏名又は名称 | 
**address_inside** | **str** | 国内において行う資産の譲渡等に係る事務所、事業所その他これらに準ずるものの所在地 | 
**address_inside_prefecture_code** | **str** | 国内において行う資産の譲渡等に係る事務所、事業所その他これらに準ずるものの所在地都道府県コード | [optional] 
**address_inside_city_code** | **str** | 国内において行う資産の譲渡等に係る事務所、事業所その他これらに準ずるものの所在地市区町村コード | 
**trade_name** | **str** | 主たる屋号 | 
**popular_name_previous_name** | **str** | 通称・旧姓 | 

## Example

```python
from kendama.models.announcement import Announcement

# TODO update the JSON string below
json = "{}"
# create an instance of Announcement from a JSON string
announcement_instance = Announcement.from_json(json)
# print the JSON string representation of the object
print Announcement.to_json()

# convert the object into a dict
announcement_dict = announcement_instance.to_dict()
# create an instance of Announcement from a dict
announcement_form_dict = announcement.from_dict(announcement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


