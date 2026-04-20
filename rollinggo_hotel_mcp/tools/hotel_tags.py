from fastmcp import FastMCP

from ..auth import extract_api_key
from ..client import request_api


def register_hotel_search_tags_tool(mcp: FastMCP) -> None:
    @mcp.tool(name="getHotelSearchTags")
    async def get_hotel_search_tags() -> dict:
        """
        获取酒店搜索标签元数据（AI Cache），包含可用标签列表。
        适用于本地缓存后进行用户意图解析，再将结构化标签传入 searchHotels.hotelTags。
        """
        api_key = extract_api_key()
        return await request_api("GET", "/hoteltags", api_key)
