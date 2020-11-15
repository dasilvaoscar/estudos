import Link from 'next/link'
import Button from '@material-ui/core/Button'
import HeadPage from '../../components/HeadPage'
import Layout from '../../components/Layout'


export default function FirstPosts() {
    return (
        <>
            <HeadPage />
            <Layout>
                <h1>First Post</h1>
                <Link href="/">
                    <Button variant="contained" color="primary">
                        Início
                    </Button>
                </Link>
            </Layout>
        </>
      )
}