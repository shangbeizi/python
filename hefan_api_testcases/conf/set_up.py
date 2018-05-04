import time,os,pymysql,logging

def report():
    report_file_name = '测试报告'+str(time.strftime('%Y-%m-%d'+'_'+'%H_%M_%S',time.localtime(time.time()))+'.html')
    output_path =str(os.path.abspath(os.path.dirname(os.path.dirname(__file__)))+'\logs')
    log_path = output_path + '\\' + report_file_name
    return log_path


def mysql(addr,user,pwd,db,cmd) :
    try:

        try:
            conn = pymysql.connect(addr, user, pwd, db,charset='utf8')
        except Exception as e:
            return e

        cur=conn.cursor()
        cur.execute(cmd)
        result=cur.fetchall()

        conn.commit()
        cur.close()
        conn.close()
        return result

    except Exception as e :
        print(e)



def creatlogdir():
    project_dir = os.path.dirname(os.path.abspath(__file__))
    logfile_dir = str(project_dir) + r'/logs'
    logfile_dir = logfile_dir.strip()
    logfile_dir = logfile_dir.rstrip('\\')

    isExists=os.path.exists(logfile_dir)
    if not isExists:
        os.makedirs(logfile_dir)
    else:
        pass


