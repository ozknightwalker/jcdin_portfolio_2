'use strict'

const { VueLoaderPlugin } = require('vue-loader');
const path = require('path');
const webpack = require('webpack');

const BaseConfig = {
    mode: 'development'
};

var AppConfig = Object.assign({}, BaseConfig, {
  entry: {
    app: './jcdin/static/js/app.js',
    vendors: ['vue', 'axios', 'vue-material']
  },
  module: {
    rules: [
      {
        test: /\.vue$/,
        use: 'vue-loader'
      },
      {
        test: /\.css$/,
        loader: 'style-loader!css-loader'
      },
      {
        test: /\.js$/,
        exclude: /node_modules/,
        loader: 'babel-loader'
      }
    ]
  },
  plugins: [
    new VueLoaderPlugin(),
  ],
  resolve: {
    alias: {
      vue: path.resolve(__dirname, 'node_modules/vue/dist/vue.esm.js'),
      source: path.resolve(__dirname, 'jcdin/static/js'),
      components: path.resolve(__dirname, 'jcdin/static/js/vue/components'),
    }
  }
});

var ServiceWorkerConfig = Object.assign({}, BaseConfig,{
    entry: {
      'service-worker': './jcdin/static/js/service-worker.js'
    },
    output: {
      path: path.join(__dirname, 'jcdin/static/js/'),
      filename: 'sw.js'
    },
});

module.exports = [
    AppConfig, ServiceWorkerConfig,
];
