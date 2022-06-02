import React from 'react'

export const GlobalContext = React.createContext();

export const AppContext = ({ children }) => {
  const [counter, setCounter] = React.useState(0);
  const counterState = { counter, setCounter }
  const state = { counterState }
  return <GlobalContext.Provider  value={ state }>{ children }</GlobalContext.Provider>
}