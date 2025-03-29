def union(objectA, objectB):
    '''takes in the set of spheres and unions them into one set and removes
       any redundant spheres

    Args:
        objectA (set of tuples): first set to be unioned
        objectB (set of tuples): seconnd set to be unioned

    Returns:
        union_set (set of tuples): the union of objectA and B with redundant
            spheres removed
    '''
    union_set = objectA.union(objectB)
    spheres_to_remove = set()
    for sphere_1 in union_set:
        for sphere_2 in union_set:
            if sphere_1 != sphere_2:
                # for every sphere check every other sphere, unless it is
                # itself, no duplicates in sets so no worry about overlap if
                # spheres are equal
                x_expres = (sphere_1[0] - sphere_2[0])**2
                y_expres = (sphere_1[1] - sphere_2[1])**2
                z_expres = (sphere_1[2] - sphere_2[2])**2
                square_root = (x_expres + y_expres + z_expres)**0.5
                left_side_equation = square_root + sphere_1[3]
                # complete equation broken down
                if left_side_equation <= sphere_2[3]:
                    spheres_to_remove.add(sphere_1)
    union_set = union_set - spheres_to_remove
    return union_set
