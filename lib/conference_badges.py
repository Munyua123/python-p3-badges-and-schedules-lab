def badge_maker(name):
    return (f"Hello, my name is {name}.")

print(badge_maker("Arel"))

def batch_badge_creator(names):
    badge_names = []
    for name in names:
         badge_names.append(f"Hello, my name is {name}.")
    return badge_names

print(batch_badge_creator(["Arel", "Carol", "Bob", "David"]))

def assign_rooms(names):
    badge_names = []
    numbers = 1 
    for name in names:
        badge_names.append(f"Hello, {name}! You'll be assigned to room {numbers}!")
        numbers += 1
    return badge_names
print(assign_rooms(["Arel", "Carol", "Bob", "David"]))

def printer(names):
    badge_names = batch_badge_creator(names)

    for message in badge_names:
        print(message)
    
    room_assignments = assign_rooms(names)

    for assignment in room_assignments:
        print(assignment)
        
printer(["Arel", "Carol", "Bob", "David"])
