# encoding:utf8

"""
"""

import time
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

from database import DataBase
from ip_location.ip2Region import Ip2Region

searcher = Ip2Region('./ip_location/ip2region.db')  # IP定位

def ip2region(ip=None):
    """
    得到IP的地理位置和运营商
    :param ip: 待查询IP
    :return
        city: ip所在城市，若城市为空，则为国家
        network_operator: 运营商，可能为空
    """
    if ip == "" or ip is None:
        return

    data = searcher.btreeSearch(ip)
    region = data['region']
    region = region.split('|')
    province = region[2]
    city = region[3]
    operater = region[4]

    return province,city,operater


def main(tb_name,fp_name):
    """主流程"""
    DB = DataBase()
    DB.db_connect()
    DB.execute_no_return("USE cyn_test")

    fp_name = './result/' + fp_name
    fp = open(fp_name,'r')

    net_list = fp.readlines()
    for ip_net in net_list:
        ip_split = ip_net.strip().split(' ')
        ip = ip_split[0]
        packet_loss = float(ip_split[1])
        rtt = float(ip_split[2])
        delay_var = float(ip_split[3])
        path_len = int(ip_split[4])
        cdate = ip_split[5]
        ctime = ip_split[6]
        pro,city,oper = ip2region(ip)
        SQL = """INSERT INTO {table} SET `ip` = '{ip}' ,`date` = '{cdate}' ,`time` = '{ctime}' ,`path_len` = {path_len} ,`RTT` = '{rtt}',`delay_var` = '{delay_var}',`packet_loss` = '{packet_loss}',`province` = '{province}' ,`city` = '{city}' ,`operater` = '{oper}' """.format(
            table=tb_name, ip=ip, cdate=cdate, ctime=ctime, path_len=path_len, rtt=rtt,delay_var=delay_var,packet_loss=packet_loss,province=pro,city=city,oper=oper
        )
        DB.execute_no_return(SQL)

    fp.close()
    DB.db_commit()
    DB.db_close()


if __name__ == '__main__':

    main('net_result_bj_sd','bj_sd.txt')