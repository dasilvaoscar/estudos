import { Grid, GridItem } from "@chakra-ui/react"


export const TestGrid = () => {
  return (
    <div>
      <Grid
        p={12}
        h='100vh'
        templateColumns='repeat(4, 1fr)'
        gap={4}
      >
        <GridItem rowSpan={4} bg='tomato' colSpan={1} />
        <GridItem rowSpan={1} bg='tomato' colSpan={3} />
        <GridItem rowSpan={1} bg='tomato' colSpan={1} />
        <GridItem rowSpan={1} bg='tomato' colSpan={1} />
        <GridItem rowSpan={3} bg='tomato' colSpan={1} />
        <GridItem rowSpan={1} bg='tomato' colSpan={1} />
        <GridItem rowSpan={1} bg='tomato' colSpan={1} />
        <GridItem rowSpan={1} bg='tomato' colSpan={2} />
      </Grid>
    </div>
  )
}

