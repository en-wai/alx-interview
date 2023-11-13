#!/usr/bin/node

const request = require('request');

// Retrieve the film ID from the command line arguments
const filmId = process.argv[2];

// Construct the API endpoint for fetching film information
const filmEndpoint = 'https://swapi-api.alx-tools.com/api/films/' + filmId;

// Function to fetch and display character names
function fetchData(characterUrls, index) {
  // Base case: check if all characters have been processed
  if (characterUrls.length === index) {
    return;
  }

  // Make a request to the API endpoint for a specific character
  request(characterUrls[index], (error, response, body) => {
    if (error) {
      console.log(error);
    } else {
      // Display the name of the character
      console.log(JSON.parse(body).name);
      
      // Recursively fetch and display the next character
      fetchData(characterUrls, index + 1);
    }
  });
}

// Make a request to the API endpoint for film information
request(filmEndpoint, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    // Extract character URLs from the film information
    const characterUrls = JSON.parse(body).characters;
    
    // Initiate the process of fetching and displaying character names
    fetchData(characterUrls, 0);
  }
});
