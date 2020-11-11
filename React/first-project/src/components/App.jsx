import React, { Component } from "react";
import axios from 'axios';
import ListaDeNotas from "./ListaDeNotas/ListaDeNotas";
import FormularioCadastro from "./FormularioCadastro/FormularioCadastro";
import "../assets/App.css";
import '../assets/index.css';

class App extends Component {
  
  constructor(){
    super()
    this.notas = []
  }

  componentDidMount() {
    axios.get(`http://127.0.0.1:5000/buscarNota`)
      .then(res => {
        for (let i = 0; i !== res.data.length; i++){
          this.notas.push(res.data[i])
        }
        this.setState({
          notas: this.notas
        })
      })
  }

  criarNota(titulo, texto) {
    const novaNota = {titulo, texto};

    const config = {
      headers: {'Access-Control-Allow-Origin': '*'}
    };
    axios.post('http://127.0.0.1:5000/criarNota', novaNota, config)
      .then(res => {
        this.notas.push(res.data)
        console.log(res.data)
        this.setState({
          notas: this.notas
        })
      })
      .catch(error => {
        console.log(error)
      });
  }
  render() {
    return (
      <section className="conteudo">
        <FormularioCadastro criarNota={this.criarNota.bind(this)} />
        <ListaDeNotas notas={this.notas} />
      </section>
    );
  }
}

export default App;
