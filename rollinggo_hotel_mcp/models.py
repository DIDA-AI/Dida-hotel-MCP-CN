from typing import Any, Dict, List

from pydantic import BaseModel, Field


class CheckInParam(BaseModel):
    adultCount: int = Field(default=2, description="每间房成人数，整数，>=1，默认2。")
    checkInDate: str = Field(
        default=None,
        description="入住日期，格式 YYYY-MM-DD。建议始终传入合法未来日期。",
    )
    stayNights: int = Field(default=1, description="入住晚数，整数，>=1，默认1。")


class FilterOptions(BaseModel):
    distanceInMeter: int = Field(
        default=None,
        description="距离上限（米），整数，>0。仅当 place 为 POI 类位置时有实际筛选意义。",
    )
    starRatings: List[float] = Field(
        default=None,
        description="星级区间数组 [min, max]，0.0~5.0，步长0.5，且 min<=max。",
    )


class HotelTags(BaseModel):
    excludedTags: List[str] = Field(default=None, description="排除标签（命中即过滤）。")
    maxPricePerNight: float = Field(default=None, description="每晚价格上限（人民币，数值）。")
    minRoomSize: float = Field(default=None, description="房间最小面积下限（平方米，数值）。")
    preferredBrands: List[str] = Field(
        default=None,
        description="偏好品牌（软约束）。",
    )
    preferredTags: List[str] = Field(default=None, description="偏好标签（软约束，影响排序）。")
    requiredTags: List[str] = Field(default=None, description="必须命中标签（硬约束，未命中应被过滤）。")


class DateParam(BaseModel):
    checkInDate: str = Field(default=None, description="入住日期，格式 YYYY-MM-DD。建议传合法未来日期。")
    checkOutDate: str = Field(
        default=None,
        description="离店日期，格式 YYYY-MM-DD，必须晚于 checkInDate。",
    )


class OccupancyParam(BaseModel):
    adultCount: int = Field(default=2, description="每间房成人数，整数，>=1，默认2。")
    childAgeDetails: List[int] = Field(default=None, description="儿童年龄数组，如 [3,5]；长度应与 childCount 一致。")
    childCount: int = Field(default=0, description="每间房儿童数，整数，>=0，默认0。")
    roomCount: int = Field(default=1, description="房间数，整数，>=1，默认1。")


class LocaleParam(BaseModel):
    countryCode: str = Field(default="CN", description="国家二字码（ISO 3166-1 alpha-2，大写），默认 CN。")
    currency: str = Field(default="CNY", description="币种代码（ISO 4217，大写），默认 CNY。")


def model_dump(data: Any) -> Dict[str, Any]:
    if hasattr(data, "model_dump"):
        return data.model_dump(exclude_none=True)  # pydantic v2
    return data.dict(exclude_none=True)  # pydantic v1
