/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    // Main templates folder
    "./templates/**/*.html",

    // Any app's templates folder
    "./**/templates/**/*.html",

    // If you use JS with Tailwind classes
    "./static/**/*.js",

    // Optional: Python template strings inside .py files
    "./**/*.py",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
};
