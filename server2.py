from mcp.server.fastmcp import FastMCP

mcp=FastMCP()

@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b

@mcp.tool()
def repeat_text(text: str, times: int = 3) -> str:
    """Repeat a given text a specified number of times."""
    return " ".join([text] * times)
if __name__ == '__main__':
    mcp.run()   