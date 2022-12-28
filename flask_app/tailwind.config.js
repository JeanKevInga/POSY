/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",
    "./static/src/**/*.js"
  ],
  theme: {
    extend: {
      colors:{
        posyMain:'#4A6EEB'
      }
    },
  },
  plugins: [],
}