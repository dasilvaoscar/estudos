import { Box, Text, Flex } from "@chakra-ui/react"

export const TestGeral = () => {
  return (
    <div>
      <Box m={[20, 2]} bgGradient="linear(to-t, green.200, pink.500)">
        <Flex align="center" justify="space-between">
          <Text
            fontWeight="extrabold"
            fontSize="md"
          >
            Tomato
          </Text>
          <Text
            fontWeight="extrabold"
            fontSize="md"
          >
            Tomato
          </Text>
        </Flex>
      </Box>
    </div>
  )
}
