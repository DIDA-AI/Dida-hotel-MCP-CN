# RollingGo Hotel MCP Server

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![FastMCP](https://img.shields.io/badge/FastMCP-MCP%20Server-green.svg)](https://github.com/jlowin/fastmcp)

---

## Navigation

[Homepage (Chinese)](https://rollinggo.store/) · [Homepage (English)](https://global.rollinggo.store/) · [Quick Start](#quick-start) · [Tools](#tools) · [Examples](#examples)

---

## Overview

**RollingGo Hotel MCP** provides AI agents and MCP clients with hotel booking capabilities, designed for developers, AI builders, travel product teams, and enterprise travel scenarios who want to integrate hotel transaction functionality into their AI products. **Both enterprises and individuals can access it completely free with one-click setup.**

Official product backed by Asia's #1 and world's #3 intelligent global travel resource distribution platform, with three major resource advantages to help your AI applications quickly integrate real hotel booking processes at zero cost, transforming "asking about hotels" into "completing full hotel booking workflows":

- **2+ Million Hotels**: Coverage of all major global destinations with comprehensive domestic and international hotel information services
- **110K+ Direct Partner Hotels**: Real-time price and inventory responses, ensuring accurate and bookable query results
- **500+ Global Suppliers**: Covering global, regional, and local hotel brands to meet diverse user needs

---

## Who Is This For?

- Individual users with hotel search, price comparison, or flight monitoring needs
- Teams or developers building AI agents
- Developers looking to integrate hotel booking capabilities into MCP clients
- Developers building travel planning, business travel management, OTA, or lifestyle service agents
- Product teams validating AI agent business transaction workflows

---

## Use Cases

- **General AI Agents**: Enable your language model agents with native hotel booking capabilities, allowing users to complete entire workflows from demand understanding, intelligent recommendations, price comparison to order creation in natural conversation
- **AI Travel Assistant**: Intelligently recommend hotels based on user destinations, dates, budgets, and preferences, supporting multi-dimensional requirement matching
- **Trip Planning Tools**: Seamlessly embed hotel search and booking capabilities into conversational trip planning processes, achieving integrated "plan and book" experiences
- **MCP / Agent Demo**: Quickly validate "AI agents directly completing hotel transactions" capabilities, building complete, demonstrable workflows

---

## Core Features

- Support for **6 location search types** including city names, airport codes, popular attractions, transportation hubs, hotel names, and detailed addresses for precise searches
- Flexible **professional filtering** including star ratings, check-in dates, stay duration configuration, and price range filtering
- **Personalized recommendations** based on user preferences, generating multiple professional rankings like best value, popular favorites, and trending choices
- **Full natural language interactions**, intelligently completing end-to-end workflows from location parsing, filtering and comparison, to personalized recommendations and order generation

---

## What Agents Can Do

- Search hotels by destination, check-in date, check-out date, and number of guests
- Query hotel prices and room type information
- Determine hotel or room type availability
- Build hotel recommendation, price comparison, and trip planning workflows
- Integrate hotel capabilities into **Claude, Cursor, Cherry Studio, ChatGPT MCP Client** or other MCP-compliant clients

⚠️ **Note**: If you're using platforms like ClawHub, DingXiang, or Qclaw, please use our [RollingGo All-in-One Flight & Hotel Booking Skill](https://modelscope.cn/collections/yorklu/RollingGo-quannengdingjiudianjipiao-Skill). See [RollingGo Skill Configuration Guide](https://rollinggo.store/docs/skill-docs/skill-config) for details.

---

## 🚀 Quick Start

> 💡 In summary, you only need to do two things: apply for an API Key and configure it in your AI assistant. **No coding required** – any MCP-compliant AI assistant gains hotel search capabilities in 5 minutes with your first tool call.

### Step 1: Get Your API Key

1. [Visit the Application Page](https://mcp.agentichotel.cn/apply)
2. Fill in basic information – automatic approval within 1-3 minutes. You'll receive an email containing:
   - API Key
   - Partner Center account (login + initial password) to configure markups, view orders, and check earnings
3. ⚠️ Check your email (including spam folder) for the API Key
4. **Limited-Time Offer**: All developers who complete their first tool call within 3 days of receiving the API Key unlock **permanent unlimited free access**. We prioritize developers with real needs and execution speed, offering zero-cost access to complete hotel MCP capabilities.

> The email includes both hotel and flight MCP endpoints – one key works for both. You can choose which ones to use. We've also published [RollingGo Flight MCP](https://modelscope.cn/mcp/servers/yorklu/RollingGo_Flight) on ModelScope.

**Why Do We Require Information for API Key Application?**

Since hotel prices, inventory, and order capabilities involve real transaction workflows, we need to provision **free, dedicated keys for each developer**. This approach helps us:

- Provision appropriate access permissions for free
- Provide technical support during integration
- Understand your use case and reduce invalid configuration costs
- Protect API stability and prevent malicious calls or unusual traffic
- Quickly contact you about test orders, price queries, and inventory validation

We only use this information for key provisioning, integration support, and service security. We don't share it externally or use it for unrelated purposes. If you just want to try MCP first, let us know your testing goals and we'll provide lightweight testing support.

### Step 2: Configure in Your AI Assistant

#### Remote Mode (Cloud-Hosted, Recommended)

\\\json
{
  "mcpServers": {
    "RollingGo-Hotel-MCP": {
      "serverUrl": "https://mcp.aigohotel.com/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_API_KEY",
        "Content-Type": "application/json"
      }
    }
  }
}
\\\

#### Local Mode

For cases where you've started the \ollinggo-hotel-mcp\ service locally:

1. **Start the backend service**: Ensure your local service is running and listening on \http://localhost:8000/mcp\
2. **Add configuration**: Use the traditional \url\ field in your \mcp.json\:

\\\json
{
  "mcpServers": {
    "RollingGo-Hotel-MCP": {
      "url": "http://localhost:8000/mcp",
      "type": "http",
      "headers": {
        "X-Secret-Key": "YOUR_API_KEY"
      }
    }
  }
}
\\\

### Step 3: Start Using

Send requests in your AI assistant, for example:
> "Find me 4+ star hotels within 5km of West Lake in Hangzhou for the next 3 days with lake views"

Your AI will automatically call the tools and return hotel listings.

### Step 4: Join Our WeChat Support Group

Have integration questions? Join our WeChat technical support group – our core development team is online ready to help you with environment setup, API debugging, and your first successful hotel booking call, ensuring smooth onboarding.

Get support on:
- Integration configuration guidance
- API / MCP call troubleshooting
- Hotel search, pricing, and booking workflow explanations
- Integration suggestions for your use cases

- 💬 [WeChat Group](https://github.com/RollingGo-AI/rollinggo-hotel-mcp/blob/main/support-wehcat%20group.png)
- 📧 Email: \york.lu@dida.com\

---

## Setup & Running

### 1. Clone the Repository

\\\ash
git clone https://github.com/RollingGo-AI/rollinggo-hotel-mcp.git
cd rollinggo-hotel-mcp
\\\

### 2. Install Dependencies

\\\ash
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate   # Linux/Mac
pip install -r requirements.txt
\\\

### 3. Start the Server

\\\ash
python server.py
\\\

Default MCP endpoint: \http://127.0.0.1:8000/mcp\

### 4. Pass API Key via Headers in MCP Client

The server does **not** read the API Key from \.env\. Configure request headers in your MCP client:

- Recommended: \Authorization: Bearer YOUR_API_KEY\
- Alternative: \X-Secret-Key: YOUR_API_KEY\

> **Important:**
> - Apply for an API Key at https://rollinggo.store/apply
> - API Keys must start with \mcp_\
> - Missing or malformed keys will cause request failures

---

## Tools

The server provides 3 tools:

1. \searchHotels\ — Search hotels by location, dates, star rating, guest count, tags, etc.
2. \getHotelDetail\ — Get real-time room types and pricing for a specific hotel
3. \getHotelSearchTags\ — Retrieve tag metadata usable in \searchHotels.hotelTags\

### 1) searchHotels

#### Input Parameters

- \originQuery\ (string, **required**): The user's original query.
- \place\ (string, **required**): Location name — be as specific as possible (city / airport / attraction / detailed address, etc.).
- \placeType\ (string, **required**): Location type. Supported values: \城市\ (city), \机场\ (airport), \景点\ (attraction), \火车站\ (train station), \地铁站\ (subway station), \酒店\ (hotel), \区/县\ (district), \详细地址\ (detailed address).
- \countryCode\ (string, optional): ISO 3166-1 alpha-2 country code, e.g. \CN\, \US\.
- \size\ (number, optional, default: \5\): Number of hotels to return, max \20\.
- \checkInParam\ (object, optional): Check-in related parameters.
- \ilterOptions\ (object, optional): Filter parameters.
- \hotelTags\ (object, optional): Tag / brand / budget filters.

**\checkInParam\ fields:**

- \dultCount\ (number, optional, default: \2\): Adults per room.
- \checkInDate\ (string, optional, format: \YYYY-MM-DD\): Check-in date. If omitted, in the past, or malformed, defaults to tomorrow.
- \stayNights\ (number, optional, default: \1\): Number of nights.

**\ilterOptions\ fields:**

- \distanceInMeter\ (number, optional): Straight-line distance from POI in meters. Defaults to \5000\ when a POI is used.
- \starRatings\ (number[], optional): Star rating range, defaults to \[0.0, 5.0]\, step \ .5\.

**\hotelTags\ fields:**

- \preferredTags\ (string[], optional): Preferred tags.
- \equiredTags\ (string[], optional): Required tags (hard constraint).
- \excludedTags\ (string[], optional): Excluded tags.
- \preferredBrands\ (string[], optional): Preferred brands.
- \maxPricePerNight\ (number, optional): Max budget per night (CNY).
- \minRoomSize\ (number, optional): Minimum room size in square meters.

#### Output

\\\json
{
  "message": "Hotel search succeeded",
  "hotelInformationList": [
    {
      "hotelId": 43615,
      "bookingUrl": "https://rollinggo.cn/pages/hotel/detail/index?...",
      "name": "Sunworld Dynasty Hotel Beijing",
      "brand": null,
      "address": "50 Wangfujing Street",
      "destinationId": "6140156",
      "latitude": 39.917748,
      "longitude": 116.412249,
      "distanceInMeters": 205,
      "starRating": 5.0,
      "price": {
        "message": "Price found, lowest: 626.0, currency: CNY",
        "hasPrice": true,
        "currency": "CNY",
        "lowestPrice": 626.0
      },
      "areaCode": "CN",
      "description": "...",
      "imageUrl": "https://image-cdn.RollingGo.com/...",
      "hotelAmenities": ["24h Front Desk", "WiFi"],
      "score": 1.0,
      "tags": ["Near Shopping Mall", "Free WiFi"]
    }
  ]
}
\\\

> **Note:** \price\ is an object, not a number. Fields may be missing or \
ull\ depending on city/supply source.

---

### 2) getHotelDetail

#### Input Parameters

- \hotelId\ (number, optional): Hotel ID. Mutually exclusive with \
ame\; if both are provided, \hotelId\ takes priority.
- \
ame\ (string, optional): Hotel name (fuzzy match).
- \dateParam\ (object, optional): Check-in / check-out date parameters.
- \occupancyParam\ (object, optional): Guest count and room count parameters.
- \localeParam\ (object, optional): Country and currency parameters.

**\dateParam\ fields:**

- \checkInDate\ (string, optional, format: \YYYY-MM-DD\): Check-in date. Defaults to tomorrow if empty, malformed, or in the past.
- \checkOutDate\ (string, optional, format: \YYYY-MM-DD\): Check-out date. Defaults to \checkInDate + 1\ day if empty, malformed, or not after check-in.

**\occupancyParam\ fields:**

- \dultCount\ (number, optional, default: \2\): Adults per room.
- \childCount\ (number, optional, default: \ \): Children per room.
- \childAgeDetails\ (number[], optional): Child ages, e.g. \[3, 5]\.
- \oomCount\ (number, optional, default: \1\): Number of rooms.

**\localeParam\ fields:**

- \countryCode\ (string, optional, default: \CN\): ISO 3166-1 alpha-2 country code.
- \currency\ (string, optional, default: \CNY\): Currency code.

#### Output

\\\json
{
  "success": true,
  "errorMessage": null,
  "hotelId": 43615,
  "bookingUrl": "https://rollinggo.cn/pages/hotel/detail/index?...",
  "name": "Sunworld Dynasty Hotel Beijing",
  "checkIn": "2026-03-05",
  "checkOut": "2026-03-06",
  "roomRatePlans": [
    {
      "roomTypeId": 4984714,
      "roomName": "Superior Room",
      "roomNameCn": "高级客房",
      "ratePlanId": "7012072001634754626",
      "ratePlanName": "Superior Room King Bed, 1 King Bed",
      "bedType": 73,
      "bedTypeDescription": "Unknown",
      "currency": "CNY",
      "totalPrice": 0,
      "totalSalesRate": null,
      "inventoryCount": null,
      "isOnRequest": null,
      "recommendIndex": null,
      "cancellationPolicies": [
        {
          "fromDate": "2026-03-02T10:00:00+08:00",
          "toDate": null,
          "amount": 634,
          "percent": null,
          "type": null,
          "description": null
        }
      ],
      "includedFees": null,
      "excludedFees": null,
      "metadata": null
    }
  ]
}
\\\

> **Note:** On failure, the response may contain an error message (e.g. "Failed to fetch pricing, please retry later") or structured error fields. The \oomRatePlans\ array can be long — consider paginating or limiting display on the client side.

---

### 3) getHotelSearchTags

Retrieves available tags for use in \searchHotels.hotelTags\. Suitable for local caching and client-side intent mapping.

#### Output

\\\json
{
  "tags": [
    {
      "name": "Free WiFi",
      "category": "Core Amenities",
      "description": "Provides free WiFi"
    }
  ],
  "usageGuide": {
    "tagUsage": "Place tag names into hotelTags.preferredTags (preference), requiredTags (hard requirement), or excludedTags (exclusion)",
    "exampleRequest": "{...}"
  }
}
\\\

**Common tag categories:**

- Brand & Ratings
- Specialty Highlights
- Core Amenities
- Family & Kids
- Service Details
- Service & Dining
- Transportation & Payment
- Views & Room Types
- Hotel Type
- Pricing

---

## Examples

### Example 1: City Search

\\\json
{
  "originQuery": "Find 4-star+ hotels in Beijing for 2 nights",
  "place": "Beijing",
  "placeType": "城市",
  "checkInParam": {
    "checkInDate": "2026-03-01",
    "stayNights": 2
  },
  "filterOptions": {
    "starRatings": [4.0, 5.0]
  },
  "size": 5
}
\\\

### Example 2: With Tags and Budget Constraints

\\\json
{
  "originQuery": "Find quality hotels in Beijing with free WiFi, budget under 1000 per night",
  "place": "Beijing",
  "placeType": "城市",
  "hotelTags": {
    "preferredTags": ["Free WiFi", "Quality Hotel"],
    "maxPricePerNight": 1000
  },
  "size": 5
}
\\\

### Example 3: Query Hotel Room Types and Pricing

\\\json
{
  "hotelId": 43615,
  "dateParam": {
    "checkInDate": "2026-03-05",
    "checkOutDate": "2026-03-06"
  },
  "occupancyParam": {
    "adultCount": 2,
    "roomCount": 1
  },
  "localeParam": {
    "currency": "CNY",
    "countryCode": "CN"
  }
}
\\\

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Links
- [Model Context Protocol](https://modelcontextprotocol.io/)
- [FastMCP](https://github.com/jlowin/fastmcp)
- [API Key Application](https://rollinggo.store/apply)