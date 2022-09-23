from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")

def index():
    return render_template("index.html")

@app.route("/curriculum", methods=["POST"])

def curriculum():
    name=request.form.get("name")
    date=request.form.get("date")
    occupation=request.form.get("occupation")
    email=request.form.get("email")
    phone=request.form.get("phone")
    nationality=request.form.get("nationality")
    level=request.form.get("level")
    language=request.form.get("language")
    aptitudes=request.form.get("aptitudes")
    skills=request.form.get("skills")
    profile=request.form.get("profile")
    
    return render_template("form.html", name_=name, date_=date, occupation_=occupation, email_=email, phone_=phone, nationality_=nationality, level_=level, language_=language, aptitudes_=aptitudes, skills_=skills, profile_=profile)

if __name__=='__main__':
   app.run()