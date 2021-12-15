# Install docker, docker service start and docker compose
# https://gist.github.com/npearce/6f3c7826c7499587f00957fee62f8ee9
sudo service docker start

# Install virtualenv
# https://gist.github.com/CoffieldWeb/dfac9b6600700be8623b49f2aae23db5

# Install Kafka stuff
wget https://dlcdn.apache.org/kafka/3.0.0/kafka_2.13-3.0.0.tgz
tar -xzf kafka_2.13-3.0.0.tgz
cd kafka_2.13-3.0.0

# Install Java 8+
# https://tecadmin.net/install-java-on-amazon-linux/
sudo amazon-linux-extras install java-openjdk11


# Set aliases
alias zookeeper-server-start='~/kafka_2.13-3.0.0/bin/zookeeper-server-start.sh'
alias kafka-server-start.sh='~/kafka_2.13-3.0.0/bin/kafka-server-start.sh.sh'
alias kafka-console-consumer='~/kafka_2.13-3.0.0/bin/kafka-console-consumer.sh'
alias kafka-console-producer='~/kafka_2.13-3.0.0/bin/kafka-console-producer.sh'
alias kafka-topics='~/kafka_2.13-3.0.0/bin/kafka-topics.sh'
alias kafka-cluster='~/kafka_2.13-3.0.0/bin/kafka-cluster.sh'
alias kafka-configs='~/kafka_2.13-3.0.0/bin/kafka-configs.sh'
alias kafka-verifiable-producer='~/kafka_2.13-3.0.0/bin/kafka-verifiable-producer.sh'
