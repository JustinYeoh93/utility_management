from graphene import Mutation, ObjectType, String, Boolean, Field
from graphql_repo.schema import Person


class CreatePerson(Mutation):
    class Arguments:
        name = String()

    ok = Boolean()
    person = Field(Person)

    def mutate(self, info, name):
        person = Person(name=name)
        ok = True
        return CreatePerson(person=person, ok=ok)


class Mutation(ObjectType):
    create_person = CreatePerson.Field()
