from config import app, db
from models import Keyword, Type
from faker import Faker
from datetime import datetime

faker = Faker()

if __name__ == '__main__':
    with app.app_context():
        # print("Creating tables...")
        # db.create_all()
        # print("Tables created!")
        
        
        print("Seeding database...")
        Keyword.query.delete()
        Type.query.delete()
        
        print("Generating keywords...")
        t1 = Type(title="Medical")
        t2 = Type(title="Country")
        db.session.add_all([t1,t2])
        db.session.commit()
        
        print("Generating types...")
        k1 = Keyword(title="Weight Loss", type_id=t1.id)
        k2 = Keyword(title="USA", type_id=t2.id)
        k3 = Keyword(title="China", type_id=t2.id)
        db.session.add_all([k1,k2,k3])
        db.session.commit()

        print("Seeding complete!")