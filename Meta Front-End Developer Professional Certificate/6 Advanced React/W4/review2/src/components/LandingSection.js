import React from "react";
import { Avatar, Heading, VStack } from "@chakra-ui/react";
import FullScreenSection from "./FullScreenSection";

const greeting = "Hello, I am Nourhene!";
const bio1 = "A frontend developer";
const bio2 = "specialized in React";

const LandingSection = () => (
  <FullScreenSection
    justifyContent="center"
    alignItems="center"
    isDarkBackground
    backgroundColor="#2A4365"
  >
    <VStack spacing={4} alignItems="center">
      <Avatar
        size="xl"
        name="Nourhene"
        src="https://i.pravatar.cc/150?img=7"
      />
      <Heading color="white" size="xl">
        {greeting}
      </Heading>
      <Heading color="white" size="md">
        {bio1}
      </Heading>
      <Heading color="white" size="md">
        {bio2}
      </Heading>
    </VStack>
  </FullScreenSection>
);

export default LandingSection;
