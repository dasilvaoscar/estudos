const getDate = ():string => { 
  return new Date().toISOString().substring(0, 10).split('-').reverse().join().replace(/,/g, '/')
}

export { getDate }