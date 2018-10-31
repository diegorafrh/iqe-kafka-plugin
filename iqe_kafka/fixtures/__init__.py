import pytest
from kafka import SimpleClient


@pytest.fixture
def test_topic():
    SimpleClient(MQ.API.KAFKA).ensure_topic_exists('test-topic')