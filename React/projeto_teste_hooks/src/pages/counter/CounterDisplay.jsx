import React from 'react'
import { GlobalContext } from '../../context/index'


export const CounterDisplay = () => {
  const { counterState: { counter } } = React.useContext(GlobalContext);
  return <h1>Contador: { counter }</h1>
}