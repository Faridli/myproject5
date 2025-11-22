# populate_db.py
import os
import django
import random
from faker import Faker

# Django settings configure
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_management.settings')
django.setup()

from tasks.models import Force, Company, ForceMember, PresentAddress, PermanentAddress

fake = Faker()

def populate_forces():
    forces = ["Army", "Navy", "Air Force", "Police", "BGB", "Ansar"]
    force_objs = []
    for name in forces:
        obj, created = Force.objects.get_or_create(name=name)
        force_objs.append(obj)
    return force_objs

def populate_companies():
    companies = ["Bn HQ", "HQ", "CPC-1", "CPC-2", "CPC-3", "CPSC", "Spl Force", "Acct Br"]
    company_objs = []
    for name in companies:
        obj, created = Company.objects.get_or_create(name=name)
        company_objs.append(obj)
    return company_objs

def populate_members(force_objs, company_objs, count=50):
    RANK_CHOICES = ['OFFICER', 'DAD', 'SI', 'ASI', 'NAYEK', 'CONSTABLE']

    for _ in range(count):
        force = random.choice(force_objs)
        company = random.choice(company_objs)
        rank = random.choice(RANK_CHOICES)

        member = ForceMember.objects.create(
            no=fake.unique.random_int(min=1000, max=9999),
            name=fake.name(),
            rank=rank,
            force=force,
            company=company,
            Svc_join_date=fake.date_between(start_date='-10y', end_date='-5y'),
            joining_date=fake.date_between(start_date='-5y', end_date='today'),
            birth_day=fake.date_of_birth(minimum_age=20, maximum_age=50),
            nid=fake.unique.random_number(digits=10, fix_len=True),
            email=fake.unique.email(),
            phone=fake.phone_number(),
            wf_phone=fake.phone_number(),
        )

        PresentAddress.objects.create(
            member=member,
            village=fake.street_name(),
            thana=fake.city_prefix(),
            district=fake.city(),
            division=fake.state(),
        )

        PermanentAddress.objects.create(
            member=member,
            village=fake.street_name(),
            thana=fake.city_prefix(),
            district=fake.city(),
            division=fake.state(),
        )

    print("✅ Fake data populated successfully!")

if __name__ == "__main__":
    forces = populate_forces()
    companies = populate_companies()
    populate_members(forces, companies)
