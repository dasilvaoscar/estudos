import { useEffect, useState, useCallback } from 'react';
import { DefaultCard as Card } from '../../public/Cards/Default/index';
import { DefaultInput as Input } from '../../../components/public/inputs/Default/index'
import * as API from '../../../services/posts/index';

export function Posts() {
  const [posts, setPosts] = useState([]);
  const [allPosts, setAllPosts] = useState([]);

  const fetchPhotos = async () => {
    const response = await API.getPostImages();
    return response.json();
  };

  const fetchPosts = async () => {
    const response = await API.getAllPosts();
    return response.json();
  };

  const mountAllPosts = useCallback(async () => {
    const [ photos, allPosts ] = await Promise.all([fetchPhotos(), fetchPosts()]);

    const postWithPhotos = allPosts.map(post => ({
      ...post,
      image: photos.find(photo => photo.id === post.id).url,
    }));

    [setPosts, setAllPosts].map(setter => setter(postWithPhotos));
  }, []);

  const filterPosts = ({ target: { value: title }}) => {
    const filteredPosts = allPosts.filter(post => post.title.toUpperCase().includes(title.toUpperCase()));
    setPosts(filteredPosts);
  }

  const renderPosts = () => {
    return posts.map(post => (
      <Card
        key={post.id}
        title={post.title}
        body={post.body}
        image={post.image}
      />
    ))
  }

  useEffect(() => { mountAllPosts() }, [mountAllPosts]);

  return (
    <section className="container">
      <Input onChange={filterPosts} placeholder='Pesquisa' /> <br />
      <div className="posts">
        { renderPosts() }
      </div>
    </section>
  );
}
