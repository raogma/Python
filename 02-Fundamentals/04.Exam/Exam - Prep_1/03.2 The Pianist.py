def fill_iterable(iterable, count):
    for _ in range(count):
        song, composer, type = input().split('|')
        iterable[song] = {'composer': composer, 'type': type}


def printing(iterable):
    res = str()
    iterable = dict(sorted(iterable.items(), key=lambda x: (x[0], x[1]['composer'])))
    for key in iterable:
        res += f"{key} -> Composer: {iterable[key]['composer']}, Key: {iterable[key]['type']}\n"
    return res


n_lines = int(input())

collection = {}
fill_iterable(collection, n_lines)

while True:
    command = input()
    if command == 'Stop':
        print(printing(collection))
        break

    action, value = command.split('|', maxsplit=1)
    if action == 'Add':
        target_song, artist, song_type = value.split('|')
        if target_song in collection:
            print(f"{target_song} is already in the collection!")
        else:
            collection[target_song] = {'composer': artist, 'type': song_type}
            print(f"{target_song} by {artist} in {song_type} added to the collection!")
    elif action == 'Remove':
        target_song = value
        for key in collection:
            if key == target_song:
                del collection[key]
                print(f"Successfully removed {target_song}!")
                break
        else:
            print(f"Invalid operation! {target_song} does not exist in the collection.")

    elif action == 'ChangeKey':
        target_song, new_type = value.split('|')
        if target_song in collection:
            collection[target_song]['type'] = new_type
            print(f"Changed the key of {target_song} to {new_type}!")
        else:
            print(f"Invalid operation! {target_song} does not exist in the collection.")
