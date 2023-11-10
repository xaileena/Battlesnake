import typing
import random

def info() -> typing.Dict:
    return {
        "apiversion": "1",
        "author": "ekans",
        "color": "#F1CFCC",
        "head": "rbc-bowler",
        "tail": "rbc-necktie",
    }

def start(game_state: typing.Dict):
    pass

def end(game_state: typing.Dict):
    pass

def is_collision(point, body):
    # Check if a point collides with the snake's body
    return point in body

def is_out_of_bounds(point, height, width):
    # Check if a point is out of bounds
    return point["x"] < 0 or point["x"] >= width or point["y"] < 0 or point["y"] >= height

def find_safe_moves(my_head, my_body, height, width, other_snakes):
    safe_moves = []

    # Define all possible moves
    moves = {
        "up": {"x": my_head["x"], "y": my_head["y"] + 1},
        "down": {"x": my_head["x"], "y": my_head["y"] - 1},
        "left": {"x": my_head["x"] - 1, "y": my_head["y"]},
        "right": {"x": my_head["x"] + 1, "y": my_head["y"]}
    }

    # Check if each move is safe
    for move, point in moves.items():
        if (
            not is_collision(point, my_body) and
            not is_out_of_bounds(point, height, width)
        ):
            # Check for collisions with other snakes
            is_safe = True
            for snake in other_snakes:
                if is_collision(point, snake):
                    is_safe = False
                    break
            if is_safe:
                safe_moves.append(move)

    return safe_moves

def move(game_state: typing.Dict) -> typing.Dict:
    my_head = game_state["you"]["body"][0]
    my_body = game_state["you"]["body"]
    height = game_state["board"]["height"]
    width = game_state["board"]["width"]
    other_snakes = [snake["body"] for snake in game_state["board"]["snakes"] if snake["id"] != game_state["you"]["id"]]

    safe_moves = find_safe_moves(my_head, my_body, height, width, other_snakes)

    if not safe_moves:
        # If there are no safe moves, just select a random one
        safe_moves = ["up", "down", "left", "right"]

    # Choose a random safe move
    chosen_move = random.choice(safe_moves)

    return {"move": chosen_move}

if __name__ == "__main__":
    from server import run_server

    run_server({
        "info": info, 
        "start": start, 
        "move": move, 
        "end": end
    })
