import styles from './footer.module.css'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faGithubAlt } from '@fortawesome/free-brands-svg-icons'
import { LinkedIn, GitHub } from '@material-ui/icons/';

export default function Footer() {
    return(
    <footer className={styles.footer}>
        <a
        href="https://github.com/OscarSilvaOfficial" 
        target="_blank">
        <GitHub className={styles.Icon} />
        </a>

        <a
        href="https://linkedin.com/in/dasilvaoscar/" 
        target="_blank">
        <LinkedIn color="primary" className={styles.Icon} />
        </a>
    </footer>
    )
}