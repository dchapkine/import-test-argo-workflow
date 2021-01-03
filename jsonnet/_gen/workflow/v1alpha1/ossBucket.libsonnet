{
  local d = (import 'doc-util/main.libsonnet'),
  '#':: d.pkg(name='ossBucket', url='', help='OSSBucket contains the access information required for interfacing with an Alibaba Cloud OSS bucket'),
  '#accessKeySecret':: d.obj(help='SecretKeySelector selects a key of a Secret.'),
  accessKeySecret: {
    '#localObjectReference':: d.obj(help='LocalObjectReference contains enough information to let you locate the\nreferenced object inside the same namespace.'),
    localObjectReference: {
      '#withName':: d.fn(help='', args=[d.arg(name='name', type=d.T.string)]),
      withName(name): { accessKeySecret+: { localObjectReference+: { name: name } } },
    },
    '#withKey':: d.fn(help='The key of the secret to select from.  Must be a valid secret key.', args=[d.arg(name='key', type=d.T.string)]),
    withKey(key): { accessKeySecret+: { key: key } },
    '#withOptional':: d.fn(help='', args=[d.arg(name='optional', type=d.T.boolean)]),
    withOptional(optional): { accessKeySecret+: { optional: optional } },
  },
  '#secretKeySecret':: d.obj(help='SecretKeySelector selects a key of a Secret.'),
  secretKeySecret: {
    '#localObjectReference':: d.obj(help='LocalObjectReference contains enough information to let you locate the\nreferenced object inside the same namespace.'),
    localObjectReference: {
      '#withName':: d.fn(help='', args=[d.arg(name='name', type=d.T.string)]),
      withName(name): { secretKeySecret+: { localObjectReference+: { name: name } } },
    },
    '#withKey':: d.fn(help='The key of the secret to select from.  Must be a valid secret key.', args=[d.arg(name='key', type=d.T.string)]),
    withKey(key): { secretKeySecret+: { key: key } },
    '#withOptional':: d.fn(help='', args=[d.arg(name='optional', type=d.T.boolean)]),
    withOptional(optional): { secretKeySecret+: { optional: optional } },
  },
  '#withBucket':: d.fn(help='Bucket is the name of the bucket', args=[d.arg(name='bucket', type=d.T.string)]),
  withBucket(bucket): { bucket: bucket },
  '#withEndpoint':: d.fn(help='Endpoint is the hostname of the bucket endpoint', args=[d.arg(name='endpoint', type=d.T.string)]),
  withEndpoint(endpoint): { endpoint: endpoint },
  '#mixin': 'ignore',
  mixin: self,
}
