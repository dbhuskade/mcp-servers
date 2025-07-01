import contextlib
from fastapi import FastAPI
from echo_server import mcp as echo_mcp # Import the echo server
from math_server import mcp as math_mcp # Import the math server

@contextlib.asynccontextmanager
async def lifespan(app: FastAPI):
    async with contextlib.AsyncExitStack() as stack:
        await stack.enter_async_context(echo_mcp.session_manager.run())
        await stack.enter_async_context(math_mcp.session_manager.run())
        yield


app = FastAPI(lifespan=lifespan)

app.mount("/echo", echo_mcp.streamable_http_app())
app.mount("/math", math_mcp.streamable_http_app())

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)