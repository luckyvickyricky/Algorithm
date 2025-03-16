from collections import deque


def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5
    
    cache = deque()
    runtime = 0
    
    for city in cities:
        city = city.lower()
        if city in cache:
            runtime += 1
            cache.remove(city)
            cache.append(city)
        else:
            runtime += 5
            if len(cache) >= cacheSize:
                cache.popleft()
            cache.append(city)
    
    return runtime