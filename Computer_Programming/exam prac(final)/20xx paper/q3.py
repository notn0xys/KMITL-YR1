def find_routes(s:str,routes:dict):
    try:
        temp = routes[s]
        count = temp[1]
        return count + find_routes(temp[0],routes)
    except:
        return 0
    
routes = {
    "i": ("j", 4.0),
    "a": ("b", 3.4),
    "j": ("k", 6.0),
    "c": ("d", 5.6),
    "b": ("c", 4.0)
}
route_a = find_routes("a", routes)
route_b = find_routes("b", routes)
print(route_a)  
print(route_b) 