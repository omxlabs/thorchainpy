from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeygenMetricNodeKeygenMetric")


@attr.s(auto_attribs=True)
class KeygenMetricNodeKeygenMetric:
    """
    Attributes:
        address (Union[Unset, str]):
        tss_time (Union[Unset, str]):
    """

    address: Union[Unset, str] = UNSET
    tss_time: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        address = self.address
        tss_time = self.tss_time

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address is not UNSET:
            field_dict["address"] = address
        if tss_time is not UNSET:
            field_dict["tss_time"] = tss_time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        address = d.pop("address", UNSET)

        tss_time = d.pop("tss_time", UNSET)

        keygen_metric_node_keygen_metric = cls(
            address=address,
            tss_time=tss_time,
        )

        keygen_metric_node_keygen_metric.additional_properties = d
        return keygen_metric_node_keygen_metric

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
