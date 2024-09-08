#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];

const url = `https://swapi.dev/api/films/${movieId}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error('Status:', response.statusCode);
  } else {
    const film = JSON.parse(body);
    const characters = film.characters;

    console.log(characters)

    const fetchCharacter = (characterUrl) => {
      return new Promise((resolve, reject) => {
        request(characterUrl, (error, response, body) => {
          if (error) {
            reject(error);
          } else if (response.statusCode !== 200) {
            reject(`Status: ${response.statusCode}`);
          } else {
            const character = JSON.parse(body);
            resolve(character.name);
          }
        });
      });
    };

    const fetchAllCharacters = async () => {
      for (const characterUrl of characters) {
        try {
          const characterName = await fetchCharacter(characterUrl);
          console.log(characterName);
        } catch (error) {
          console.error('Error:', error);
        }
      }
    };

    fetchAllCharacters();
  }
});
