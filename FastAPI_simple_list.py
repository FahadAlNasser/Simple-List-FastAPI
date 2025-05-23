from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

Video_games: List[str] = ["Dragon Age Inquisition", "Mass Effect 3",
                          "Tomb Raider", "Destiny", "Baldur's Gate 3"]

class Games(BaseModel):
    name: str

# Function that shows the list of video games
@app.get("/game-list", response_model=List[str])
def get_video_games():
    return  Video_games

# function that allows a user to include a new game to the list
@app.post("/game-list", response_model=List[str])
def make_game(new_game: Games):
    Video_games.append(new_game.name)
    return Video_games

# This function updates the list
@app.put("/game-list/{game_index}", response_model=List[str])
def game_update(game_index: int, new_game: Games):
    if 0 <= game_index < len(Video_games):
        Video_games[game_index] = new_game.name
        return Video_games
    raise HTTPException(status_code=404, detail="The game was not found")

# This function delete a video game from the list
@app.delete("/game-list/{game_index}", response_model=List[str])
def remove_game(game_index: int):
    if 0 <= game_index < len(Video_games):
        Video_games.pop(game_index)
        return Video_games
    raise HTTPException(status_code=404, detail="The game is not found")
