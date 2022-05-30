const API_URL = 'https://jsonplaceholder.typicode.com'

export const getAllPosts = async () => await fetch(`${API_URL}/posts`)
export const getPostImages = async () => await fetch(`${API_URL}/photos`)