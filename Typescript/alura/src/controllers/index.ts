import { Path, GET } from "typescript-rest";
import Negociacao from "../models/Negociacao"

@Path("/")
class HelloService {
  
  @GET
  home(): Negociacao {
    const negociacao = new Negociacao(new Date)
    return negociacao;
  }

}

export default HelloService