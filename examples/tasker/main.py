from google_auth import get_google_credentials, get_drive_files
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("google services")


@mcp.tool()
def get_files(query: str):
    """
    Get files from Google Drive based on a query.

    Args:
        query (str): The query to filter files in Google Drive. example: "trashed = false and name = 'reverse proxy.drawio'"
    Returns(example):
        [{'parents': ['ghhugdonoadsknasfasfasfiasubf'], 'id': 'fasloiufg849sdfg45sd', 'name': 'reverse proxy.drawio', 'mimeType': 'application/vnd.jgraph.mxfile', 'webViewLink': 'https://drive.google.com/file/d/1fas654fas65f41as65fj/view?usp=drivesdk'}]
    """
    creds = get_google_credentials()
    files = get_drive_files(creds, query)
    return files


if __name__ == "__main__":
    mcp.run(transport='stdio')
