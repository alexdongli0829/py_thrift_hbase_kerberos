from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from hbase import Hbase
from hbase.ttypes import *

import os


thriftServer = "ec2-52-63-250-197.ap-southeast-2.compute.amazonaws.com"
thriftPort = 9090
saslServiceName = "hbase"

tableName = 'demo_table'
row = 'mytoll'
colName = "info:words"

if __name__ == '__main__':
#   os.system('kinit -kt /etc/security/keytabs/xfyan.keytab xfyan/bgs-5p242-yanxufei@BFD.COM')

    socket = TSocket.TSocket(thriftServer,thriftPort)
    transport = TTransport.TSaslClientTransport(socket, thriftServer,saslServiceName)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    client = Hbase.Client(protocol)
    transport.open()
    print "Row=>%s" % (client.getRow(tableName, row, {}))

    transport.close()

