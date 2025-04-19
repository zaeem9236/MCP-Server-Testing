from mcp.server.fastmcp import FastMCP

mcp = FastMCP("First MCP")


# Use Tools if the LLM needs to act or modify data (e.g., update a database record, calling a function).
# Use Resources (ready-only) if the LLM needs to retrieve or access data (e.g., get a database schema).

@mcp.tool()
def greeting(name: str) -> str:
    """Return greeting with name"""
    return 'Welcome to the MCP server, ' + name + '!'

@mcp.resource("version://{name}")
def version(name: str):
    """Returns the application version."""
    return f'{name}, This is v0.1'
    

if __name__ == "__main__":
    mcp.run(transport='stdio')


