# MCP Server Usage

This repository now includes an MCP (Model Context Protocol) server that exposes the now playing functionality as a tool.

## MCP Server Features

The MCP server provides a single tool:

- **`now_playing`**: Returns currently playing song information from music players

## Running the MCP Server

### Prerequisites

1. Install dependencies:
   ```bash
   uv sync
   ```

2. On Windows, ensure you have music players running (Spotify, QQMusic, NeteaseMusic)

### Starting the Server

Run the MCP server:

```bash
uv run python mcp_server.py
```

The server will run on stdio and communicate using the MCP protocol.

### Testing the Server

You can test the server components without running the full MCP protocol:

```bash
# Test basic functionality
uv run python test_mcp.py

# Test tool functionality
uv run python test_tool.py
```

## MCP Client Configuration

To use this server with an MCP client, add the following configuration:

```json
{
  "mcpServers": {
    "now-playing": {
      "command": "uv",
      "args": ["run", "python", "mcp_server.py"],
      "cwd": "/path/to/NowPlayingAPI"
    }
  }
}
```

## Platform Support

- **Windows**: Full functionality with actual music player detection
- **Linux/macOS**: Mock data for development and testing purposes

## Tool Schema

### now_playing

**Description**: Get currently playing song information from music players

**Input**: No parameters required

**Output**: Text response with currently playing songs, formatted as:
```
Currently playing:
🎵 Song Title - Artist (from spotify.exe)
🎵 Another Song (from qqmusic.exe)
```

If no music is playing, returns: "No music is currently playing."