from flask import Flask, render_template, request

import servFunctions

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def index():
	if request.method == 'POST':
		#print(request.get_json())
		test1= servFunctions.getGesture(request.get_json())
		#test1= servFunctions.getGesture(request.form.getlist('k1'))
		countVal = servFunctions.readCounter("count.txt")
		countVal += 1
		servFunctions.writeCounter("count.txt",countVal)
		return render_template("result.html",gesture=test1,gestNum = countVal,gesturelist = servFunctions.gestures)
	elif request.method == "GET":
		return render_template("index.html")

@app.route("/about")
def about():
	return render_template("about.html")

@app.route("/result")
def result():
	countVal = servFunctions.readCounter("count.txt")
	return render_template("result.html", gesture="You're requesting last gestures made, here you are", gestNum= countVal, gesturelist = servFunctions.gestures)


if __name__ == "__main__":
	app.run(host='0.0.0.0',debug=True)