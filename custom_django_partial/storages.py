# -*- coding: utf-8 -*-

from ecstatic.storage import CachedStaticFilesMixin, StaticManifestMixin
from qiniustorage.backends import QiniuMediaStorage, QiniuStaticStorage


class QiniuCachedMediaStorage(StaticManifestMixin, CachedStaticFilesMixin, QiniuMediaStorage):
    pass


class QiniuCachedStaticStorage(StaticManifestMixin, CachedStaticFilesMixin, QiniuStaticStorage):
    pass
