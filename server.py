from mcp.server.fastmcp import FastMCP
import logging
import sys

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("XiaozhiMCP")

# Initialize FastMCP server
mcp = FastMCP("XiaozhiTemplate")

@mcp.tool()
def hello_world(name: str = "World") -> str:
    """A simple hello world tool to verify the server is working.
    
    Args:
        name: The name to greet. Defaults to "World".
    """
    logger.info(f"Greeting {name}")
    return f"Hello, {name}!"

@mcp.tool()
def echo(message: str) -> str:
    """Echoes back the message.
    
    Args:
        message: The message to echo.
    """
    return f"Echo: {message}"

if __name__ == "__main__":
    # The transport is handled by mcp_pipe.py which communicates via stdio
    # but we can also run this directly for testing if needed.
    mcp.run(transport="stdio")
