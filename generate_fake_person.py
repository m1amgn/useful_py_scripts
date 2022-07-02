# Python Faker
# pip install Faker

from faker import Faker

dumy = Faker()

# Get Profile
print(dumy.profile())

# Get random sentence
print(dumy.sentence())

# Get a random name
print(dumy.name())

# Get a random address
print(dumy.address())

# Get a random phone number
print(dumy.phone_number())

# Get a random email address
print(dumy.email())

# Get a random company name
print(dumy.company())

# Get a random city
print(dumy.city())

# Get a random state
print(dumy.state())

# Get a random zip code
print(dumy.zipcode())
