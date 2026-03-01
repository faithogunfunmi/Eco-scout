// src/brandData.js

// This is our testing data we used with the frontend before we connected it to FireStore

// 0 = Yes, 1 = No, 2 = Mixed
export const MOCK_CASES = {
  yes: {
    name: "Patagonia",
    sustainability: 0, 
    ethics: 0,
    overall: "yes", // Used to set the meter needle
    recommendations: [] 
  },
  mixed: {
    name: "Nike",
    sustainability: 2, 
    ethics: 1,
    overall: "mixed",
    recommendations: ["Girlfriend Collective", "Patagonia", "Tentree"]
  },
  no: {
    name: "Shein",
    sustainability: 1, 
    ethics: 1,
    overall: "no",
    recommendations: ["Pact", "Skims Organic", "ThredUp"]
  }
};

// This is what shows up on the "Default" page when no brand is detected
export const DEFAULT_RECOMMENDATIONS = [
  { name: "ThredUp", type: "Second-hand" },
  { name: "Pact", type: "Basics" },
  { name: "Patagonia", type: "Athletic/Outdoor" },
  { name: "Good On You", type: "Brand Directory" }
];

