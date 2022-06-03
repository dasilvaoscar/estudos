import React from 'react'
import { GlobalContext } from '../../context/index'


export const Counter = () => {
  const { counterState: { counter } } = React.useContext(GlobalContext);
  return <h1>Contador: { counter }</h1>
}