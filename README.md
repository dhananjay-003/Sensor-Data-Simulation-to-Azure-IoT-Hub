# Sensor-Data-Simulation-to-Azure-IoT-Hub
This project simulates sensor data (temperature, humidity, and pressure) and sends it to Azure IoT Hub for cloud-based monitoring. The data is also stored in Azure Table Storage for persistence. It's a demonstration of real-time IoT data simulation and storage using Python and Azure services.

# Project Overview
Features:

Simulates Sensor Data: Randomly generates temperature, humidity, and pressure readings.

Sends Data to Azure IoT Hub: Transmits the simulated data to Azure IoT Hub using a secure connection.

Stores Data in Azure Table Storage: After sending data to IoT Hub, the same data is stored in Azure Table Storage for persistence.

# Components:
Azure IoT Hub: Acts as the cloud gateway to collect telemetry data from simulated sensors.

Azure Table Storage: Stores sensor data for retrieval and analysis.

Python: Implements the simulation and data transmission logic.

# Prerequisites
Azure IoT Hub: Create an IoT Hub in your Azure account.

Azure Storage Account: Create a storage account for Table Storage.

Python 3.x: Ensure Python is installed on your machine.

# Install the required Python packages:

pip install azure-iot-device azure-cosmosdb-table

# Clone this repository:

git clone (https://github.com/dhananjay-003/Sensor-Data-Simulation-to-Azure-IoT-Hub/blob/main/Python_code.py)

# Set Up Environment:

Replace the placeholders in the script with your actual Azure IoT Hub and storage account credentials:

YOUR_IOT_HUB_NAME

YOUR_DEVICE_ID

YOUR_SHARED_ACCESS_KEY

STORAGE_ACCOUNT_NAME

STORAGE_ACCOUNT_KEY

TABLE_NAME

# Run the Simulation:

python simulated_temp.py

The script will simulate temperature, humidity, and pressure values and send them to your Azure IoT Hub every 5 seconds.

# Code Explanation

IoT Hub Client Initialization: The IoT Hub client is initialized using the connection string, which includes the IoT Hub name, device ID, and shared access key.

client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

Simulating Sensor Data: The script generates random values for temperature (20-30°C), humidity (40-60%), and pressure (100-110 kPa).

temperature_c = random.uniform(20.0, 30.0)

humidity_percent = random.uniform(40.0, 60.0)

pressure_kpa = random.uniform(100.0, 110.0)

# Sending Data to IoT Hub: The sensor data is formatted into a JSON message and sent to the IoT Hub.

payload = '{{"temperature": {}, "humidity": {}, "pressure": {}}}'.format(temperature, humidity, pressure)

client.send_message(message)

# Storing Data in Azure Table Storage: The same data is stored in Azure Table Storage for later analysis. Each entry is associated with a unique timestamp.

entity.RowKey = str(int(time.time()))

table_service.insert_entity(TABLE_NAME, entity)

# Future Enhancements
Add more sensor types to simulate additional telemetry data.

Implement analytics dashboards using Power BI or Azure Data Explorer.

Incorporate error handling and retries for improved robustness.
