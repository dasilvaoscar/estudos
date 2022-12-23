import { JsonExpress } from "./infrastructure/proxies/JsonExpress";
import { routes } from "./infrastructure/web";

const web = JsonExpress.create(routes)

web.run()