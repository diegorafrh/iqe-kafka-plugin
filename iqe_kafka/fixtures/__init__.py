import pytest
from kafka import SimpleClient

from iqe_kafka.tests import MQ

@pytest.fixture
def test_topic():
    SimpleClient(MQ.API.KAFKA).ensure_topic_exists('test-topic')