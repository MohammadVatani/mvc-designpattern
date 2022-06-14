import apps.monthly_report.config as c

def middle1(letter, results, next):
    print("middle1")
    next()

def middle2(letter, results, next):
    print("middle2")
    next()

def func(letter, results):
    print("function")
    print(results)

routes = {
    c.MONTLY_REPORT: {
        "function": func,
        "middlewares": [middle1,middle2]
    }
}