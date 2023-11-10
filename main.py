import typing
import random

def info() -> typing.Dict:
    print("INFO")

    return {
        "apiversion": "1",
        "author": "snaaaak",
        "color": "#888888",
        "head": "rbc-bowler",
        "tail": "rbc-necktie",
    }

def start(game_state: typing.Dict):
    print("GAME START")

def end(game_state: typing.Dict):
    print("GAME OVER\n")

  
def move(game_state: typing.Dict) -> typing.Dict:

  is_move_safe_dict = {
    "up": True, 
    "down": True, 
    "left": True, 
    "right": True
  }
  
  my_head = game_state["you"]["body"][0]
  my_neck = game_state["you"]["body"][1]
  
  if my_neck["x"] < my_head["x"]:
      is_move_safe_dict["left"] = False
  elif my_neck["x"] > my_head["x"]:
      is_move_safe_dict["right"] = False
  elif my_neck["y"] < my_head["y"]:
      is_move_safe_dict["down"] = False
  elif my_neck["y"] > my_head["y"]:
      is_move_safe_dict["up"] = False

  height = game_state["board"]["height"]
  width = game_state["board"]["width"]


  if my_head["y"] >= height - 1:
    is_move_safe_dict["up"] = False
    
  if my_head["y"] == 0:
    is_move_safe_dict["down"] = False
    
  if my_head["x"] == 0:
    is_move_safe_dict["left"] = False
    
  if my_head["x"] >= width - 1:
     is_move_safe_dict["right"] = False

  safe_moves = []
  for move in is_move_safe_dict:
    if is_move_safe_dict[move]:
      safe_moves.append(move)

  
  
  return {"move": safe_moves[random.randint(0, len(safe_moves) - 1)]}

if __name__ == "__main__":
    from server import run_server

    run_server({
        "info": info, 
        "start": start, 
         "move": move, 
        "end": end
    })
