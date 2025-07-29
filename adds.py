from faker import Faker
import random

fake = Faker()

malaysia_states = [
    "Selangor", "Kuala Lumpur", "Penang", "Johor", "Perak", "Sabah",
    "Sarawak", "Negeri Sembilan", "Melaka", "Pahang", "Kedah", "Kelantan", "Terengganu", "Perlis", "Putrajaya", "Labuan"
]

def generate_malaysian_address():
    building = fake.building_number()
    street = "Jalan " + fake.last_name()
    postcode = random.randint(10000, 99999)
    city = fake.city()
    state = random.choice(malaysia_states)
    return f"{building}, {street}, {postcode} {city}, {state}, Malaysia"


