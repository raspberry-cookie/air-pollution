import pm2008
import gps
import find_id
import time
import threading
from collections import defaultdict
from database import insert_raspdb
from database import check_tables
from database import update_raspdb

def collect_air_quality(data: defaultdict):
    pm2_5, pm10 = pm2008.pm2008()
    # co = co.co()
    co = 4.5
    data["pm2_5"] = pm2_5
    data["pm10"] = pm10
    data['co'] = co
    data['air_index'] = 10 
    # threading.Timer(1,collect(data)).start()
    # time.sleep(1)

    print(data)

def collect_gps(gps_data: defaultdict):
    lat, lon = gps.getGps()
    gps_data["lat"] = lat
    gps_data["lon"] = lon
    
    print(gps_data)

if __name__ == "__main__":
    data = defaultdict()
    gps_data = defaultdict()
    # id 설정 
    id = find_id.get_serial()
    network_condition = True 
    # 1이면 중복id  존재 
    if (check_tables.check_device(id) == 1):
        update_raspdb.insert_raspdb_device(id,network_condition)
    else:
        insert_raspdb.insert_raspdb_device(id,network_condition)

    # t = threading.Thread(target = collect, args=(data,))
    # t.start()

    ######### 여기부터 
    collect_air_quality(data)
    if (check_tables.check_air_quality(id) == 1):
        update_raspdb.insert_raspdb_air_quality(id,data["co"], data["pm2_5"], data["pm10"],data["air_index"])
    else:
        insert_raspdb.insert_raspdb_air_quality(id, data["co"], data["pm2_5"], data["pm10"],data["air_index"])
    
    collect_gps(gps_data)
    if (check_tables.check_gps(id) == 1):
        update_raspdb.insert_raspdb_gps(id,gps_data["lat"],gps_data["lon"])
    else:
        insert_raspdb.insert_raspdb_gps(id,gps_data["lat"],gps_data["lon"])
    ######### 여기까지 1초에 한번씩 시행
    
