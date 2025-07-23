from datetime import datetime
from mcp.server.fastmcp import FastMCP


mcp = FastMCP("Time")

@mcp.tool()
async def get_time() -> dict:
    """
    Gets the current local time and returns it as a dictionary.
    
    Returns:
        dict: A dictionary containing the current time components with keys:
            - "Hour": Current hour (0-23)
            - "Minute": Current minute (0-59) 
            - "Second": Current second (0-59)
        This function only returns the current time. Uses the system's local timezone.
    """
    now = datetime.now()
    hour = now.hour
    minute = now.minute
    second = now.second
    return {"Hour":hour, "Minute":minute, "Second":second}

if __name__ == "__main__":
    mcp.run(transport='stdio')