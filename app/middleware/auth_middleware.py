from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from app.config import settings


EXEMPT_PATHS = ["/docs", "/openapi.json", "/health"]


class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        path = request.url.path

        print('Expected token:', settings.ACCESS_TOKEN)  # Debugging line
        
        if any(path.startswith(exempt) for exempt in EXEMPT_PATHS):
            return await call_next(request)

        auth_header = request.headers.get("Authorization")
        print('Authorization header:', auth_header)  # Debugging line
        if not auth_header or not auth_header.startswith("Bearer "):
            return JSONResponse(
                status_code=401,
                content={"detail": "Missing Authorization header"},
            )

        token = auth_header.split("Bearer ")[1]
        
        if token != settings.ACCESS_TOKEN:
            return JSONResponse(
                status_code=401,
                content={"detail": "Invalid token"},
            )

        return await call_next(request)