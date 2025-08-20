"""
Platform-aware wrapper for now playing functionality.
Provides mock implementations for non-Windows platforms.
"""
import platform
import sys
from typing import List

from .models import SongInfo

def get_now_playing_info() -> List[SongInfo]:
    """
    Platform-aware wrapper for getting now playing information.
    Uses actual implementation on Windows, mock data on other platforms.
    """
    if sys.platform == "win32":
        # Import and use the actual Windows implementation
        from .services import get_now_playing_info as _get_now_playing_info
        return _get_now_playing_info()
    else:
        # Return mock data for non-Windows platforms (for development/testing)
        return [
            SongInfo(
                process_name="spotify.exe",
                song_title="Mock Song - Mock Artist (Development Mode)"
            )
        ]