from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:test@cluster0.bwpfqzd.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/lsspage')
def lsspage():
    return render_template('lss_intro.html')

@app.route('/kbypage')
def kbypage():
    return render_template('kby_intro.html')

@app.route('/chnpage')
def chnpage():
    return render_template('chn_intro.html')

@app.route('/psypage')
def psypage():
    return render_template('psy_intro.html')

@app.route('/jhjpage')
def jhjpage():
    return render_template('jhj_intro.html')

@app.route("/reply", methods=["POST"])
def guestbook_post():
    reply_receive = request.form['reply_give']
    doc = {
        'reply':reply_receive
    }
    db.b4after.insert_one(doc)

    return jsonify({'msg': '저장 완료!'})

@app.route("/reply", methods=["GET"])
def guestbook_get():
    all_reply = list(db.b4after.find({},{'_id':False}))
    return jsonify({'result': all_reply})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)
