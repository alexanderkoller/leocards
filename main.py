import cherrypy
from flask import Flask, render_template, send_from_directory, request, flash, redirect, url_for
from flask_wtf import Form, FlaskForm
from wtforms import TextField, StringField

import backend
import conf
import leo


app = Flask(__name__)
app.secret_key = 'lkjasdlkajsd'
# app.debug = True
app.jinja_env.filters['zip'] = zip


sections = [('section-subst', "Substantive"),
            ('section-verb', "Verben"),
            ('section-adjadv', "Adjektive/Adverbien"),
            ('section-praep', "Präpositionen/Pronomen/..."),
            ('section-phrase', "Phrasen"),
            ('section-example', "Beispiele")]

    
class WordForm(FlaskForm):
    word = StringField("Dieses Wort nachschlagen")

    
@app.route("/", methods=("GET",))
def main():
    form = WordForm()
    return render_template("main.html", form=form, from_dict={}, to_dict={}, sections=sections)

@app.route("/", methods=("POST",))
def do_main():
    form = WordForm()
    if form.validate_on_submit():
        from_dict, to_dict = leo.lookup(form.word.data)
        return render_template("main.html", form=form, from_dict=from_dict, to_dict=to_dict, sections=sections)
    else:
        return render_template("main.html", form=form, from_dict={}, to_dict={}, sections=sections)

@app.route("/save_vocab")
def save_vocab():
    f = request.args.get("from")
    t = request.args.get("to")

    response = backend.add_vocab(f, t)

    if response == 200:
        flash("Wort hinzugefügt: %s / %s" % (f, t))
        return redirect("/")
    else:
        flash("Fehler!")
        return redirect("/")


@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)



cherrypy.tree.graft(app.wsgi_app, '/')
cherrypy.config.update({'server.socket_host': '0.0.0.0',
                        'server.socket_port': conf.port,
                        'engine.autoreload.on': False,
                        })

if __name__ == '__main__':
    cherrypy.engine.start()
