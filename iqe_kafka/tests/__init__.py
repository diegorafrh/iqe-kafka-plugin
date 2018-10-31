import os


class MQ:
    KAFKA_TOPICS = ["advisor", "available", "testareno", "uploadvalidation"]

    QUIET_MODE = True if os.getenv("QUIET_MODE", "true").lower() in ['1', 'true', 'yes'] else False
    TASK_DELAY = int(os.getenv("TASK_DELAY", "0"))

    class API:
        ZOOKEEPER = os.getenv("ZOOKEEPER", "localhost:32181")
        KAFKA = os.getenv("KAFKA", "localhost:29092")