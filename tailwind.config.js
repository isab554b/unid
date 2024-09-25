/** @type {import('tailwindcss').Config} */
module.exports = {
  mode: "jit",
  content: ["./views/**/*.*", "./assets/**/*.*"],
  theme: {
    extend: {
      colors: {
        unidBlue: "#92AACF",
        unidBlueHover: "#98B1D6",
        unidDarkBlue: "#1D1B6E",
        unidLightBlue: "#A0B4D3",
        unidPurple: "#59437B",
        unidLightPurple: "#E4CBE5",
        unidYellow: "#F7F0E6",
        unidLigthPink: "#F2EBED",
      },
      fontFamily: {
        saira: "'Saira', sans-serif",
        montserrat: "'Montserrat', sans-serif",
      },
      backgroundImage: {
        watermark: "url('/assets/graphics/watermark.png')",
        watermarkUniverse: "url('/assets/graphics/watermark-universe.png')",
      },
    },
    plugins: [],
  },
};
