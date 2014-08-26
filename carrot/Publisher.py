from carrot.connection import BrokerConnection
from carrot.messaging import Publisher

conn = BrokerConnection(hostname="localhost", port=61617,
                          userid="admin", password="manager",
                          virtual_host="/")

publisher = Publisher(connection=conn,
                    exchange="feed", routing_key="importer")

for i in range(30):
   publisher.send({"name":"foo", "i":i})
publisher.close()

