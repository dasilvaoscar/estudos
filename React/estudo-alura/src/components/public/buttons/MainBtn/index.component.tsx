import { IStyleProps } from "../../../../helpers/interfaces/styles/styles.props";
import defaultStyles from './styles.module.scss'

interface MainBtnProps extends IStyleProps {
  title?: string;
  children?: React.ReactNode;
}

export function MainBtn({ title, styles, children }: MainBtnProps) {
  return (
    <button className={ defaultStyles.MainBtn } style={ styles }>
      { title ? title : children }
    </button>
  )
}