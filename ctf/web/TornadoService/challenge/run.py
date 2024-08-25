import tornado.ioloop

from application.main import APP

if __name__ == "__main__":
    APP.listen(1337, address="0.0.0.0")
    tornado.ioloop.IOLoop.current().start()
