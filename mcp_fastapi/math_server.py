from mcp.server.fastmcp import FastMCP


mcp = FastMCP(name="MathServer",stateless_http=True)
@mcp.tool(description="Tool to perform addition of numbers")
def add_numbers(a: int, b: int) -> int:
    """
    Use this tool to add two numbers.
    Args:
        a: the first number
        b: the second number
    Return:
        the sum of the two numbers.
    """
    return a + b

@mcp.tool(description="Tool to perform multiplication of numbers")
def multiply_numbers(a: int, b: int) -> int:
    """
    Use this tool to multiply two numbers.
    Args:
        a: the first number
        b: the second number
    Return:
        the product of the two numbers.
    """
    return a * b