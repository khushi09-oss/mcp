from mcp.server.fastmcp import FastMCP

mcp=FastMCP('My first server')  #Creates your server. The name is shown to Claude.

@mcp.tool()  #Registers the function as a callable MCP tool.
def say_hello(name: str) -> str:  #Type hints define the tool's input schema — Claude uses these. Return type hint tells Claude what kind of output to expect.
    """Say hello to someone.""" #Critical: Claude reads this to decide when to call the tool.
    return f'Hello, {name}!'

if __name__ == '__main__':
    mcp.run() #Starts the server over STDIO.
