import { CounterReducer } from './reducers'
import { CounterState } from './state'
import { CounterActions } from './actions'
import React from 'react'

export const CounterContext = () => {
  const [state, dispatcher] = React.useReducer(CounterReducer, CounterState)
  const actions = CounterActions(dispatcher)
  return [state, actions]
}