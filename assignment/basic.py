#! /usr/bin/python

import logging
import os
import tornado.ioloop
import tornado.web
import sys

logging.basicConfig(level=logging.DEBUG)

directory="./semanticUIDocs/"

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render(directory + 'index.html')

# Covered by testMain. This hits and item located in paths[] and the 404 via a malformed url.
class MainContentHandler(tornado.web.RequestHandler):
    def get(self, path):
    	logging.info(path)
        paths = ("collection", "download","element", "introduction","module","playground","test")
        if not path: path = "index"
        if path not in paths:
            self.render(directory + '404.html')
            raise tornado.web.HTTPError(404)
        logging.info(directory + path + ".html")
        self.render(directory + path + ".html")

class SubContentHandler(tornado.web.RequestHandler):
    def get(self,folder,path):
    	logging.info(folder)
    	logging.info(path)
        folders = ("collections","draft","elements","guide","introduction","modules","overrides","project","spec","views")
        if folder not in folders:
            self.render(directory + '404.html')
            raise tornado.web.HTTPError(404)
        logging.info(directory + folder +"/"+ path + ".html")
        self.render(directory + folder +"/"+ path + ".html")


class CatchAllHandler(tornado.web.RequestHandler):
	def get(self):
		self.set_status(404)
		self.render(directory + '404.html')

	def head(self):
		if not self.entry:
			self.set_status(404)

settings = {
    "static_path": os.path.join(os.path.dirname(__file__), directory ),
    "debug":True,
}

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/(\w+).html", MainContentHandler),
    (r"/(\w+)/(\w+).html", SubContentHandler),
    (r"/javascript/(.*)",tornado.web.StaticFileHandler,{"path":os.path.join(os.path.dirname(__file__), directory) + "javascript/"},),
    (r"/build/(.*)",tornado.web.StaticFileHandler,{"path":os.path.join(os.path.dirname(__file__), directory) + "build/"},),
    (r"/stylesheets/(.*)",tornado.web.StaticFileHandler,{"path":os.path.join(os.path.dirname(__file__), directory) + "stylesheets/"},),
    (r"/images/(.*)",tornado.web.StaticFileHandler,{"path":os.path.join(os.path.dirname(__file__), directory) + "images/"},),
    (r"/(favicon.ico)",tornado.web.StaticFileHandler,{"path":directory},),
    (r".*", CatchAllHandler),
    ])

if __name__ == "__main__":
    logging.info("Path:"+os.path.join(os.path.dirname(__file__), directory ))
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
