# Time MCP Server

A simple Model Context Protocol (MCP) server that provides current time information to Large Language Models (LLMs) and why not.

## Why This MCP?

LLMs don't have access to real-time information, including the current time. This MCP server bridges that gap by providing accurate, up-to-date time information when needed.

## Features

- **Real-time clock access**: Get the current hour, minute, and second
- **System timezone**: Uses the local system timezone
- **Simple API**: Single function call returns all time components
- **Lightweight**: Minimal overhead and dependencies

## Installation

```bash
git clone https://github.com/alpardayalman/time-mcp.git
pip3 install fastmcp
```

## Usage

The server provides one main function:

### `get_time()`

Returns the current time as a structured object:

```json
{
  "Hour": 13,
  "Minute": 30,
  "Second": 45
}
```

- **Hour**: 24-hour format (0-23)
- **Minute**: Minutes (0-59)
- **Second**: Seconds (0-59)

## Configuration

Add to your MCP client configuration:

```json
"mcpServers": {
  "time-mcp": {
    "command": "python3",
    "args": [
      "/PATH/TO/REPO/server.py"
    ]
  }
}
```

## Use Cases

- Timestamping responses
- Time-based calculations
- Scheduling assistance
- Real-time awareness in conversations
- Logging and debugging with accurate timestamps

## Requirements

- Python
- MCP-compatible client
