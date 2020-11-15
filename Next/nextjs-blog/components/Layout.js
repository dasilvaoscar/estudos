import Container from '@material-ui/core/Container'
import styles from './css/layout.module.css'

export default function Layout({children}) {
    return <Container maxWidth="sm"><div className={styles.container}>{children}</div></Container>
}