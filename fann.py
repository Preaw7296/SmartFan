from flask import Flask, jsonify
import socket
import struct

app = Flask(__name__)

# การตั้งค่า MQTT
broker = "your-render-server-url"
port = 1883
topic_sub = "sensor/data"
topic_pub = "fan/control"

client_id = "FlaskClient"

# ฟังก์ชันเชื่อมต่อไปยัง MQTT Broker
def connect_to_broker():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((broker, port))
    return sock

# ฟังก์ชันสำหรับสร้าง MQTT packet
def create_mqtt_packet(topic, message):
    # Fixed header: 0x30 = CONNECT packet type
    header = b'\x30'  # MQTT CONNECT packet type
    length = len(topic) + len(message) + 4  # คำนวณความยาว
    packet = struct.pack('!B', header) + struct.pack('!H', length)  # MQTT packet header
    packet += struct.pack('!H', len(topic)) + topic.encode('utf-8')  # Topic length and name
    packet += struct.pack('!H', len(message)) + message.encode('utf-8')  # Message length and content
    return packet

# ฟังก์ชัน Publish ข้อความ
def publish(sock, message):
    publish_packet = create_mqtt_packet(topic_pub, message)
    sock.sendall(publish_packet)
    print(f"Published: {message}")

@app.route('/')
def index():
    return "Flask app is running and connected to MQTT!"

@app.route('/start_fan')
def start_fan():
    sock = connect_to_broker()
    publish(sock, "ON")
    sock.close()
    return jsonify({"status": "Fan ON"})

@app.route('/stop_fan')
def stop_fan():
    sock = connect_to_broker()
    publish(sock, "OFF")
    sock.close()
    return jsonify({"status": "Fan OFF"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
