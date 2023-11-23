from flask import Flask, request
from werkzeug.utils import secure_filename
import uuid
import db

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/badge', methods=['POST'])
def badgePost():
    badgeId = -1

    try:
        image = request.files['image']
        imageName = secure_filename(str(uuid.uuid1()) + "." + image.filename.rsplit('.', 1)[1])
        image.save('./static/' + imageName)
        imageName = "http://1.227.28.126:9049/static/" + imageName
        badgeId = db.insertBadge(request, imageName)
    except Exception as ex:
        return {"description":"잘못된 요청","Exception":ex}, 400

    return {"description":"뱃지가 성공적으로 등록되었습니다.", "badgeId":badgeId}, 201

@app.route('/badge', methods=['get'])
def badgeGet():
    badgeId = int(request.values.get("badgeId"))

    try:
        badge = db.selectBadge(badgeId)
    except Exception as ex:
        return {"description":"뱃지를 찾을 수 없음","Exception":ex}, 400

    return {"description":"작업이 성공적으로 수행되었습니다.","badgeId":badge[0],"image":badge[1],"badgeName":badge[2],"content":badge[3],"detailContent":badge[4],"createDt":badge[5].strftime("%Y%m%d%H%M%S")}, 200

@app.route('/user', methods=['post'])
def userPost():
    payload = request.get_json()

    try:
        db.insertUser(payload)
    except Exception as ex:
        return {"description":"잘못된 요청","Exception":ex}, 400

    return {"description":"작업이 성공적으로 수행되었습니다."}, 200

@app.route('/user', methods=['get'])
def userGet():
    userId = int(request.values.get("userId"))

    try:
        user = db.selectUser(userId)
    except Exception as ex:
        return {"description":"사용자를 찾을 수 없음","Exception":ex}, 400

    return {"description":"작업이 성공적으로 수행되었습니다.","userId":user[0],"userName":user[1],"email":user[2],"team":user[3],"position":user[4]}, 200

@app.route('/mybadge', methods=['post'])
def myBadgePost():
    payload = request.get_json()

    try:
        db.insertUserBadge(payload)
    except Exception as ex:
        return {"description":"잘못된 요청","Exception":ex}, 400

    return {"description":"뱃지가 성공적으로 수여되었습니다."}, 201

@app.route('/mybadge/<int:userId>', methods=['get'])
def myBadgeGet(userId):
    try:
        myBadge = db.selectMyBadge(userId)
        pass
    except Exception as ex:
        return {"description":"잘못된 요청","Exception":ex}, 400

    return {"description":"뱃지가 성공적으로 수여되었습니다.","items":myBadge}, 201

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)