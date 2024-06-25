/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    './static/js/**/*.js'
  ],
  theme: {
    extend: {
        fontFamily: {
           Spectral: ["Spectral SC", "serif"],
           Great: ["Great Vibes", "cursive"],
           Julius: ["Julius Sans One", "cursive"],
           EB: ["EB Garamond", "cursive"],
           Comforter: ["Comforter", "cursive"],
           Forum: ["Forum", "serif"],
           },
        margin: {
           '81': '20rem',
           },
    },
  },
  plugins: [],
}

