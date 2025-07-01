from mcp.server.fastmcp import FastMCP


mcp = FastMCP(name="EchoServer", stateless_http=True)

@mcp.tool(description="Tool to echo back the input")
def echo(input_text: str) -> str:
    """
    Use this tool to echo back the input text.
    Args:
        input_text: the text to echo
    Return:
        the echoed text.
    """
    return input_text