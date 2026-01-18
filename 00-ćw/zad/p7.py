def f(car, order):
    filtered_cars = [x for x in car if list(x.values())[0] > 200]

    if order == 1:
        return sorted(filtered_cars, key=lambda x: list(x.keys())[0])
    elif order == 2:
        return sorted(filtered_cars, key=lambda x: list(x.keys())[0], reverse=True)
    return filtered_cars

if __name__ == "__main__":
    cars = [{"KR333":138}, {"WL555":497}, {"DB444":341}, {"MC222":412}]
    # KR333 ma 138 km, więc powinien wylecieć w obu przypadkach!
    
    print(f(cars, 1)) 
    # Oczekiwany wynik (alfabetycznie, bez KR333): 
    # [{'DB444': 341}, {'MC222': 412}, {'WL555': 497}]
    
    print(f(cars, 2)) 
    # Oczekiwany wynik (przebieg malejąco, bez KR333): 
    # [{'WL555': 497}, {'MC222': 412}, {'DB444': 341}]