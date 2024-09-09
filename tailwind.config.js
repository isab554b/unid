/** @type {import('tailwindcss').Config} */
module.exports = {
  mode: "jit",
  content: ["./views/**/*.*", "./assets/**/*.*"],
  theme: {
    extend: {
      colors: {
        unidBlue: "#92AACF",
        unidBlueHover: "#98B1D6",
        unidDarkBlue: "#2A2C64",
        unidLightBlue: "#CAD7E5",
        unidPurple: "#59437B",
        unidLightPurple: "#E3CBE3",
        unidYellow: "#F7F0E6",
        unidLigthPink: "#F4E9EC",
      },
      fontFamily: {
        saira: "'Saira', sans-serif",
        montserrat: "'Montserrat', sans-serif",
      },
      backgroundImage: {
        wave: "url('/assets/graphics/wave.svg')",
      },
    },
    plugins: [],
  },
};
