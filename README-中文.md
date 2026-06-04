# RollingGo Hotel MCP Server

🌐 **[English](#english-version)** | **[中文](#中文版本)**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Version](https://img.shields.io/badge/Version-1.0.0-blue.svg)](https://github.com/RollingGo-AI/rollinggo-hotel-mcp/releases)
[![ModelScope](https://img.shields.io/badge/ModelScope-Rank%237-brightgreen.svg)](https://modelscope.cn/)
[![Calls](https://img.shields.io/badge/Calls-847.3k-orange.svg)](https://github.com/RollingGo-AI/rollinggo-hotel-mcp)

---

## 简介
**RollingGo Hotel MCP**为 AI Agent 和 MCP 客户端提供酒店预订能力，它适合希望在 AI 产品中接入酒店交易能力的开发者、Agent 构建者、旅游产品团队和企业差旅场景，**企业和个人均可完全免费一键接入**。

官方出品，依托亚洲第一、全球第三的智能驱动全球旅游资源分发服务商，三大核心资源优势，帮助你的 AI 应用零成本快速接入真实酒店预订全流程，把 "问酒店" 变成 "能完成酒店预订流程"：
- **200 万 + 酒店数量**：覆盖全球所有主要目的地，提供全量海内外酒店信息服务
- **11 万 + 直签酒店**：价格库存实时响应，确保查询结果准确可订
- **500+ 全球供应商**：涵盖全球、区域及本地各类酒店品牌，满足不同用户需求

## 适用人群
- 有酒店查询、酒店比价、机票监控需求的个人用户
- 正在开发 AI Agent 的团队或个人开发者
- 想在 MCP Client 中接入酒店预订能力的开发者
- 正在构建旅行规划、差旅管理、OTA、生活服务类智能体的开发者
- 希望验证 AI Agent 商业交易闭环的产品团队

## 应用场景
- **通用 AI Agent**：让你的大模型 Agent 直接拥有原生酒店预订能力，用户在自然对话中即可完成从需求理解、智能推荐、比价筛选到订单创建的全流程
- **AI 旅行助手**：根据用户目的地、日期、预算和个性化偏好精准推荐酒店，支持多维度需求匹配
- **行程规划工具**：把酒店搜索和预订能力无缝嵌入对话式行程规划流程，实现 "规划即预订" 的一体化体验
- **MCP / Agent Demo**：快速验证 "AI Agent 直接完成酒店交易" 的产品能力，打造可演示的完整闭环

## 核心功能
- 支持**城市名称、机场代码、热门景点、交通枢纽、酒店名称、具体地址**等 6 种目标地点类型精准搜索
- 提供灵活的**星级筛选、入住日期设置、住宿天数配置、价格区间过滤**等专业筛选功能
- 基于用户个人偏好提供**个性化推荐，生成高性价比、好评热门、人气精选**等多维度专业榜单
- 全程自然语言交互，智能完成从**地点解析、筛选比价、个性化推荐到订单生成**的完整闭环

## 你可以让 Agent 完成以下酒店相关任务：
- 根据目的地、入住日期、离店日期和人数搜索酒店
- 查询酒店价格和房型信息
- 判断酒店或房型是否可订
- 构建酒店推荐、比价、行程规划等 AI 工作流
- 将酒店能力接入到**Claude、Cursor、Cherry Studio、ChatGPT MCP Client**或其他支持 MCP客户端中

⚠️如果你使用 ClawHub/扣子/Qclaw等Agent 平台，请使用我们的[Rollinggo全能订机票酒店Skill](https://modelscope.cn/collections/yorklu/RollingGo-quannengdingjiudianjipiao-Skill)。请参考[RollingGo Skill 配置指南](https://rollinggo.store/docs/skill-docs/skill-config).

---

## 🚀快速开始
> 💡 总结来说，你只需要做两件事：申请API Key+ 在AI助手中一键配置，**无需编写代码**，就能让任何支持MCP的AI助手具备酒店搜索能力，5 分钟内完成第一次 MCP Tool 调用，

### 第一步：获取API密钥

1. [点击进入申请地址](https://mcp.agentichotel.cn/apply)
2. 填写基本信息，1-3 分钟内自动审核通过，收到邮件包含：
API Key
伙伴中心账号（登录名 + 初始密码），登录后可配置加价比例、查看订单、查询收益
3. ⚠️ 注意查收邮件，如未收到请检查垃圾邮箱
4. 为了感谢首批愿意尝鲜、快速行动的开发者，我们特别推出限时福利：**所有收到 API Key 后 3 天内完成第一次工具调用，即可自动解锁永久免费无限制调用额度。**
我们希望优先支持真正有需求、有执行力的开发者，让大家零成本体验完整的酒店MCP 能力。

> 邮件中同时包含酒店MCP端点和机票MCP端点，一个Key即可接入，你可选择性使用。我们同时在魔搭上架了[RollingGo Flight MCP](https://modelscope.cn/mcp/servers/yorklu/RollingGo_Flight)产品介绍。

**为什么需要填写信息申请 KEY**？

酒店价格、库存和订单能力涉及真实交易链路，因此我们需要为每个开发者开通**免费专属的独立 KEY**。申请 KEY 时仅需填写少量信息，这样做主要是为了：
- 为你免费开通合适的接口权限
- 在接入过程中提供技术支持
- 判断你的使用场景，减少无效配置成本
- 保护接口稳定性，避免恶意调用或异常流量
- 在测试订单、价格查询、库存校验等问题上能及时联系到你

我们只会将这些信息用于 KEY 开通、接入支持和服务安全，不会对外共享，也不会用于无关用途。若你只是想先体验 MCP，也可以说明你的测试目标，我们会尽量提供轻量的测试支持。

### 第二步：在AI助手中配置

#### 在 Cursor / Windsurf 中使用 （远程模式）

\\\json
{
  "mcpServers": {
    "aigohotel-mcp": {
      "serverUrl": "https://mcp.aigohotel.com/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_API_KEY", //替换成你的API-KEY
        "Content-Type": "application/json"
      }
    }
  }
}
\\\
#### 本地模式
适用于你在本地启动了 \igohotel-mcp\ 服务进程的情况。
1. **启动后端服务**：确保本地服务已运行并监听 \http://localhost:8000/mcp\。
2. **添加配置**：在 \mcp.json\ 中使用传统的 \url\ 字段。
\\\json
{
  "mcpServers": {
    "aigohotel-mcp": {
      "url": "http://localhost:8000/mcp", //本地服务地址
      "type": "http",
      "headers": {
             "X-Secret-Key": "YOUR_API_KEY" // 替换成你的API-KEY
         }
    }
  }
}
\\\
### 第三步：开始使用

在AI助手中发送请求，例如：
> "帮我查一下未来3日内，杭州西湖景区附近有哪些可以看到西湖风景的，4星以上的酒店？"

AI会自动调用工具，返回酒店列表。

### 第四步：加入微信群，获取技术支持
接入路上有任何问题都别担心！欢迎加入我们的微信技术支持群，我们的核心开发团队会全程在线，手把手帮你搞定环境配置、接口调试，陪你跑通第一个成功的酒店预订调用，让你零障碍快速上线。

你可以在群内获得：
- 接入配置指导
- API / MCP 调用问题排查
- 酒店搜索、价格、预订流程说明
- 适合你业务场景的集成建议
- 💬 微信群：[扫码加入](https://github.com/RollingGo-AI/rollinggo-hotel-mcp/blob/main/support-wehcat%20group.png)
- 📧 邮箱：\york.lu@dida.com\

---

## ✨ 功能特性

| 功能 | 说明 |
|------|------|
| 🏙️ **多地点搜索** | 支持城市、景点、机场、火车站、地铁站等 |
| 📅 **日期筛选** | 指定入住日期和住宿天数 |
| ⭐ **星级过滤** | 支持0-5星筛选，精确到0.5星梯度 |
| 📍 **距离搜索** | 以景点为中心，限定半径范围（米） |
| 🛏️ **设施详情** | 可选返回酒店设施、房间设施信息 |
| 🌐 **多语言** | 支持中文、英文等语言环境 |

---

## 🛠️ 工具列表
| 工具名称 | 功能简介 | 使用场景 |
|----------|---------|----------|
| **GetHotelSearchTags** | 获取酒店搜索标签元数据 | 启动时缓存，辅助AI理解用户需求 |
| **SearchHotels** | 多条件酒店信息搜索 | 初筛比选候选酒店 |
| **GetHotelDetail** | 单个酒店房型价格，以及酒店详细信息查询 | 用户选定酒店后查价预订 |
---


## 📝 使用示例

### 示例1：城市酒店搜索
> "帮我看看未来三天内，杭州有哪些4星以上的酒店推荐？"

![showcase1](https://raw.githubusercontent.com/young63/dida-picbed/main/showcase1.png)
![showcase2](https://raw.githubusercontent.com/young63/dida-picbed/main/showcase2.png)

---

### 示例2：景点周边搜索
> "2026年七夕节，想在香港迪士尼附近找个性价比高的酒店"

![showcase3](https://raw.githubusercontent.com/young63/dida-picbed/main/showcase3.png )
![showcase5](https://raw.githubusercontent.com/young63/dida-picbed/main/showcase5.png)
---

### 配置参数说明

#### 常用核心参数

| 参数 | 必填 | 说明 | 示例 |
|------|------|------|------|
| place | ✅ | 搜索地点 | 杭州、迪士尼 |
| placeType | ✅ | 地点类型 | 城市、景点、机场、地铁站、区/县... |
| originQuery | ✅ | 你的原始需求描述 | 帮我找酒店 |
| checkIn | ❌ | 入住日期(yyyy-MM-dd) | 2026-05-01 |
| stayNights | ❌ | 住宿天数 | 2 |
| starRatings | ❌ | 星级范围 | [4, 5] 表示4-5星 |
| size | ❌ | 返回数量(默认10)，最大20 | 5 |

> 注意：
> - 实际字段以接口数据返回为准，上述示例仅展示部分字段。
> -   随着后端能力演进，字段可能会新增或调整，MCP 客户端侧建议按"有则使用、无则忽略"的方式做兼容。
---

## ❓ 常见问题
### Q: 支持哪些AI助手/IDE？

**A:** 目前支持以下平台：
- Cursor
- Windsurf
- Antigravity
- Claude Desktop
- Cherry studio等其他支持MCP协议的客户端

### Q: 搜索结果包含哪些信息？

**A:** 默认返回酒店名称、星级、价格、地址、预订链接，酒店图片、酒店设施等。(具体可参考实际返回数据)
### Q: 有调用次数限制吗？

**A:** 目前阶段免费使用。
---

## 🔒 安全与鉴权

### 认证方式

| 环境 | 认证方式 | Header |
|------|----------|--------|
| 远程(云端) | Bearer Token | \Authorization: Bearer YOUR_API_KEY\ |
| 本地服务 | Secret Key | \X-Secret-Key: YOUR_API_KEY\ |

### 安全建议

- API Key请妥善保管，不要硬编码在代码中
- 生产环境建议使用环境变量管理
- 公网访问请使用HTTPS协议

---

## 📋 更新日志

### v1.0.0 
- ✨ 文档信息更变
---

<div align="center">

**Made with ❤️ by RollingGo Team**

</div>