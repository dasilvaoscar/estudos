import React from 'react'
import { Context } from '../context/index'


export const Counter = () => {
  const { counterState: { counter } } = React.useContext(Context);
  return <h1>Contador: { counter }</h1>
}