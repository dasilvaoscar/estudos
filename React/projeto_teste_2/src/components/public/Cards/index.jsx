import './styles.css'

export function Card({ id, title, body, image }) {
  return (
    <div key={ id } className="post">
      <img src={ image } alt="" />
      <div className='post-content'>
        <h1>{ title }</h1>
        <p>{ body }</p>
      </div>
    </div>
  )
}