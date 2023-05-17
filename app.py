from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:test@cluster0.zoedaxq.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/teams/members/seongsu')
def lsspage():
    return render_template('lss_intro.html')

@app.route('/teams/members/boyoung')
def kbypage():
    return render_template('kby_intro.html')

@app.route('/teams/members/haena')
def chnpage():
    return render_template('chn_intro.html')

@app.route('/teams/members/seoyeon')
def psypage():
    return render_template('psy_intro.html')

@app.route('/teams/members/hojin')
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

@app.route("/reply", methods=["DELETE"])
def guestbook_delete():
    Delreply_receive = request.form['Delreply_give']
    db.b4after.delete_one({'reply':Delreply_receive})
    return jsonify({'msg': '삭제 완료!'})
   
@app.route("/reply", methods=["PUT"])
def guestbook_put():
    Modreply_receive = request.form['Modreply_give']
    reply_receive = request.form['reply_give']    
    db.b4after.update_one({'reply':reply_receive},{'$set':{'reply':Modreply_receive}})
    return jsonify({'msg': '수정 완료!'})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)
