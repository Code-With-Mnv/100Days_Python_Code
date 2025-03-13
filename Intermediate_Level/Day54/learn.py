import time

# from flask import Flask
#
# app = Flask(__name__)
#
#
# @app.route("/")
# def hello_world():
#     return "Hello, World!"


# making decorators
def delay_decorator(function):
    def generating_delay():
        time.sleep(2)
        function()

    return generating_delay


@delay_decorator
def say_hello():
    print("Hello, World!")
