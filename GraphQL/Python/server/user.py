import graphene

class Permission(graphene.ObjectType):
    name=graphene.String()
    description=graphene.String()
 
class User(graphene.ObjectType):
  name=graphene.String()
  permission=graphene.List(Permission)
 
  def resolve_name(self):
    return 'Oscar'
 
schema = graphene.Schema(query=User)
