def populatiry_scores():
    scores = {
        "C++":99.7,
        "Python":96.7,
        "Java":97.5,
        "Rust":97.5,
        "Jom":96
    }
    result = {}
    placement = 0
    end = {}
    val = list(scores.values())
    val.sort()
    val.reverse()
    for item in scores:
        check = False
        for j in result:
            if j == scores[item]:
                result[j] += f" , {item}"
                check = True
                break
        if check == False:
            result[scores[item]] = item

    for k in result:
        placement += 1
        end[placement] = result[k]

    print(end)



populatiry_scores()