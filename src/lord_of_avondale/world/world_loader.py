"""
Utilities for loading game worlds from data files.
"""

import json
from pathlib import Path

from lord_of_avondale.world.room import Room

def load_world(path: Path) -> tuple[dict[str, Room], str]:
    """
    Load a world definition from a JSON file.
    
    Returns:
        A tuple containing:
        - A dictionary of room IDs mapped to Room objects.
        - The ID of the starting room.
    """
    with path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    rooms_data = data["rooms"]
    start_room = data["start_room"]

    rooms = {
        room_id: Room(
            name=room_data["name"],
            description=room_data["description"]
        )
        for room_id, room_data in rooms_data.items()
    }

    for room_id, room_data in rooms_data.items():
        room = rooms[room_id]

        for direction, destination_id in room_data.get("exits", {}).items():
            room.add_exit(direction, rooms[destination_id])

    return rooms, start_room