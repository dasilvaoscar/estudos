import React from 'react'
import { CounterContext } from './counter/_index'

export const GlobalContext = React.createContext();

export const AppContext = ({ children }) => {
  const [counterState, counterActions] = CounterContext()
  return <GlobalContext.Provider value={{ counterState, ...counterActions }}>{ children }</GlobalContext.Provider>
}