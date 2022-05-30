export const addPostOnStorage = (newPostList) => localStorage.setItem('posts', `${newPostList}`)

export const getAllPostOnStorate = () => localStorage.getItem('posts')