import { Path, GET } from "typescript-rest";

@Path("/")
class HelloService {
  
  @GET
  sayHello(): string {
    return "Hello";
  }
}

export default HelloService