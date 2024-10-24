def find_route(s:str,routes:dict):
    total_distance = 0
    route = []
    if s not in routes.keys():
        return "Path Not found"
    while True:
        try:
            temp_var = routes[s]
            route.append(s)
            total_distance += temp_var[1]
            s = temp_var[0]
        except:
            route.append(s)
            break
    return (route,total_distance)
routes = {
    "i": ("j", 4.0),
    "a": ("b", 3.4),
    "j": ("k", 6.0),
    "c": ("d", 5.6),
    "b": ("c", 4.0)
}
route_a = find_route("a", routes)
route_b = find_route("b", routes)
print(find_route("h",routes))
print(route_a)  
print(route_b) 