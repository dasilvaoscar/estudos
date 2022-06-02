import * as React from 'react';

let message;

function App() {
  const [count, setCount] = React.useState(0);

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
    console.log(message + ' ' + count);
  }, [count]);

  return (
    <div className="App" style={{ textAlign: 'center' }}>
      <h1>Contador: {count}</h1>
      <button type='button' onClick={() => setCount(count + 1)}>
        +  
      </button>
    </div>
  );
}

export default App;
