import google_services as gs
from mcp.server.fastmcp import FastMCP
import models
from rich import print
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
    creds = gs.get_google_credentials()
    files = gs.get_drive_files(query=query, creds=creds)
    return files


@mcp.tool()
def create_calendar_event(event_creation_details: models.EventCreationModel, attachments: list[models.EventAttachmentModel] = []):
    """
    Get files from Google Calendar based on a query.

    Args:
        - event_creation_details (models.EventCreationModel): The details of the event to be created.
    """
    creds = gs.get_google_credentials()
    event = gs.create_calendar_event(
        event_creation_details, creds, attachments)
    return event


if __name__ == "__main__":
    # creds = gs.get_google_credentials()
    # files = gs.get_drive_files(query="asd", creds=creds)
    # print(files)

    # file_from_get = gs.get_drive_file_by_id(
    #     file_id=files[0]['id'], creds=creds)
    # print(file_from_get)
    mcp.run(transport='stdio')
