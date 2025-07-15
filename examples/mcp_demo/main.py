from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("weather")

if __name__ == "__main__":
    mcp.run(transport='stdio')
