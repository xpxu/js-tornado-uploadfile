import tornado.ioloop  
import tornado.web  
  
  
class MainHandler(tornado.web.RequestHandler):  
 
    def get(self):  
        self.write("Hello, world")
  
class UploadHandler(tornado.web.RequestHandler):  

    def set_default_headers(self):
        print "setting headers!!!"
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "*")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def post(self):  
        if self.request.files:  
            myfile = self.request.files['mof'][0]  
            fin = open("uploadfile","ab")    
            print "success to open file"  
            fin.write(myfile["body"])  
            fin.close()  

    def options(self):
        self.set_status(204)
        self.finish
 
application=tornado.web.Application([(r'/',MainHandler),(r'/upload', UploadHandler)])

if __name__=='__main__':  
    application.listen(2033)  
    tornado.ioloop.IOLoop.instance().start()  
