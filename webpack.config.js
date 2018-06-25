'use strict'

const { VueLoaderPlugin } = require('vue-loader');
const webpack = require('webpack');
const UglifyJsPlugin = require('uglifyjs-webpack-plugin');

module.exports = {
  mode: 'production',
  entry: {
    app: './jcdin/static/js/app.js',
    vendors: ['vue', 'axios']
  },
  module: {
    rules: [
      {
          test: /\.vue$/,
          use: 'vue-loader'
      }
    ]
  },
  plugins: [
    new VueLoaderPlugin(),
  ],
  resolve: {
    alias: {
      vue: "./node_modules/vue/dist/vue.common.js"
    },
  },
  optimization: {
    minimize: true,
    minimizer: [
      new UglifyJsPlugin({
        parallel: true
      })
    ]
  }
}
