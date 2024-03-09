import React from "react";
import { Box, Heading, HStack, Image, Text, VStack } from "@chakra-ui/react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faArrowRight } from "@fortawesome/free-solid-svg-icons";

const Card = ({ title, description, imageSrc }) => (
  <Box
    backgroundColor="white"
    borderRadius="md"
    boxShadow="lg"
    p={4}
    transition="transform 0.2s"
    _hover={{ transform: "translateY(-8px)" }}
  >
    <Image src={imageSrc} alt={title} borderRadius="md" />
    <VStack spacing={2} align="start" mt={4}>
      <Heading as="h3" size="md">
        {title}
      </Heading>
      <Text color="gray.600" fontSize="sm">
        {description}
      </Text>
    </VStack>
    <HStack justify="space-between" mt={4}>
      <Text color="blue.500" fontWeight="bold">
        Learn More
      </Text>
      <FontAwesomeIcon icon={faArrowRight} size="1x" />
    </HStack>
  </Box>
);

export default Card;
