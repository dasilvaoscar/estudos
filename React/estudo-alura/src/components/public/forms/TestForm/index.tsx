import { useState } from 'react';
import { IChangeEvent, IFormEvent } from '@/helpers/interfaces/events/index';
import { frozen } from '../../../../helpers/functions';

export const TestForm = () => {
  const [name, setName] = useState<string>();

  function changeNameState(event: IChangeEvent) {
    setName(event.target.value);
  }

  function submit(event: IFormEvent) {
    frozen(event);
    alert(`Hello ${name}`);
  }

  return (
    <form onSubmit={submit}>
      <p>Name: {name}</p>
      <input type="text" onChange={changeNameState} />
      <button>Submit</button>
    </form>
  );
};
