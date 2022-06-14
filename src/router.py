from logger import log_decorator

def match_route(routes, letter):
    for route in routes:
        if route["route"] in letter["Title"]:
            return route


class Router:
    def __init__(self) -> None:
        self._routes = []

    def add_route(self, route_obj):
        self._routes.append(route_obj)
    @log_decorator()
    def letter_handler(self, letter):
        results = {}
        matched_route = match_route(self._routes, letter)
        if not matched_route:
            raise Exception("no route found")
        middlewares = matched_route["middlewares"]
        handler = matched_route["function"]
        def prepare_middlewares(index, letter, results, next):
            if index == -1:
                return next
            def mid():
                return middlewares[index](letter, results, next)
            return prepare_middlewares(index - 1, letter, results, mid);
        
        def hand():
            return handler(letter, results)
        firstMiddleware = prepare_middlewares(len(middlewares)-1, letter, results, hand)
        try:
            firstMiddleware()
        except Exception as e:
            raise Exception(e)