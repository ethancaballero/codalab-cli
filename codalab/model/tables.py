from sqlalchemy import (
  Column,
  ForeignKey,
  MetaData,
  Table,
)
from sqlalchemy.types import (
  Boolean,
  Integer,
  String,
  Text,
)

# TODO(skishore): Add various indices once we know how we're querying the db.
# TODO(skishore): Write these in a MySQL-compatible form.
db_metadata = MetaData()

bundle = Table(
  'bundle',
  db_metadata,
  Column('id', Integer, primary_key=True, nullable=False),
  Column('bundle_type', String(63), nullable=False),
  # The data_hash will be NULL if the bundle's value is still being computed.
  Column('data_hash', String(63), nullable=True),
  Column('state', String(63), nullable=False),
  Column('is_current', Boolean, nullable=False),
  sqlite_autoincrement=True,
)

bundle_metadata = Table(
  'bundle_metadata',
  db_metadata,
  Column('id', Integer, primary_key=True, nullable=False),
  Column('bundle_id', Integer, ForeignKey(bundle.c.id), nullable=False),
  Column('metadata_key', String(63), nullable=False),
  Column('metadata_value', String(63), nullable=False),
  sqlite_autoincrement=True,
)

dependency = Table(
  'dependency',
  db_metadata,
  Column('id', Integer, primary_key=True, nullable=False),
  Column('dependency_type', String(63), nullable=False),
  Column('child_bundle_id', Integer, ForeignKey(bundle.c.id), nullable=False),
  Column('parent_bundle_id', Integer, ForeignKey(bundle.c.id), nullable=False),
  Column('parent_subpath', Text, nullable=False),
  sqlite_autoincrement=True,
)