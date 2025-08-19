from pydantic import BaseModel

class SongInfo(BaseModel):
    """
    Represents the structured information for a currently playing song.
    """
    process_name: str
    song_title: str

    # Pydantic v2 feature to generate example data in the OpenAPI docs.
    class Config:
        json_schema_extra = {
            "example": {
                "process_name": "spotify.exe",
                "song_title": "Rick Astley - Never Gonna Give You Up"
            }
        }