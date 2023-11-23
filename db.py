import oracledb

USER_ID = 'test'
PASSWORD = '1234'
DNS = '127.0.0.1:1521/xe'

def insertBadge(request, imageName):
    con = oracledb.connect(user=USER_ID, password=PASSWORD, dsn=DNS)
    cursor = con.cursor()

    cursor.execute("SELECT badge_seq.NEXTVAL FROM DUAL")
    badge_seq = cursor.fetchone()[0]

    sql = "INSERT INTO badge VALUES(%d, '%s', '%s', '%s', '%s', TO_DATE('%s', 'YYYYMMDDHH24MISS'))" % (badge_seq, imageName, request.form['badgeName'], request.form['content'], request.form['detailContent'], request.form['createDt'])

    cursor.execute(sql)
    con.commit()
    con.close()

    return badge_seq

def selectBadge(badgeId):
    con = oracledb.connect(user=USER_ID, password=PASSWORD, dsn=DNS)
    cursor = con.cursor()

    cursor.execute("SELECT * FROM badge WHERE badgeId = %d" % badgeId)
    badge = cursor.fetchone()
    con.close()

    return badge

def insertUser(payload):
    con = oracledb.connect(user=USER_ID, password=PASSWORD, dsn=DNS)
    cursor = con.cursor()

    sql = "INSERT INTO userTb VALUES(%d, '%s', '%s', '%s', '%s')" % (payload['userId'], payload['userName'], payload['email'], payload['team'], payload['position'])
    cursor.execute(sql)
    con.commit()
    con.close()
def selectUser(userId):
    con = oracledb.connect(user=USER_ID, password=PASSWORD, dsn=DNS)
    cursor = con.cursor()

    cursor.execute("SELECT * FROM usertb WHERE userId = %d" % userId)
    user = cursor.fetchone()
    con.close()

    return user

def insertUserBadge(payload):
    con = oracledb.connect(user=USER_ID, password=PASSWORD, dsn=DNS)
    cursor = con.cursor()

    sql = "INSERT INTO userBadge VALUES(%d, %d, TO_DATE('%s', 'YYYYMMDDHH24MISS'))" % (payload['badgeId'], payload['userId'], payload['createDt'])
    cursor.execute(sql)
    con.commit()
    con.close()

def selectMyBadge(userId):
    con = oracledb.connect(user=USER_ID, password=PASSWORD, dsn=DNS)
    cursor = con.cursor()

    sql = """
        SELECT A.BADGEID, A.IMAGE, A.BADGENAME, B.CREATEDT  
        FROM BADGE A
        JOIN USERBADGE B
          ON A.BADGEID = B.BADGEID 
        WHERE B.USERID = %s
    """ % userId

    cursor.execute(sql)
    results = cursor.fetchall()
    myBadge = []

    for badge in results:
        myBadge.append({"badgeId":badge[0],"image":badge[1],"badgeName":badge[2],"createDt":badge[3].strftime("%Y%m%d%H%M%S")})
    con.close()

    return myBadge

if __name__ == "__main__":
    print("Test")