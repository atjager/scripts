import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS


bucket = ""
org = ""
token = ""
url=""

client = influxdb_client.InfluxDBClient(
    url=url,
    token=token,
    org=org
)

#--------------------Insert
# write_api = client.write_api(write_options=SYNCHRONOUS)

# p = influxdb_client.Point("my_measurement").tag("location", "Prague").field("temperature", 40.2)
# write_api.write(bucket=bucket, org=org, record=p)


#---------------------Query
query_api = client.query_api()
query = 'from(bucket: "bucketname")\
  |> range(start: -1d)\
  |> filter(fn: (r) => r._measurement == "measname")\
  |> aggregateWindow(every: 1m, fn: mean, createEmpty: false)\
  |> yield(name: "mean")'
result = query_api.query(org=org, query=query)
results = []
for table in result:
    for record in table.records:
        results.append((record.get_field(), record.get_value()))
        
print(results)