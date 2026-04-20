# RollingGo MCP Server

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![FastMCP](https://img.shields.io/badge/FastMCP-MCP%20Server-green.svg)](https://github.com/jlowin/fastmcp)

RollingGo 酒店搜索 MCP Server。通过标准的 Model Context Protocol (MCP) 协议为 AI 助手提供全球酒店搜索能力。

当前主包名已切换为 `rollinggo-hotel-mcp`，Python 包目录同步切换为 `rollinggo_hotel_mcp`。

## 工具列表

**search_hotels** - 查询全球酒店信息
- 支持按城市、景点、酒店、交通枢纽等多种地点类型搜索
- 支持星级筛选、距离筛选、入住日期等多维度条件
- 返回符合条件的酒店列表(JSON格式)

### 请求参数

**必填参数**:
- **place** (string): 目的地(城市、景点、酒店、交通枢纽、地标等)
- **placeType** (string): 目的地类型(城市、区/县、机场、火车站、酒店、景点等)

**可选参数**:
- **originalQuery** (string): 用户的原始问询句
- **checkIn** (string): 入住日期,格式 yyyy-MM-dd,默认次日
- **stayNights** (int): 入住晚数,默认 1
- **starRatings** (array): 酒店星级范围,如 [4.5, 5.0],默认 [0.0, 5.0]
- **adultCount** (int): 每间房成人数量,默认 2
- **distanceInMeter** (int): 距离景点的米数,默认 5000
- **size** (int): 返回结果数量,默认 10,最大 20
- **withHotelAmenities** (bool): 是否包含酒店设施,默认 true
- **withRoomAmenities** (bool): 是否包含客房设施,默认 true
- **language** (string): 语言环境(zh_CN, en_US等),默认 zh_CN
- **queryParsing** (bool): 是否分析用户个性化需求,默认 true

### 返回参数
```json
{
  "hotelId": "酒店ID",
  "name": "酒店名称",
  "address": "酒店位置",
  "destinationId": "目的地",
  "latitude": 30.665025, # 纬度
  "longitude": 104.066475, # 经度
  "starRating": 5.0, # 星级
  "bookingUrl": "酒店预定详情页",
  "description": "酒店描述",
  "imageUrl": "酒店首图",
  "areaCode": "国家",
  "price": 549.0, # 价格
  "hotelAmenities": [
    "咖啡厅咖啡厅",
    "会议厅会议室",
    // ... 部分省略
  ], # 酒店设施
  "hotelRoomAmenities": [], # 房间设施
  "tags": [], # 酒店个性化标签
  "score": "个性化评分",
  "currency": "CNY" # 币种
}

```

### 使用示例

**示例 1**: 搜索西雅图的酒店
```json
{
  "place": "西雅图",
  "placeType": "城市"
}
```

**示例 2**: 搜索白金汉宫附近的高星级酒店
```json
{
  "place": "白金汉宫",
  "placeType": "景点",
  "checkIn": "2026-01-01",
  "starRatings": [4.5, 5.0]
}
```

## 配置方法
目前仅支持`streamable-http` 传输

### 1. 安装依赖

```bash
# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 安装依赖包
pip install -r requirements.txt
```

### 2. 准备 API Key (必需)

**获取 API Key**: https://mcp.agentichotel.cn/apply

HTTP 版本在运行时从请求头读取 API Key，不需要在本地 `.env` 中保存密钥。调用方需要传入以下任一请求头：

```http
Authorization: Bearer mcp_your_actual_api_key_here
```

或：

```http
X-Secret-Key: mcp_your_actual_api_key_here
```

> **重要**: 
> - 前往 https://mcp.agentichotel.cn/apply 申请 API Key
> - API Key 必须以 `mcp_` 开头
> - 未携带或格式错误将导致 API 请求失败

### 3. 启动服务器

```bash
python server.py
```

启动成功后会显示:
```
RollingGo MCP Server 启动中...
认证方式: 从请求 header 中读取 Authorization / X-Secret-Key
INFO: Uvicorn running on http://127.0.0.1:8000
```

## MCP 客户端配置
在 MCP 配置文件中添加以下内容:

```json
{
  "mcpServers": {
    "rollinggo": {
      "url": "http://localhost:8000/mcp"
    }
  }
}
```

## API 鉴权说明

### 申请 API Key

访问 https://mcp.agentichotel.cn/apply 申请 API Key

## 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 相关链接
- [Model Context Protocol](https://modelcontextprotocol.io/)
- [FastMCP](https://github.com/jlowin/fastmcp)
- [API Key 申请](https://mcp.agentichotel.cn/apply)
