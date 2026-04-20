from fastmcp.server.dependencies import get_http_request


def extract_api_key() -> str:
    api_key = ""
    try:
        request = get_http_request()
        if request:
            headers = request.headers
            auth_header = (
                headers.get("authorization")
                or headers.get("Authorization")
                or headers.get("x-secret-key")
                or headers.get("X-Secret-Key")
                or ""
            )
            if auth_header:
                api_key = auth_header[7:].strip() if auth_header.startswith("Bearer ") else auth_header.strip()
    except RuntimeError:
        # 非 HTTP 上下文时，get_http_request() 会抛出 RuntimeError
        pass

    if not api_key:
        raise Exception("未提供 API Key，请在请求 header 中添加 Authorization: Bearer <your_api_key>")

    return api_key
