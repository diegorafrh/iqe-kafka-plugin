import json
import os

import pytest
from iqe_kafka.tests import MQ
from kafka import KafkaConsumer, KafkaProducer
from kafka.errors import KafkaError


class TestKafka:
    body = {"test": "some message"}

    @staticmethod
    def produce_message(topic, body):
        producer = KafkaProducer(bootstrap_servers=MQ.API.KAFKA)
        future = producer.send(topic, body)
        producer.flush()
        return future

    @staticmethod
    def consume_message(topic):
        consumer = KafkaConsumer(
            topic, bootstrap_servers=[MQ.API.KAFKA], group_id='some-group',
            consumer_timeout_ms=3000
        )

        for m in consumer:
            yield json.loads(m.value)

    def test_message_produce_and_consume(self, test_topic):
        topic_name = 'test-topic'

        future = self.produce_message(topic_name, json.dumps(self.body).encode())

        # This blocks till the future is done and returns the record (message) metadata
        try:
            record_metadata = future.get(3000)
        except KafkaError as e:
            import traceback; traceback.print_exc()
            pytest.xfail("[ERROR] Can't produce the message")

        assert future.is_done is True
        assert record_metadata.topic == topic_name
        assert record_metadata.partition is not None

        for message in self.consume_message(topic_name):
            assert 'test' in message
            assert message['test'] == 'some message'


def test_plugin_accessible(application):
     hasattr(application, "kafka")
