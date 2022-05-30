import { useEffect, useState } from 'react';
import { Card } from '../../components/public/Cards/index';
import * as API from '../../services/posts/index';

export function Home() {
  const [posts, setPosts] = useState([]);

  const fetchPosts = async () => {
    const fetchPhotos = async () => {
      return API.getPostImages()
        .then((res) => res.json())
        .then();
    };

    const photos = await fetchPhotos();

    API.getAllPosts()
      .then((res) => res.json())
      .then(async (allPosts) => {
        setPosts(
          allPosts.map((post) => ({
            ...post,
            image: photos.find((photo) => photo.id === post.id).url,
          })),
        );
      });
  };

  useEffect(() => {
    fetchPosts();
  });

  return (
    <section className="container">
      <div className="posts">
        {posts.map((post) => (
          <Card
            id={post.id}
            title={post.title}
            body={post.body}
            image={post.image}
          />
        ))}
      </div>
    </section>
  );
}
