import { useState } from "react"
import { IFormEvent } from "../../interfaces/events/form"

export const TestForm = () => {
  const [name, setName] = useState<string>()

  function submit(event: IFormEvent) {
    event.preventDefault()
    alert("name: " + name)
  }

  return (
    <form onSubmit={submit}>
      <label>
        Name:
        <input
          type="text"
          value={name}
          onChange={(e) => setName(e.target.value)}
        />
      </label>
      <button>Submit</button>
    </form>
  )
}