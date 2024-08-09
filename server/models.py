from sqlalchemy_serializer import SerializerMixin
from config import db

associations = db.Table('association_table',
                        db.Column('keyword_id', db.Integer, db.ForeignKey('keyword_table.id'), primary_key=True),
                        db.Column('company_id', db.Integer, db.ForeignKey('company_table.id'), primary_key=True)
                        )


class Type(db.Model, SerializerMixin):
    
    __tablename__ = 'type_table'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String, nullable=False)

    keywords = db.relationship('Keyword', back_populates='type')

    serialize_rules = ('-keywords.type',)


class Keyword(db.Model, SerializerMixin):
    
    __tablename__ = 'keyword_table'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String, nullable=False)
    type_id = db.Column(db.Integer, db.ForeignKey('type_table.id'))
    companies_id = db.Column(db.Integer, db.ForeignKey('company_table.id'))

    type = db.relationship('Type', back_populates='keywords')
    companies = db.relationship('Company', secondary=associations, back_populates='keywords')

    serialize_rules = ('-type.keywords', '-companies.keywords')


class Company(db.Model, SerializerMixin):
    
    __tablename__ = 'company_table'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String, nullable=False)
    ticker = db.Column(db.String, nullable=False)
    country_id = db.Column(db.Integer, db.ForeignKey('country_table.id'),nullable=True)
    # keywords_id = db.Column(db.Integer, db.ForeignKey('keyword_table.id'))

    country = db.relationship('Country', back_populates='companies')
    keywords = db.relationship('Keyword', back_populates='companies')

    serialize_rules = ('-keywords.companies', '-country.companies')


class Country(db.Model, SerializerMixin):
    
    __tablename__ = 'country_table'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String, nullable=False)
    abrv = db.Column(db.String, nullable=False)

    companies = db.relationship('Company', back_populates='country')

    serialize_rules = ('-companies.country',)