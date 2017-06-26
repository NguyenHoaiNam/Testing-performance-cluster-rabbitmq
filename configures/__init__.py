from oslo_config import cfg

queue_opt_group = cfg.OptGroup(name='queue',
                               title='Queue Application Options')

queue_opts = [
    cfg.BoolOpt('enable', default=True,
                help='True enables queuing, False invokes '
                     'workers synchronously'),
    cfg.StrOpt('namespace', default='test_rabbit', help='Queue namespace'),
    cfg.StrOpt('topic', default='testing.workers',
               help='Queue topic name'),
    cfg.StrOpt('version', default='1.1',
               help='Version of tasks invoked via queue'),
    cfg.StrOpt('server_name', default='testing.queue',
               help='Server name for RPC task processing server'),
    cfg.IntOpt('asynchronous_workers', default=1,
               help='Number of asynchronous worker processes'),
]


def new_config():
    conf = cfg.ConfigOpts()
    conf.register_group(queue_opt_group)
    conf.register_opts(queue_opts)
    return conf

CONF = new_config()
CONF(default_config_files=['rabbit.conf'])
