import React from 'react';
import { GlobalContext } from '../context/index'
import { Counter } from './counter/Counter'
import { CounterIncrement } from './counter/CounterIncrement';

let message;

export const Home = () => {
  const { counterState: { counter } } = React.useContext(GlobalContext)

  React.useEffect(() => {
    message = 'Sempre executa quando o componente é atualizado';
    console.log(message)
  });

  React.useEffect(() => {
    message = 'Sempre que o componente for montado, o useEffect será executado';
    console.log(message)
  }, []);

  React.useEffect(() => {
    message = 'Sempre que a variável count for alterada, o useEffect será executado novamente';
    console.log(message + ' ' + counter);
  }, [counter]);

  return (
    <div className="App" style={{ textAlign: 'center' }}>
      <Counter />
      <CounterIncrement />
    </div>
  );
}