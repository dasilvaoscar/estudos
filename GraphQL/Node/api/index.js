import { ApolloServer, gql } from 'apollo-server';

const users =[{
    name: "Oscar",
  }, {
    name: "Dinora"
  }
]

const typeDefs = gql `

type User {
  name: String,
}`

const server = new ApolloServer({ typeDefs, resolvers })
