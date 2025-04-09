@app.route('/set_threshold', methods=['GET', 'POST'])
def set_threshold():
    message = ""
    if request.method == 'POST':
        try:
            new_threshold = int(request.form['threshold'])
            sensor_data['threshold'] = new_threshold
            message = f"✅ Threshold updated to {new_threshold}"
        except ValueError:
            message = "❌ Invalid input. Please enter a number."

    # HTML Page for form and status
    html = '''
    <html>
        <head>
            <title>🌟 IoT Control Panel</title>
            <style>
                body {
                    font-family: 'Arial', sans-serif;
                    background: linear-gradient(to right, #FFB6C1, #FFD700);
                    color: #333;
                    margin: 0;
                    padding: 20px;
                }
                h2 {
                    text-align: center;
                    color: #FF6347;
                }
                table {
                    width: 100%;
                    margin: 20px auto;
                    border-collapse: collapse;
                    background-color: #FFFFFF;
                    border-radius: 8px;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                }
                th, td {
                    padding: 12px;
                    text-align: center;
                    font-size: 18px;
                }
                th {
                    background-color: #FF6347;
                    color: white;
                    border-radius: 8px 8px 0 0;
                }
                td {
                    background-color: #FFFAF0;
                    border-radius: 0 0 8px 8px;
                }
                button {
                    background-color: #FF6347;
                    color: white;
                    padding: 10px 20px;
                    border: none;
                    border-radius: 5px;
                    font-size: 16px;
                    cursor: pointer;
                    transition: background-color 0.3s ease;
                }
                button:hover {
                    background-color: #FF4500;
                }
                input[type="number"] {
                    padding: 8px;
                    font-size: 16px;
                    width: 100px;
                    margin: 10px 0;
                    border-radius: 5px;
                    border: 1px solid #ddd;
                }
                p {
                    font-size: 16px;
                    color: #228B22;
                    text-align: center;
                    font-weight: bold;
                }
            </style>
        </head>
        <body>
            <h2>🌞 IoT Sensor Dashboard</h2>
            <table>
                <tr><th>Sensor</th><th>Value</th></tr>
                <tr><td>🌡️ Temperature</td><td>{{ temperature }} °C</td></tr>
                <tr><td>🎚️ Threshold</td><td><b>{{ threshold }} %</b></td></tr>
                <tr><td>💧 Humidity</td><td>{{ humidity }} %</td></tr>
            </table>

            <h3 style="text-align:center;">🔧 Update Threshold</h3>
            <form method="POST" style="text-align: center;">
                <label for="threshold">New Threshold (%):</label><br>
                <input type="number" name="threshold" min="0" max="100" value="{{ threshold }}" required>
                <br><br>
                <button type="submit">Update</button>
            </form>

            <p>{{ message }}</p>
        </body>
    </html>
    '''
    return render_template_string(
        html,
        temperature=sensor_data["temperature"],
        humidity=sensor_data["humidity"],
        soil_moisture=sensor_data["soil_moisture"],
        threshold=sensor_data["threshold"],
        message=message
    )
