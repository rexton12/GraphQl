from ariadne import ObjectType, QueryType, gql, make_executable_schema
from ariadne.asgi import GraphQL

type_defs = gql("""
    type Query {
        user: [user!]!
    }

    type user {
        firstName: String
        lastName: String!
        age: Int!
        fullName: String!
    }
""")

# Map resolver functions to Query fields using QueryType
query = QueryType()

# Resolvers are simple python functions
@query.field("user")
def resolve_user(*_):
    return [
       {"firstName": "Rexton", "lastName": "itsiah", "age": 21},
      #{"firstName": "Bob", "lastName": "Boberson", "age": 24},
    ]


# Map resolver functions to custom type fields using ObjectType
user = ObjectType("user")

@user.field("fullName")
def resolve_person_fullname(user, *_):
    return "%s %s" % (user["firstName"], user["lastName"])

# Create executable GraphQL schema
schema = make_executable_schema(type_defs, query, user)

# Create an ASGI app using the schema, running in debug mode
app = GraphQL(schema, debug=True)