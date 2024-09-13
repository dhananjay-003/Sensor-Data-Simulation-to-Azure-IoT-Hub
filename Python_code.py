import time
import random
from azure.iot.device import IoTHubDeviceClient, Message
from azure.cosmosdb.table.tableservice import TableService
from azure.cosmosdb.table.models import Entity

YOUR_IOT_HUB_NAME = "#You will get this key in azure IoT hub"
YOUR_DEVICE_ID = "#You will get this key in azure IoT hub"
YOUR_SHARED_ACCESS_KEY = "#You will get this key in azure IoT hub"

CONNECTION_STRING = f"HostName={YOUR_IOT_HUB_NAME}.azure-devices.net;DeviceId={YOUR_DEVICE_ID};SharedAccessKey={YOUR_SHARED_ACCESS_KEY}"

STORAGE_ACCOUNT_NAME = "#Name the storage account"
STORAGE_ACCOUNT_KEY = "#You will get this key if you create an database in azure"
TABLE_NAME = "#You will get this key if you create an database in azure"

# Initialize table_service at the top level
table_service = TableService(account_name=STORAGE_ACCOUNT_NAME, account_key=STORAGE_ACCOUNT_KEY)

def iothub_client_init():
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
    return client

def send_telemetry_data(client, temperature, humidity, pressure):
    payload = '{{"temperature": {}, "humidity": {}, "pressure": {}}}'.format(temperature, humidity, pressure)
    message = Message(payload)
    client.send_message(message)
    print("Message sent: {}".format(payload))
    
    # Store data in Azure Storage Table
    store_data_in_storage_table(temperature, humidity, pressure)

def store_data_in_storage_table(temperature, humidity, pressure):
    # Check if the table exists, and create it if it doesn't
    if not table_service.exists(TABLE_NAME):
             table_service.create_table(TABLE_NAME)

    # Create an entity (row) with sensor data
    entity = Entity()
    entity.PartitionKey = YOUR_DEVICE_ID
    entity.RowKey = str(int(time.time()))
    entity.temperature = temperature
    entity.humidity = humidity
    entity.pressure = pressure

    # Insert the entity into the table
    table_service.insert_entity(TABLE_NAME, entity)

client = iothub_client_init()

while True:
    temperature_c = random.uniform(20.0, 30.0)
    humidity_percent = random.uniform(40.0, 60.0)
    pressure_kpa = random.uniform(100.0, 110.0)

    print('Simulated Temperature: {} °C, Humidity: {} %, Pressure: {} kPa'.format(temperature_c, humidity_percent, pressure_kpa))

    send_telemetry_data(client, temperature_c, humidity_percent, pressure_kpa)

    # Query and print entities from the table after sending data
    try:
        entities = table_service.query_entities(TABLE_NAME)
        for entity in entities:
            print(entity)
    except Exception as e:
        print(f"Error: {e}")

    time.sleep(5)
