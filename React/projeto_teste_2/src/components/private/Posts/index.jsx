import { useEffect, useState } from 'react';
import { Card } from '../../public/Cards/index';
import * as API from '../../../services/posts/index';

export function Posts() {
  const [posts, setPosts] = useState([]);

  const fetchPhotos = async () => {
    const response = await API.getPostImages();
    return response.json();
  };

  const fetchPosts = async () => {
    const response = await API.getAllPosts();
    return response.json();
  };

  const mountPosts = async () => {
    const photos = await fetchPhotos();
    const allPosts = await fetchPosts();
    const postWithPhotos = allPosts.map((post) => ({
      ...post,
      image: photos.find((photo) => photo.id === post.id).url,
    }));
    setPosts(postWithPhotos);
  };

  useEffect(() => {
    mountPosts();
  });

  return (
    <section className="container">
      <div className="posts">
        {posts.map((post) => (
          <Card
            key={post.id}
            title={post.title}
            body={post.body}
            image={post.image}
          />
        ))}
      </div>
    </section>
  );
}
