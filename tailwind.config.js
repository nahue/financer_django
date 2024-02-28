/** @type {import('tailwindcss').Config} */
const config = {
  content: [
    "./**/templates/**/*.html"
  ],
  theme: {
    extend: {},
  },
  plugins: [require("@tailwindcss/forms"), require("@tailwindcss/typography")],
};

module.exports = config
