# coding: utf-8

"""
    国税庁API

    国税庁が提供するインボイス制度適格請求書発行事業者公表システムWeb-APIを使用するためのクライアントAPI(https://www.invoice-kohyo.nta.go.jp/web-api/index.html)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import date
from typing import Optional
from pydantic import BaseModel, Field, StrictStr, constr, validator

class Announcement(BaseModel):
    """
    Announcement
    """
    sequence_number: constr(strict=True, max_length=8, min_length=1) = Field(..., alias="sequenceNumber", description="一連番号")
    registrated_number: StrictStr = Field(..., alias="registratedNumber", description="登録番号")
    process: StrictStr = Field(..., description="事業者処理区分")
    correct: StrictStr = Field(..., description="訂正区分")
    kind: StrictStr = Field(..., description="人格区分")
    country: StrictStr = Field(..., description="国内外区分")
    latest: StrictStr = Field(..., description="最新履歴")
    registration_date: date = Field(..., alias="registrationDate", description="登録年月日")
    update_date: date = Field(..., alias="updateDate", description="更新年月日")
    disposal_date: StrictStr = Field(..., alias="disposalDate", description="取消年月日")
    expire_date: StrictStr = Field(..., alias="expireDate", description="失効年月日")
    address: constr(strict=True, max_length=600) = Field(..., description="本店又は主たる事務所の所在地（法人）")
    address_prefecture_code: StrictStr = Field(..., alias="addressPrefectureCode", description="本店又は主たる事務所の所在地都道府県コード（法人）")
    address_city_code: StrictStr = Field(..., alias="addressCityCode", description="本店又は主たる事務所の所在地市区町村コード（法人）")
    address_request: constr(strict=True, max_length=600) = Field(..., alias="addressRequest", description="本店又は主たる事務所の所在地（公表申出）")
    address_request_prefecture_code: StrictStr = Field(..., alias="addressRequestPrefectureCode", description="本店又は主たる事務所の所在地都道府県コード（公表申出）")
    address_request_city_code: StrictStr = Field(..., alias="addressRequestCityCode", description="本店又は主たる事務所の所在地市区町村コード（公表申出）")
    kana: constr(strict=True, max_length=500) = Field(..., description="日本語（カナ）")
    name: constr(strict=True, max_length=300) = Field(..., description="氏名又は名称")
    address_inside: constr(strict=True, max_length=300) = Field(..., alias="addressInside", description="国内において行う資産の譲渡等に係る事務所、事業所その他これらに準ずるものの所在地")
    address_inside_prefecture_code: Optional[StrictStr] = Field(None, alias="addressInsidePrefectureCode", description="国内において行う資産の譲渡等に係る事務所、事業所その他これらに準ずるものの所在地都道府県コード")
    address_inside_city_code: StrictStr = Field(..., alias="addressInsideCityCode", description="国内において行う資産の譲渡等に係る事務所、事業所その他これらに準ずるものの所在地市区町村コード")
    trade_name: constr(strict=True, max_length=200) = Field(..., alias="tradeName", description="主たる屋号")
    popular_name_previous_name: constr(strict=True, max_length=200) = Field(..., alias="popularName_previousName", description="通称・旧姓")
    __properties = ["sequenceNumber", "registratedNumber", "process", "correct", "kind", "country", "latest", "registrationDate", "updateDate", "disposalDate", "expireDate", "address", "addressPrefectureCode", "addressCityCode", "addressRequest", "addressRequestPrefectureCode", "addressRequestCityCode", "kana", "name", "addressInside", "addressInsidePrefectureCode", "addressInsideCityCode", "tradeName", "popularName_previousName"]

    @validator('process')
    def process_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('01', '02', '03', '04', '99'):
            raise ValueError("must be one of enum values ('01', '02', '03', '04', '99')")
        return value

    @validator('correct')
    def correct_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('0', '1', ''):
            raise ValueError("must be one of enum values ('0', '1', '')")
        return value

    @validator('kind')
    def kind_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('1', '2'):
            raise ValueError("must be one of enum values ('1', '2')")
        return value

    @validator('country')
    def country_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('1', '2', '3'):
            raise ValueError("must be one of enum values ('1', '2', '3')")
        return value

    @validator('latest')
    def latest_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('0', '1'):
            raise ValueError("must be one of enum values ('0', '1')")
        return value

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Announcement:
        """Create an instance of Announcement from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Announcement:
        """Create an instance of Announcement from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Announcement.parse_obj(obj)

        _obj = Announcement.parse_obj({
            "sequence_number": obj.get("sequenceNumber"),
            "registrated_number": obj.get("registratedNumber"),
            "process": obj.get("process"),
            "correct": obj.get("correct"),
            "kind": obj.get("kind"),
            "country": obj.get("country"),
            "latest": obj.get("latest"),
            "registration_date": obj.get("registrationDate"),
            "update_date": obj.get("updateDate"),
            "disposal_date": obj.get("disposalDate"),
            "expire_date": obj.get("expireDate"),
            "address": obj.get("address"),
            "address_prefecture_code": obj.get("addressPrefectureCode"),
            "address_city_code": obj.get("addressCityCode"),
            "address_request": obj.get("addressRequest"),
            "address_request_prefecture_code": obj.get("addressRequestPrefectureCode"),
            "address_request_city_code": obj.get("addressRequestCityCode"),
            "kana": obj.get("kana"),
            "name": obj.get("name"),
            "address_inside": obj.get("addressInside"),
            "address_inside_prefecture_code": obj.get("addressInsidePrefectureCode"),
            "address_inside_city_code": obj.get("addressInsideCityCode"),
            "trade_name": obj.get("tradeName"),
            "popular_name_previous_name": obj.get("popularName_previousName")
        })
        return _obj

