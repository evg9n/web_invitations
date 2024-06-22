/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    './static/js/**/*.js'
  ],
  theme: {
    extend: {
        fontFamily: {
           Cinzel: ["Cinzel", "serif"],
           Dancing: ["Dancing Script", "cursive"],
           Great: ["Great Vibes", "cursive"],
           Julius: ["Julius Sans One", "cursive"],
           EB: ["EB Garamond", "cursive"],
           },
        margin: {
           '81': '20rem',
           },
    },
  },
  plugins: [],
}

