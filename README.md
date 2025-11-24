# Xiaozhi MCP Template

A template for creating MCP servers compatible with Xiaozhi, using `fastmcp` and a WebSocket pipe.

## Quick Start

1.  **Install dependencies**:

    ```bash
    uv sync
    ```

2.  **Set up environment variables**:

    ```bash
    export MCP_ENDPOINT=<your_mcp_endpoint>
    ```

3.  **Run the server**:

    ```bash
    uv run mcp_pipe.py server.py
    ```

## Project Structure

-   `mcp_pipe.py`: Handles WebSocket communication with the Xiaozhi client.
-   `server.py`: The MCP server implementation. Add your tools here.
-   `pyproject.toml`: Project configuration and dependencies.

## Customization

1.  Modify `server.py` to add your own tools using the `@mcp.tool()` decorator.
2.  Update `pyproject.toml` to change the project name and add any new dependencies.