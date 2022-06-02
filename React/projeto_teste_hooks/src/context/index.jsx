import React from 'react'

export const Context = React.createContext();

export const AppContext = ({ children }) => {
  const [counter, setCounter] = React.useState(0);
  const counterState = { counter, setCounter }
  const state = { counterState }
  return <Context.Provider  value={ state }>{ children }</Context.Provider>
}