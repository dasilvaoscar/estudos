import Head from 'next/head'

export default function HeadPage() {
    return(
        <Head>
            <title>NextJS | Estudos</title>
            <link rel="icon" href="/images/next-js.svg" />
            <meta name="viewport" content="initial-scale=1.0, width=device-width" />
            <meta property="og:title" content="Estudo de NextJS" key="title" />
        </Head>
    )
}