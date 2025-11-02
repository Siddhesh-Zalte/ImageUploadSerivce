import tornado.web as tw
import tornado.ioloop as ti



if (__name__=="__main__"):
    app =tw.Application(
        [
            #("/", uploadHandler),
            ("/(.*)", tw.StaticFileHandler, {"path":"img"})
        ]
    )
    app.listen(8082)
    print("Listening on port 8080")

    ti.IOLoop.instance().start()

