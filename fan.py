import org.eclipse.paho.client.mqttv3.*;

public class FanController {
    public static void main(String[] args) throws MqttException {
        String broker = "tcp://your-render-server-url:1883";
        String clientId = "JavaClient";
        String topicSub = "sensor/data";
        String topicPub = "fan/control";

        MqttClient client = new MqttClient(broker, clientId);
        client.connect();
        client.subscribe(topicSub, (topic, message) -> {
            String payload = new String(message.getPayload());
            System.out.println("Received: " + payload);

            if (payload.contains("\"temperature\":")) {
                double temp = Double.parseDouble(payload.split(":")[1].split(",")[0]);
                if (temp > 30) {
                    client.publish(topicPub, new MqttMessage("ON".getBytes()));
                } else {
                    client.publish(topicPub, new MqttMessage("OFF".getBytes()));
                }
            }
        });
    }
}
