import { useState } from 'react';
import { IChangeEvent } from '@/components/public/interfaces/events/change';
import { IFormEvent } from '@/components/public/interfaces/events/form';
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
