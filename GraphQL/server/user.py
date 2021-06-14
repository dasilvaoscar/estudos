import graphene
 
class QueryUser(graphene.ObjectType):
  name = graphene.String()
 
  def resolve_name(self, info):
    return 'Oscar'
 
schema = graphene.Schema(query=QueryUser)
