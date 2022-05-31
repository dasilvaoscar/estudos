import './styles.css'

export function Card({ title, body, image }) {
  return (
    <div className="post">
      <img src={ image } alt="" />
      <div className='post-content'>
        <h2>{ title }</h2>
        <p>{ body }</p>
      </div>
    </div>
  )
}