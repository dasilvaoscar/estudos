import Head from 'next/head'
import Footer from '../components/Footer/footer'
import Main from '../components/Main/main'
import Menu from '../components/Menu/menu'
import styles from '../styles/Home.module.css'


export default function Home() {
  return (
    <div className={styles.container}>
      <Head>
        <title>NextJS | Aprendendo</title>
        <link rel="icon" href="/images/next-js.svg" />
      </Head>

      <Menu />
      <Main />
      <Footer />
    </div>
  )
}
