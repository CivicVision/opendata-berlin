from sqlalchemy.orm import relation
from sqlalchemy import types, Column, Table, ForeignKey, and_, UniqueConstraint
import datetime

from .meta_helper import metadata
from .types import make_uuid, JsonDictType

PACKAGE_NAME_MAX_LENGTH = 100
PACKAGE_NAME_MIN_LENGTH = 2
PACKAGE_VERSION_MAX_LENGTH = 100

MAX_TAG_LENGTH = 100
MIN_TAG_LENGTH = 2

VOCABULARY_NAME_MIN_LENGTH = 2
VOCABULARY_NAME_MAX_LENGTH = 100

package_table = Table('package', metadata,
        Column('id', types.UnicodeText, primary_key=True, default=make_uuid),
        Column('name', types.Unicode(PACKAGE_NAME_MAX_LENGTH),
               nullable=False, unique=True),
        Column('title', types.UnicodeText),
        Column('version', types.Unicode(PACKAGE_VERSION_MAX_LENGTH)),
        Column('url', types.UnicodeText),
        Column('author', types.UnicodeText),
        Column('author_email', types.UnicodeText),
        Column('maintainer', types.UnicodeText),
        Column('maintainer_email', types.UnicodeText),
        Column('notes', types.UnicodeText),
        Column('license_id', types.UnicodeText),
        Column('type', types.UnicodeText, default=u'dataset'),
        Column('owner_org', types.UnicodeText),
        Column('creator_user_id', types.UnicodeText),
        Column('metadata_created', types.DateTime, default=datetime.datetime.utcnow),
        Column('metadata_modified', types.DateTime, default=datetime.datetime.utcnow),
        Column('private', types.Boolean, default=False),
        Column('berlin_type', types.UnicodeText),
        Column('geographical_granularity', types.UnicodeText),
        Column('temporal_granularity', types.UnicodeText),
        Column('license_title', types.UnicodeText),
        Column('geographical_coverage', types.UnicodeText),
        Column('berlin_source', types.UnicodeText),
        Column('state', types.UnicodeText),
        Column('date_released', types.DateTime, default=datetime.datetime.utcnow),
        Column('date_updated', types.DateTime, default=datetime.datetime.utcnow),
        Column('username', types.UnicodeText),
        Column('attribution_text', types.UnicodeText),
        Column('temporal_coverage_from', types.UnicodeText),
        Column('temporal_coverage_to', types.UnicodeText),
)

resource_table = Table(
    'resource', metadata,
    Column('id', types.UnicodeText, primary_key=True,
           default=make_uuid),
    Column('package_id', types.UnicodeText,
           ForeignKey('package.id')),
    Column('url', types.UnicodeText, nullable=False),
    Column('format', types.UnicodeText),
    Column('description', types.UnicodeText),
    Column('hash', types.UnicodeText),
    Column('position', types.Integer),
    Column('name', types.UnicodeText),
    Column('resource_type', types.UnicodeText),
    Column('mimetype', types.UnicodeText),
    Column('mimetype_inner', types.UnicodeText),
    Column('size', types.BigInteger),
    Column('created', types.DateTime, default=datetime.datetime.utcnow),
    Column('last_modified', types.DateTime),
    Column('cache_url', types.UnicodeText),
    Column('cache_last_updated', types.DateTime),
    Column('url_type', types.UnicodeText),
    Column('Abteilung', types.UnicodeText),
    Column('Landesstelle', types.UnicodeText),
    Column('extras', JsonDictType),
)

tag_table = Table('tag', metadata,
    Column('id', types.UnicodeText, primary_key=True, default=make_uuid),
    Column('name', types.Unicode(MAX_TAG_LENGTH), nullable=False),
    Column('vocabulary_id',
        types.Unicode(VOCABULARY_NAME_MAX_LENGTH))
)

package_tag_table = Table('package_tag', metadata,
    Column('id', types.UnicodeText, primary_key=True, default=make_uuid),
    Column('package_id', types.UnicodeText, ForeignKey('package.id')),
    Column('tag_id', types.UnicodeText, ForeignKey('tag.id')),
    )

package_group_table = Table('package_group', metadata,
    Column('id', types.UnicodeText, primary_key=True, default=make_uuid),
    Column('package_id', types.UnicodeText, ForeignKey('package.id')),
    Column('group_id', types.UnicodeText, ForeignKey('group.id')),
    )

group_table = Table('group', metadata,
    Column('id', types.UnicodeText, primary_key=True, default=make_uuid),
    Column('name', types.UnicodeText, nullable=False, unique=True),
    Column('title', types.UnicodeText),
    Column('display_name', types.UnicodeText),
    Column('type', types.UnicodeText),
    Column('description', types.UnicodeText),
    Column('image_url', types.UnicodeText),
    Column('created', types.DateTime, default=datetime.datetime.now),
    Column('is_organization', types.Boolean, default=False),
    Column('approval_status', types.UnicodeText, default=u"approved")
    )
