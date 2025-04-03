import socket
import struct
import time

broker = "your-render-server-url"
port = 1883
topic_sub = "sensor/data"
topic_pub = "fan/control"
client_id = "PythonClient"

# ฟังก์ชันสร้าง header สำหรับ MQTT Packet
def create_mqtt_packet(topic, message):
    # Fixed header: 0x30 = CONNECT packet type
    header = b'\x30'  # MQTT CONNECT packet type
    length = len(topic) + len(message) + 4  # คำนวณความยาว
    packet = struct.pack('!B', header) + struct.pack('!H', length)  # MQTT packet header
    packet += struct.pack('!H', len(topic)) + topic.encode('utf-8')  # Topic length and name
    packet += struct.pack('!H', len(message)) + message.encode('utf-8')  # Message length and content
    return packet

# เชื่อมต่อไปที่ broker
def connect_to_broker():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((broker, port))
    return sock

# ฟังก์ชัน Subscribe
def subscribe(sock):
    subscribe_packet = create_mqtt_packet(topic_sub, "Request")
    sock.sendall(subscribe_packet)
    print(f"Subscribed to {topic_sub}")

# ฟังก์ชัน Publish
def publish(sock, message):
    publish_packet = create_mqtt_packet(topic_pub, message)
    sock.sendall(publish_packet)
    print(f"Published: {message}")

# ฟังก์ชันอ่านข้อมูลจาก MQTT
def listen_for_messages(sock):
    while True:
        data = sock.recv(1024)
        if data:
            message = data.decode("utf-8")
            print(f"Received: {message}")

            # ตรวจสอบว่า payload มีข้อมูลอุณหภูมิหรือไม่
            if "\"temperature\":" in message:
                try:
                    temp = float(message.split(":")[1].split(",")[0])
                    if temp > 30:
                        publish(sock, "ON")
                    else:
                        publish(sock, "OFF")
                except ValueError:
                    print("Error parsing temperature")
        time.sleep(1)

# หลักการทำงาน
sock = connect_to_broker()
subscribe(sock)
listen_for_messages(sock)
