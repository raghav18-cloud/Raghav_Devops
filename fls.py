from flask import Flask

app = Flask(__name__)



@app.route('/')                         ####@app.route(/) is decorator, basically routing the request..and next return the value for it.

@app.route('/hello')

def Helloworld():

   return "Hello From Aetna!!We are healthcare company.!!! This is our First product Release!!!!Adding Second product Release!!!!!!"



if __name__ == '__main__':

   app.debug = True

   app.run(host = '0.0.0.0', port = 5006)
