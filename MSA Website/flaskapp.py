from flask import Flask, render_template, url_for, session, request, redirect
from datetime import timedelta
app = Flask("__name__", static_url_path='/static')
app.secret_key = "linusplsstop"
app.permanent_session_lifetime = timedelta(minutes=1)
@app.route("/")
def main():
	return render_template("index.html")
@app.route("/survey", methods=["POST", "GET"])
def survey():
	if request.method == "POST":
		session.permanent = True
		question1 = request.form["happiness"]
		session["question1"] = question1
		question2 = request.form["usage"]
		session["question2"] = question2
		question3 = request.form["sleep"]
		session["question3"] = question3
		question4 = request.form["remember"]
		session["question4"] = question4
		question5 = request.form["ridicule"]
		session["question5"] = question5
		question6 = request.form["missing out"]
		session["question6"] = question6
		question7 = request.form["mindless"]
		session["question7"] = question7
		question8 = request.form["relationship"]
		session["question8"] = question8
		question9 = request.form["mostusedapp"]
		session["question9"] = question9
		question10 = request.form["appearance"]
		session["question10"] = question10
		question11 = request.form["age"]
		session["question11"] = question11
		return redirect(url_for("response"))
	else:
		if "question1" in session:
			return redirect(url_for("response"))
		return render_template("survey.html")
@app.route("/about")
def about():
		return render_template("about.html")
@app.route("/response")
def response():
	if "question1" in session:
		question1 = session["question1"]
		question2 = session["question2"]
		question3 = session["question3"]
		question4 = session["question4"]
		question5 = session["question5"]
		question6 = session["question6"]
		question7 = session["question7"]
		question8 = session["question8"]
		question9 = session["question9"]
		question10 = session["question10"]
		question11 = session["question11"]
		#Happiness scale
		#happiness = int(question1)
		#Time spent Scale
		#time = 20 * int(question2)
		#Sleep Scale
		##if question3 == "yes":
		#	sleep = 0
		#if question3 == "no":
		#	sleep = 1

		#Wasted time scale
		if question4 == "yes":
			wasted = 0
		if question4 == "no":
			wasted = 50
		if question4 == "only some":
			wasted = 25

		if question7 == "yes":
			wasted += 50
		elif question7 == "no":
			wasted = wasted
		elif question7 == "waiting":
			wasted += 25
		elif question7 == "sometimes":
			wasted += 40
		#Social interaction Scale
		if int(question5) == 1:
			socialInteraction = 0
		if int(question5) == 2:
			socialInteraction = 11
		if int(question5) == 3:
			socialInteraction = 24
		if int(question5) == 4:
			socialInteraction = 40
		if int(question5) == 5:
			socialInteraction = 50

		if int(question8) == 1:
			socialInteraction += 50
		if int(question8) == 2:
			socialInteraction += 40
		if int(question8) == 3:
			socialInteraction += 24
		if int(question8) == 4:
			socialInteraction += 11
		if int(question8) == 5:
			socialInteraction += 0
		#FoMO Scale
		if question6 == "yes":
			fomo = 100
		if question6 == "no":
			fomo = 0
		if question6 == "sometimes":
			fomo = 50
		#Self Confidence Scale
		if int(question10) == 1:
			confidence = 0
		if int(question10) == 2:
			confidence = 25
		if int(question10) == 3:
			confidence = 50
		if int(question10) == 4:
			confidence = 80
		if int(question10) == 5:
			confidence = 100

		return render_template("response.html", wasted= wasted, interaction= socialInteraction , fomo= fomo, confidence= confidence)
		session.clear()
	else:
		return redirect(url_for("survey"))
@app.route("/logout")
def logout():
	[session.pop(key) for key in list(session.keys())]
	return redirect(url_for("survey"))
if __name__ == "__main__":
	app.run()