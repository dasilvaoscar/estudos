import styles from './main.module.css'

export default function Main() {
    return(
        
        <main className={styles.main}>
            <h1 className={styles.title}>
                <p className={styles.h1Violeta}>Estudos em</p> <a href="https://nextjs.org"><img className={styles.nextLogo} width="150" height="80" src="/images/next.png"></img></a>
            </h1>

            <p className={styles.description}>
                Rota principal: {' '}
                <code className={styles.code}>pages/index.js</code>
            </p>
        </main>
    )
}