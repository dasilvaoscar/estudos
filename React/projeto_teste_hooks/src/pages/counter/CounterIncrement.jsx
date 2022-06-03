import React from 'react'
import { GlobalContext } from '../../context/index'


export const CounterIncrement = () => {
  const { increment } = React.useContext(GlobalContext);

  return (
    <button type='button' onClick={() => increment()}>
      +  
    </button>
  )
}