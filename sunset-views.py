def sunsetViews(buildings, direction):
    if len(buildings) == 0:
        return []
    elif len(buildings) == 1:
        return [0]

    indexes = []

    if direction == "EAST":
        # loop from the end
        i = len(buildings) - 1
        tallest = buildings[i]
        indexes.append(i)
        while i >= 0:
            i -= 1
            if buildings[i] > tallest:
                tallest = buildings[i]
                indexes.append(i)
        return indexes[::-1]

    if direction == "WEST":
        # loop from the start
        i = 0
        tallest = buildings[0]
        indexes.append(i)
        while i < len(buildings) - 1:
            i += 1
            if buildings[i] > tallest:
                tallest = buildings[i]
                indexes.append(i)
        return indexes

    return []


# buildings = [3, 5, 4, 4, 3, 1, 3, 2]
# direction = "EAST"
buildings = [3, 5, 4, 4, 3, 1, 3, 2]
direction = "WEST"
out = sunsetViews(buildings, direction)
print(out)
