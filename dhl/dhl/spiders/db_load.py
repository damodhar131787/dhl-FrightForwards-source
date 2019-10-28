import sys 
from datetime import datetime
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="dbms",
  database="damu"
)

mycursor = mydb.cursor()
now=datetime.now()
file_read=open('/home/headrun/task/sample.csv','r')

#print("start_time:",str(datetime.now()))
count=0
#sources=['abf', 'sefl', 'yrc', 'aduiepyle', 'averitt', 'ups', 'dohrntransfer', 'manitoulin', 'pittohio', 'saia', 'odfl', 'dayton', 'estes', 'central_freight', 'central_transport', 'landair', 'hiway', 'magnum', 'midland', 'ohfl', 'vitran', 'roadtex', 'rlcarriers', 'nmtransfer', 'newpenn', 'dayross', 'usf_holland', 'usf_reddaway', 'roadrunner', 'aaacooper', 'cctc']
#sources_names=['abf']
source_name=sys.argv[1]
for data in file_read:
    source=data.split(',')[0]
    if source.strip().lower() == source_name.strip().lower():
        track_number=data.split(',')[-1].strip()
        if 'E' in track_number:
            try:
                track_number=  "%.f" % float(track_number)
            except:
                track_number=track_number
        querystring = {"source":"{}".format(source),"tracking_id":"{}".format(track_number)}
        if count <=10:
            sql = "INSERT IGNORE  INTO inputs_tracking_queue1 (source,tracking_id,crawl_status,final_status,crawl_type,extra_info,hash_key,modified_at,created_at) VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s)"
            val=(source,track_number,'0','inserted','keepup','','',now,now)
            mycursor.execute(sql, val)
            mydb.commit()
            print(mycursor.rowcount, "record inserted.")
        else:
            pass
        count+=1
    else:
        pass
#print("end_time",str(datetime.now()))
