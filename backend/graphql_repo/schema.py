from graphene import ObjectType, String, Field


class Person(ObjectType):
    name = String()

    def resolve_name(self, info):
        return f"This is {self.name} the query."


class Query(ObjectType):
    get_person = Field(Person, name=String())

    def resolve_get_person(self, info, name):
        # Person object/ class that has the same properties
        return Person(name=name)
