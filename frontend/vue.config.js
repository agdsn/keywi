const { defineConfig } = require('@vue/cli-service')
const { ProvidePlugin } = require('webpack');

module.exports = defineConfig({
  outputDir: "../backend/web",
  transpileDependencies: [
    'vuetify'
  ],
  configureWebpack: {
    resolve: {
      fallback: {
        http: require.resolve('http-browserify'),
        https: require.resolve('https-browserify'),
        stream: require.resolve('stream-browserify'),
      },
      aliasFields: ['browser'],
    },
    plugins: [
      new ProvidePlugin({
        process: 'process/browser',
      }),
      new ProvidePlugin({
        Buffer: ['buffer', 'Buffer'],
      }),
    ],
  },
})
