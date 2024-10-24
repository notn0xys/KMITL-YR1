def populatiry_scores():
    scores = {
        "C++":99.7,
        "Python":96.7,
        "Java":97.5,
        "Rust":97.5,
        "Jom":96
    }
    lok = list(scores.values())
    lok.sort()
    lok.reverse()
    meow = dict()
    counter = 1
    past = None
    process = set()
    for i in lok:
        for j in scores:
            if scores[j] == i:
                if past == scores[j]:
                    meow[counter - 1] += f", {j}"
                else:
                    meow[counter] = j
                    counter += 1
                past = scores[j]
                scores.pop(j)
                break
    return meow
            
        
    
print(populatiry_scores())