# create your dictionary here

objects_dict = {}


for obj in objects:
    try:
        hash(obj)
    except TypeError:
        continue
    else:
        objects_dict[obj] = hash(obj)
