import attr
import importscan

from . import fixtures
from iqe.base.application.plugins import ApplicationPlugin, ApplicationPluginException


class ApplicationkafkaException(ApplicationPluginException):
    """Basic Exception for kafka object"""

    pass


@attr.s
class Applicationkafka(ApplicationPlugin):
    """Holder for application kafka related methods and functions"""

    plugin_real_name = "kafka"
    plugin_name = "kafka"
    plugin_title = "kafka"
    plugin_package_name = "iqe-kafka-plugin"


importscan.scan(fixtures)
