import paho.mqtt.client as mqtt

broker = "your-render-server-url"
client_id = "PythonClient"
topic_sub = "sensor/data"
topic_pub = "fan/control"

def on_message(client, userdata, message):
    payload = message.payload.decode("utf-8")
    print(f"Received: {payload}")

    if "\"temperature\":" in payload:
        try:
            temp = float(payload.split(":")[1].split(",")[0])
            if temp > 30:
                client.publimportish(topic_pub, "ON")
                print("Fan turned ON")
            else:
                client.publish(topic_pub, "OFF")
                print("Fan turned OFF")
        except ValueError:
            print("Error parsing temperature")

client = mqtt.Client(client_id, protocol=mqtt.MQTTv311)
client.connect(broker, 1883)
client.subscribe(topic_sub)
client.on_message = on_message

print("MQTT client started...")
client.loop_forever()
import paho.mqtt.client as mqtt

broker = "your-render-server-url"
client_id = "PythonClient"
topic_sub = "sensor/data"
topic_pub = "fan/control"

def on_message(client, userdata, message):
    payload = message.payload.decode("utf-8")
    print(f"Received: {payload}")

    if "\"temperature\":" in payload:
        try:
            temp = float(payload.split(":")[1].split(",")[0])
            if temp > 30:
                client.publish(topic_pub, "ON")
                print("Fan turned ON")
            else:
                client.publish(topic_pub, "OFF")
                print("Fan turned OFF")
        except ValueError:
            print("Error parsing temperature")

# ✅ แก้ไขตรงนี้
client = mqtt.Client(client_id, protocol=mqtt.MQTTv5)

client.on_message = on_message
client.connect(broker, 1883)
client.subscribe(topic_sub)

print("MQTT client started...")
client.loop_forever()
