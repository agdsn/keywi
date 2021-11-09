import * as  _ from 'lodash'
import {OpenAPIClientAxios} from "openapi-client-axios"
import Vue from "vue"
import vuetify from './plugins/vuetify'

var app = new Vue({
  el: '#app',
  data: {
    testvar: 'Keywi Projekt'
  }
});

function component() {
  const element = document.createElement('div');

  element.innerHTML = _.join(['Hello', 'webpack'], ' ');

  return element;
}

document.body.appendChild(component());