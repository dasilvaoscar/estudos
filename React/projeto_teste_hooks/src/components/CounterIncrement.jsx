import React from 'react'
import { Context } from '../context/index'


export const CounterIncrement = () => {
  const { counterState: { counter, setCounter } } = React.useContext(Context);

  return (
    <button type='button' onClick={() => setCounter(counter + 1)}>
      +  
    </button>
  )
}