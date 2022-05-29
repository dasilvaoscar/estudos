import { IChangeEvent } from '@/helpers/interfaces/events/index';
import { IStyleProps } from '@/helpers/interfaces/styles/styles.props';
import { useState } from 'react';
import styles from './styles.module.scss';

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
