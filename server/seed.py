#!/usr/bin/env python3

from config import app, db
from models import Keyword, Type, Country, Company
from faker import Faker
from datetime import datetime

faker = Faker()
top_50_countries_by_gdp = [
    ("United States", "USA"),
    ("China", "CHN"),
    ("Japan", "JPN"),
    ("Germany", "DEU"),
    ("India", "IND"),
    ("United Kingdom", "GBR"),
    ("France", "FRA"),
    ("Italy", "ITA"),
    ("Canada", "CAN"),
    ("South Korea", "KOR"),
    ("Russia", "RUS"),
    ("Brazil", "BRA"),
    ("Australia", "AUS"),
    ("Spain", "ESP"),
    ("Mexico", "MEX"),
    ("Indonesia", "IDN"),
    ("Netherlands", "NLD"),
    ("Saudi Arabia", "SAU"),
    ("Turkey", "TUR"),
    ("Switzerland", "CHE"),
    ("Taiwan", "TWN"),
    ("Poland", "POL"),
    ("Sweden", "SWE"),
    ("Belgium", "BEL"),
    ("Thailand", "THA"),
    ("Argentina", "ARG"),
    ("Austria", "AUT"),
    ("Norway", "NOR"),
    ("United Arab Emirates", "ARE"),
    ("Nigeria", "NGA"),
    ("South Africa", "ZAF"),
    ("Israel", "ISR"),
    ("Hong Kong", "HKG"),
    ("Ireland", "IRL"),
    ("Singapore", "SGP"),
    ("Malaysia", "MYS"),
    ("Philippines", "PHL"),
    ("Colombia", "COL"),
    ("Denmark", "DNK"),
    ("Egypt", "EGY"),
    ("Vietnam", "VNM"),
    ("Bangladesh", "BGD"),
    ("Chile", "CHL"),
    ("Finland", "FIN"),
    ("Czech Republic", "CZE"),
    ("Portugal", "PRT"),
    ("Romania", "ROU"),
    ("New Zealand", "NZL"),
    ("Greece", "GRC"),
]

if __name__ == '__main__':
    with app.app_context():
        print("Seeding database...")

        Keyword.query.delete()
        Type.query.delete()
        Country.query.delete()
        Company.query.delete()
        
        t1 = Type(title="Industry")
        db.session.add_all([t1])
        db.session.commit()
        

        # n1 = Country(name="United States of America", abrv="USA")
        new_countries = []
        for country in top_50_countries_by_gdp:
            new_country = Country(name=country[0], abrv=country[1])
            new_countries.append(new_country)
            
        db.session.add_all(new_countries)
        db.session.commit()

       

        

        c1 = Company(name="Apple Inc.", ticker="AAPL")
        db.session.add_all([c1])
        db.session.commit()

        k1 = Keyword(title="Crypto Mining", type_id=t1.id, companies_id=c1.id)
        db.session.add_all([k1])
        db.session.commit()


        print("Seeding complete!")