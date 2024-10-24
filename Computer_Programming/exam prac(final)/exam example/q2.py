def popularity_scores(d:dict):
    sorted_dict = dict(sorted(d.items(), key=lambda item: item[1],reverse=True))
    return_dict = dict()
    last = None
    counter = 1
    for i in sorted_dict:
        if last == sorted_dict[i]:
            return_dict[counter - 1] += f", {i}"
        else:
            return_dict[counter] = i
            counter += 1
        last = sorted_dict[i]
    return return_dict
scores = {
    "Python":89,
    "C++":78,
    "Rust":99,
    "TypeScript":88,
    "React":87
}
print(popularity_scores(scores))