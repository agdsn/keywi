const path = require('path');

module.exports = {
  entry: './src/index.ts',
  module: {
    rules: [
      {
        test: /\.(sass|less|css)$/,
        use: [
            'ts-loader',
            'vue-style-loader',
            'css-loader',
            {
                loader: 'sass-loader',
                // Requires >= sass-loader@^8.0.0
                options: {
                  implementation: require('sass'),
                },
            }
        ],
        // exclude: /node_modules/,
      },
    ],
  },
  resolve: {
    extensions: ['.tsx', '.ts', '.js'],
    alias: {
      vue: 'vue/dist/vue.js'
    }
  },
  output: {
    filename: 'main.js',
    path: path.resolve(__dirname, 'dist'),
  },
};