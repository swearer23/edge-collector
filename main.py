from pymodbus.client.tcp import ModbusTcpClient
from datetime import datetime

# 连接到 Modbus TCP 设备

SERVER_IP = '192.168.2.140'
SERVER_PORT = 502

client = ModbusTcpClient(SERVER_IP, port=SERVER_PORT, timeout=3, unit=1)

try:
    # 连接到 Modbus TCP 服务器
    client.connect()
    start = datetime.now()
    print('连接成功')
    # 在这里执行多个读写操作
    result = client.read_holding_registers(address=0, count=4, slave=0x01)
    # result = client.read_holding_registers(40001, 4)
    print(result.registers)

    # 更多操作...

finally:
    # 显式关闭连接
    client.close()

print('耗时', datetime.now() - start)