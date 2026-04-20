from dotenv import load_dotenv
from fastmcp import FastMCP

from .tools import register_tools

load_dotenv()

mcp = FastMCP("RollingGo Hotel Search", version="1.0.0")
register_tools(mcp)


def main() -> None:
    print("RollingGo MCP Server 启动中...")
    print("认证方式: 从请求 header 中读取 Authorization / X-Secret-Key")
    mcp.run(transport="http", host="127.0.0.1", port=8000)


if __name__ == "__main__":
    main()
