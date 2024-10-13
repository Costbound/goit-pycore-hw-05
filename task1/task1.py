def caching_febonachi():
    cache = {}
    def fibonachi(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            return cache[n]
        
        cache[n] = fibonachi(n - 1) + fibonachi(n - 2)
        return cache[n]
    
    return fibonachi
