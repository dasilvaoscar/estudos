import axiosTest from 'npm:axios@1.6.3'
import axios from 'npm:axios'

Deno.serve((_request: Request) => {
  return new Response("Hello, world!");
});