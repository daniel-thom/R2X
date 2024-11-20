# coding: utf-8

"""
PowerSystemModels

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: 1.0.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from infrasys import Component

from pydantic import BaseModel, ConfigDict, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.cost_curve_value_curve import CostCurveValueCurve
from openapi_client.models.fuel_curve_fuel_cost import FuelCurveFuelCost
from openapi_client.models.input_output_curve import InputOutputCurve
from typing import Optional, Set
from typing_extensions import Self


class FuelCurve(Component):
    """
    FuelCurve
    """  # noqa: E501

    fuel_cost: FuelCurveFuelCost
    power_units: StrictStr
    value_curve: CostCurveValueCurve
    variable_cost_type: Optional[StrictStr] = None
    vom_cost: InputOutputCurve
    __properties: ClassVar[List[str]] = [
        "fuel_cost",
        "power_units",
        "value_curve",
        "variable_cost_type",
        "vom_cost",
    ]

    @field_validator("power_units")
    def power_units_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(["SYSTEM_BASE", "DEVICE_BASE", "NATURAL_UNITS"]):
            raise ValueError("must be one of enum values ('SYSTEM_BASE', 'DEVICE_BASE', 'NATURAL_UNITS')")
        return value

    @field_validator("variable_cost_type")
    def variable_cost_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(["FUEL"]):
            raise ValueError("must be one of enum values ('FUEL')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of FuelCurve from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of fuel_cost
        if self.fuel_cost:
            _dict["fuel_cost"] = self.fuel_cost.to_dict()
        # override the default output from pydantic by calling `to_dict()` of value_curve
        if self.value_curve:
            _dict["value_curve"] = self.value_curve.to_dict()
        # override the default output from pydantic by calling `to_dict()` of vom_cost
        if self.vom_cost:
            _dict["vom_cost"] = self.vom_cost.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FuelCurve from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "fuel_cost": FuelCurveFuelCost.from_dict(obj["fuel_cost"])
                if obj.get("fuel_cost") is not None
                else None,
                "power_units": obj.get("power_units"),
                "value_curve": CostCurveValueCurve.from_dict(obj["value_curve"])
                if obj.get("value_curve") is not None
                else None,
                "variable_cost_type": obj.get("variable_cost_type"),
                "vom_cost": InputOutputCurve.from_dict(obj["vom_cost"])
                if obj.get("vom_cost") is not None
                else None,
            }
        )
        return _obj
