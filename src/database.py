from sqlalchemy import Table, Column, String, MetaData, Integer, JSON, ForeignKey

meta = MetaData()  

Integration = Table('integration', meta,
   Column('id', String, primary_key=True),
   Column('created_date', String),
   Column('modified_date', String),
   Column('uid', String),
   Column('source', String),
   Column('provider', String),
   Column('extra_data', JSON),
   Column('user_id', String),
   Column('created_by_id', String),
   Column('modified_by_id', String)
   )

IntegrationAuth = Table('integration_auth', meta,
   Column('id', Integer, primary_key=True),
   Column('created_date', String),
   Column('modified_date', String),
   Column('name', String),
   Column('token', String),
   Column('created_by_id', String),
   Column('modified_by_id', String),
   )

OrganizationIntegration = Table('organization_integration', meta,
   Column('id', Integer, primary_key=True),
   Column('created_date', String),
   Column('modified_date', String),
   Column('school_name', String),
   Column('partner', String),
   Column('auth_id', Integer, ForeignKey('integration_auth.id')),
   Column('created_by_id', String),
   Column('modified_by_id', String),
   )

