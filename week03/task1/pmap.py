import subprocess
import ipaddress
import multiprocessing
import argparse

def check_ping(host):
    #调用系统命令，结果不输到终端
    cmd = subprocess.run(['ping', '-c', '1' ,'-W','1', host],stdout=subprocess.PIPE)

    if cmd.returncode == 0:
        return True
    else:
        return False

def check_tcp(host,port):
    #调用系统命令，结果不输到终端
    cmd = subprocess.run(['nc', '-w', '1' ,'-z', host,port],stdout=subprocess.PIPE)

    if cmd.returncode == 0:
        return True
    else:
        return False


def parse_ip(ip_str):

    ip_list = []

    #一个IP地址
    try:
        ip_list.append(ipaddress.ip_address(ip_str))
        return ip_list
    except:
        print('ip 地址输入错误，错误码 -1')

    #检查ip地址分隔符
    if ip_str.find('-') == -1:
        print('ip 地址输入错误，错误码 -2')
        return ip_list

    #输入合法性判断
    ips = ip_str.split('-')
    if len(ips) != 2:
        print('ip 地址输入错误，错误码 -3')
        return ip_list

    try:
        ip_start = ipaddress.ip_address(ips[0])
        ip_end = ipaddress.ip_address(ips[1])
    except:
        print('ip 地址输入错误，错误码 -4')
        return ip_list

    #将IP地址转化为整数，方便比较
    ip_start_int = int(ip_start) 
    ip_end_int = int(ip_end)

    if ip_start_int > ip_end_int:
        print('ip 地址输入错误，错误码 -5')
        return ip_list

    while(ip_start_int <= ip_end_int):
        ip_list.append(ipaddress.ip_address(ip_start_int))
        ip_start_int = ip_start_int + 1

    return ip_list

def parse_ip2(ip_str):
    try:
        return ipaddress.ip_address(ip_str)
    except:
         print('ip 地址输入错误，错误码 -6')

def process_ping_run(concurrent_num,ip_str):

    p = multiprocessing.Pool(concurrent_num)

    for ip in parse_ip(ip_str):
        result = p.apply_async(check_ping, args=(str(ip),))
        print(f'{str(ip)} -- {result.get()}')

    p.close()
    p.join()
    p.terminate()

def process_tcp_run(concurrent_num,ip_str):

    p = multiprocessing.Pool(concurrent_num)

    for i in range(1024):
        result = p.apply_async(check_tcp,args=(str(ip_str),str(i+1),))
        if result.get() == True:
            print(f'{str(ip_str)} --{str(i+1)}-- {result.get()}')

    p.close()
    p.join()
    p.terminate()


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='网络扫描器')
    
    parser.add_argument('-n',type=int,default=1,metavar=1,required=True,help='扫描请求的并发数，默认值为 1')
    parser.add_argument('-f',choices=['ping','tcp'],default='ping',metavar='ping',required=True,help='扫描协议：ping 或者 tcp，默认值为ping')
    parser.add_argument('-ip',metavar='192.168.1.1',required=True,help='扫描对象：192.168.1.1 或者 192.168.1.1-192.168.1.255，无默认值')

    args = parser.parse_args()
    
    if args.f == 'ping':
        process_ping_run(args.n,args.ip)
    elif args.f == 'tcp':
        process_tcp_run(args.n,args.ip)