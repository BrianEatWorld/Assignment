#! /usr/bin/python

import logging
import os
import tornado.ioloop
import tornado.web


def main(directory, port):

    working_directory = ''.join([os.path.abspath(os.path.join(os.path.dirname(__file__), directory)), '/'])
    http_error_page = ''.join([working_directory, '404.html'])

    class MainHandler(tornado.web.RequestHandler):
        def get(self):
            self.render(''.join([working_directory, "/index.html"]))

    # Covered by testMain. This hits and item located in paths[] and the 404 via a malformed url.
    class MainContentHandler(tornado.web.RequestHandler):
        def get(self, path):
            try:
                self.render(''.join([working_directory, path, ".html"]))
            except IOError:
                self.set_status(404)
                self.render(http_error_page)

    class SubContentHandler(tornado.web.RequestHandler):
        def get(self, folder, path):
            try:
                self.render(''.join([working_directory, folder, "/", path, ".html"]))
            except IOError:
                self.set_status(404)
                self.render(http_error_page)

    class CatchAllHandler(tornado.web.RequestHandler):
        def get(self):
            self.set_status(404)
            self.render(http_error_page)

        def head(self):
            if not self.entry:
                self.set_status(404)

    application = tornado.web.Application([
        (r"/", MainHandler),
        (r"/(\w+).html", MainContentHandler),
        (r"/(\w+)/(\w+).html", SubContentHandler),
        (r"/javascript/(.*)", tornado.web.StaticFileHandler, {"path": ''.join([working_directory, 'javascript/'])},),
        (r"/build/(.*)", tornado.web.StaticFileHandler, {"path": ''.join([working_directory, "/build/"])},),
        (r"/stylesheets/(.*)", tornado.web.StaticFileHandler, {"path": ''.join([working_directory, "stylesheets/"])},),
        (r"/images/(.*)", tornado.web.StaticFileHandler, {"path": ''.join([working_directory, "/images/"])},),
        (r"/(favicon.ico)", tornado.web.StaticFileHandler, {"path": working_directory},),
        (r".*", CatchAllHandler),
        ],
        debug=True,
        static_path=working_directory,
        )

    application.listen(port)

def start_tornado():
    logging.basicConfig(level=logging.DEBUG)
    directory = "./semanticUIDocs/"
    port = 8888
    main(directory, port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    directory = "./semanticUIDocs/"
    port = 8888
    main(directory, port)
    tornado.ioloop.IOLoop.instance().start()
    