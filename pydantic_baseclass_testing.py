from pydantic import BaseModel, Field

class User(BaseModel):
    name: str
    age: int

alice_user = User(name="Alice", age=30)
print(alice_user.name)

bob_user = User(name="Bob", age="not a numbaaaaaa")
# This will raise a validation error because age is not an integer
print(bob_user.age)