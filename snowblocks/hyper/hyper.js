const colors = {
  black: "#e7e5e2",
  lightBlack: "#bbbdb6",
  red: "#aa586e",
  green: "#608f8e",
  yellow: "#447487",
  blue: "#56759a",
  magenta: "#7c6a93",
  cyan: "#a05b89",
  white: "#697383",
  lightWhite: "#555f6f",
  colorCubes: "#dfddd7",
  grayscale: "#929cad"
};

colors.lightRed = colors.red;
colors.lightGreen = colors.green;
colors.lightYellow = colors.yellow;
colors.lightBlue = colors.blue;
colors.lightMagenta = colors.magenta;
colors.lightCyan = colors.cyan;

module.exports = {
  config: {
    shell: "fish",
    fontSize: 13,
    fontFamily: "Iosevka, monospace",
    uiFontFamily: "Iosevka, monospace",
    padding: "0 0",
    cursorShape: "BLOCK",
    cursorColor: colors.white,
    cursorAccentColor: colors.black,
    foregroundColor: colors.white,
    backgroundColor: colors.black,
    selectionColor: colors.colorCubes,
    borderColor: colors.grayscale,
    colors
  },

  plugins: ["hyperminimal"],
  localPlugins: [],

  keymaps: {}
};
