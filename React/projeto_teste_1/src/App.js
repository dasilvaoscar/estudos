import { useState } from 'react'
import { Card } from './components/Cards/index.component'
import * as storage from './helpers/storage/posts'
import * as generators from './helpers/generators/id'

const getAllPosts = () => {
  const defaultPostsList = [
    'Hello World',
    'Goodbye World',
    'Hello World Again'
  ]

  const posts = storage.getAllPostOnStorate()

  if (!posts) {
    storage.addPostOnStorage(defaultPostsList)
    return defaultPostsList
  }
  
  return posts.split(',')
}

export const App = () => {

  const [ posts, setPosts ] = useState(getAllPosts());
  const [ currentPost, setCurrentPost ] = useState()

  function addPostOnList() {
    const newPostList = [...posts, currentPost]
    storage.addPostOnStorage(newPostList)
    setPosts(newPostList)
  }

  function changeCurrentPost({ target }) {
    setCurrentPost(target.value)
  }

  function renderPost(post) {
    return <Card id={ generators.generateID() } text={ post } />
  }

  function renderAllPosts() {
    return posts.map(renderPost)
  }

  return (
    <> 
      <input type="text" onChange={ changeCurrentPost } />
      <button onClick={ addPostOnList }>Change Posts</button>
      <ul class="tilesWrap">
        { renderAllPosts() }
      </ul>
    </>
  );
}
