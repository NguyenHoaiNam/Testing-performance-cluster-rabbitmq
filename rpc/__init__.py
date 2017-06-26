import oslo_messaging as om

import configures

CONF = configures.CONF
TRANSPORT = None


def init():
    global TRANSPORT
    TRANSPORT = om.get_transport(CONF)


def get_target():
    return om.Target(topic=CONF.queue.topic,
                     namespace=CONF.queue.namespace,
                     version=CONF.queue.version,
                     server=CONF.queue.server_name)


def get_client(target=None, version_cap=None, serializer=None):
    if not CONF.queue.enable:
        return None
    if TRANSPORT is None:
        init()
    queue_target = target or get_target()
    return om.RPCClient(TRANSPORT, target=queue_target,
                        version_cap=version_cap, serializer=serializer)
