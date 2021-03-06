import pymysql

def update_raspdb_air_quality(id: str, ozone: float, co: float, pm2_5: int, pm10: int, air_index: int):
    #connect to database
    db = pymysql.connect(host='localhost',user= 'root',password='raspberry',db='raspdb',charset='utf8')
    cur = db.cursor()

    #insert
    sql = "UPDATE air_quality_sensor SET ozone=%s, co=%s, pm25=%s, pm10=%s, air_index=%s WHERE device_id=%s"
    val = (ozone, co, pm2_5, pm10,air_index,id)
    cur.execute(sql,val)

    db.commit()

    print(f"raspDB: {cur.rowcount} air_quality record updated")

def update_raspdb_location(geohash: str, latitude: float, longitude: float, timestamp: str):
    #connect to database
    db = pymysql.connect(host='localhost',user= 'root',password='raspberry',db='raspdb',charset='utf8')
    cur = db.cursor()

    #insert
    sql = "UPDATE location SET receive_time=%s, latitude=%s, longitude=%s WHERE geohash=%s"
    val = (timestamp, latitude, longitude, geohash)
    cur.execute(sql,val)

    db.commit()

    print(f"raspDB: {cur.rowcount} gps record updated")

def update_raspdb_device(id: str, network_condition: bool, timestamp: str):
    #connect to database
    db = pymysql.connect(host='localhost',user= 'root',password='raspberry',db='raspdb',charset='utf8')
    cur = db.cursor()

    #insert
    sql = "UPDATE device SET network_condition=%s, last_updated_time=%s WHERE device_id=%s"
    val = (network_condition,timestamp, id)
    cur.execute(sql,val)

    db.commit()

    print(f"raspDB: {cur.rowcount} device record updated")




