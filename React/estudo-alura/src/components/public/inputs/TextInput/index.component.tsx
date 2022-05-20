import { IChangeEvent } from '../../interfaces/event';
import { useState } from 'react';
import styles from './styles.module.scss';
import { IStyleProps } from '../../interfaces/styles/styles.props';

interface TextInputProps extends IStyleProps {
  value?: string;
}

export function TextInput(props: TextInputProps) {
  const [value, setValue] = useState<string>(props.value || '');

  async function setValueOfInput({ target, preventDefault }: IChangeEvent) {
    setValue(target.value);
  }

  return (
    <input
      className={styles.TextInput}
      type="text"
      value={value}
      style={props.styles}
      onChange={setValueOfInput}
    />
  );
}
