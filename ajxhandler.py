from flask import Flask, jsonify
from flask import request
from flask import render_template
app = Flask(__name__)

@app.route('/')
def inex(): 
	return render_template("forms.html")
@app.route('/echo/', methods = ['GET','POST'])
def recieve():
	color = request.args.get('color')
	if color == "blue" :
		retcolor = "#0000FF"
	if color == "red" :
		retcolor = "#FF0000"
	
	ret_data = {"value": request.args.get('echoValue'), "color": retcolor}
	return jsonify(ret_data)
	
  
	
	
if __name__ == '__main__':
    app.run(debug = True)
