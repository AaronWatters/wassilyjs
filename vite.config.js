const path = require('path')
const { defineConfig } = require('vite')

module.exports = defineConfig({
  build: {
    lib: {
      entry: path.resolve(__dirname, 'lib/main.js'),
      name: 'wassilyjs',
      fileName: (format) => `wassilyjs.${format}.js`
    }
  },
  test: {
    globals: true,
    environment: 'node',
  },
});