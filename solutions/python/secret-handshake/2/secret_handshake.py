actions = ("wink", "double blink", "close your eyes", "jump")

def commands(binary_str):
    action_que = []
    number = int(binary_str, 2)
    for index, action in enumerate(actions):
        if number & (1 << index):
            action_que.append(action)
    if number & (1 << 4):
        action_que.reverse()
    
    return action_que
