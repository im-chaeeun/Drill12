objects = [[] for _ in range(4)]

# fill here
collision_pairs = {} # {'boy:ball' : [[boy], [balls]]}


def add_object(o, depth = 0):
    objects[depth].append(o)

def add_objects(ol, depth = 0):
    objects[depth] += ol


def update():
    for layer in objects:
        for o in layer:
            o.update()


def render():
    for layer in objects:
        for o in layer:
            o.draw()


def add_collision_pair(group, a = None, b = None): # a, b 충돌 검사
    if group not in collision_pairs:
        print(f'new group {group} added...')
        collision_pairs[group] = [ [], [] ]
    if a:
        collision_pairs[group][0].append(a)
    if b:
        collision_pairs[group][1].append(b)


def remove_collision_object(o):
    for pairs in collision_pairs.values():
        if o in pairs[0]:
            pairs[0].remove(o)
        if o in pairs[1]:
            pairs[1].remove(o)


def remove_object(o):
    for layer in objects:
        if o in layer:
            layer.remove(o)
            remove_collision_object(o)
            del o # 메모리도 날려 주도록
            return
    raise ValueError('충돌x')


def clear():
    for layer in objects:
        layer.clear()

# fill here
def collide(a, b):
    la, ba, ra, ta = a.get_bb()
    lb, bb, rb, tb = b.get_bb()

    if la > rb: return False
    if ra < lb: return False
    if ta < bb: return False
    if ba > tb: return False
    return True

def handle_collisions():
    for group, pairs in collision_pairs.items():
        for a in pairs[0]:
            for b in pairs[1]:
                if collide(a, b): # a, b 충돌처리 해라
                    a.handle_collision(group, a)
                    b.handle_collision(group, b)


    return None