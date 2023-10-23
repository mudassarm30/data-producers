# data-producers


Starting ZooKeeper and Kafka

bin/zookeeper-server-start.sh config/zookeeper.properties
bin/kafka-server-start.sh config/server.properties

Creating and Listing Topic(s)

bin/kafka-topics.sh --create --topic HandsOnTopic --bootstrap-server localhost:9092
bin/kafka-topics.sh --list --bootstrap-server localhost:9092

Producing and Consuming message to/from a topic

bin/kafka-console-producer.sh --topic HandsOnTopic --bootstrap-server localhost:9092
bin/kafka-console-consumer.sh --topic HandsOnTopic --bootstrap-server localhost:9092

Troubleshooting

List what is running on 2181 and 9092

sudo lsof -i :2181
sudo lsof -i :9092

Killing the processes that hold the above ports

sudo kill <procId>
