from pymodbus.client.tcp import ModbusTcpClient

# 连接到 Modbus TCP 设备

SERVER_IP = '192.168.1.10'
SERVER_PORT = 502

client = ModbusTcpClient(SERVER_IP, port=SERVER_PORT)

try:
    # 连接到 Modbus TCP 服务器
    client.connect()

    # 在这里执行多个读写操作
    result = client.read_holding_registers(0, 4, unit=1)
    print(result.registers)

    # 更多操作...

finally:
    # 显式关闭连接
    client.close()
