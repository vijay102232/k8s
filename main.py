from flask import Flask
import socket, os

app = Flask(_name_)

@app.route('/')
def print_ip():
    hostname = socket.gethostname()
    localip = socket.gethostbyname(hostname)
    return localip
  
 if _name_ == "_main_":
    app.run(host="0.0.0.0",port=80)
