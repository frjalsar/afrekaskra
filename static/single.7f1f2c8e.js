parcelRequire=function(e,r,t,n){var i,o="function"==typeof parcelRequire&&parcelRequire,u="function"==typeof require&&require;function f(t,n){if(!r[t]){if(!e[t]){var i="function"==typeof parcelRequire&&parcelRequire;if(!n&&i)return i(t,!0);if(o)return o(t,!0);if(u&&"string"==typeof t)return u(t);var c=new Error("Cannot find module '"+t+"'");throw c.code="MODULE_NOT_FOUND",c}p.resolve=function(r){return e[t][1][r]||r},p.cache={};var l=r[t]=new f.Module(t);e[t][0].call(l.exports,p,l,l.exports,this)}return r[t].exports;function p(e){return f(p.resolve(e))}}f.isParcelRequire=!0,f.Module=function(e){this.id=e,this.bundle=f,this.exports={}},f.modules=e,f.cache=r,f.parent=o,f.register=function(r,t){e[r]=[function(e,r){r.exports=t},{}]};for(var c=0;c<t.length;c++)try{f(t[c])}catch(e){i||(i=e)}if(t.length){var l=f(t[t.length-1]);"object"==typeof exports&&"undefined"!=typeof module?module.exports=l:"function"==typeof define&&define.amd?define(function(){return l}):n&&(this[n]=l)}if(parcelRequire=f,i)throw i;return f}({"wxma":[function(require,module,exports) {
"use strict";Object.defineProperty(exports,"__esModule",{value:!0}),exports.default=void 0;var e=a(require("axios")),t=a(require("vue-spinner/src/PulseLoader.vue"));function a(e){return e&&e.__esModule?e:{default:e}}var i={name:"KeppandiSingle",components:{PulseLoader:t.default},data:function(){return{competitor_info:[],event_info:[],isReady:!1,competitorID:"",message:"",isShowAllEvents:!0}},created:function(){this.competitorID=this.$route.params.competitorID,this.get_data()},methods:{get_data:function(){var t=this;this.$parent.loading=!0,this.message="Næ í gögn ekki stökkva langt 😉",this.data=[];var a="/api/keppandi/"+this.competitorID;e.default.all([e.default.get(a)]).then(e.default.spread(function(){for(var e=arguments.length,a=new Array(e),i=0;i<e;i++)a[i]=arguments[i];t.competitor_info=a[0].data.Competitor,t.event_info=a[0].data.Events})).catch(function(e){t.message="Villa frá vefþjóni ("+e+") 😭"}).finally(function(){t.$parent.loading=!1,t.isReady=!0})}}};exports.default=i;
(function(){var t=exports.default||module.exports;"function"==typeof t&&(t=t.options),Object.assign(t,{render:function(){var t=this,s=t.$createElement,e=t._self._c||s;return e("div",[t.isReady?e("div",{attrs:{id:"competitor-view"}},[e("div",{staticClass:"card",staticStyle:{width:"35.5rem"}},[e("img",{staticClass:"card-img-top",attrs:{src:"/static/kt_action.86c0c7c9.jpg",alt:"Card image cap"}}),t._v(" "),e("div",{staticClass:"card-header"},[t._v(" "+t._s(t.competitor_info.FirstName)+" "+t._s(t.competitor_info.LastName)+" ("+t._s(t.competitor_info.Club)+") ")]),t._v(" "),e("div",{staticClass:"card-body"},[e("table",{staticClass:"table table-striped table-hover table-responsive-sm table-sm"},[e("col",{staticClass:"wide",attrs:{span:"1"}}),t._v(" "),t._m(0),t._v(" "),e("tbody",t._l(t.event_info,function(s,a){return e("tr",{directives:[{name:"show",rawName:"v-show",value:a<3&&t.showAllEvents,expression:"index < 3 && showAllEvents"}]},[e("th",{attrs:{scope:"row"}},[t._v(t._s(s.Event))]),t._v(" "),e("td",[t._v(t._s(s.PB_out))]),t._v(" "),e("td",[t._v(t._s(s.PB_in))]),t._v(" "),e("td",[t._v(t._s(s.count))])])}),0)])]),t._v(" "),e("div",{staticClass:"card-footer text-muted text-center"},[t._v(" Sýna meira. ")])])]):t._e()])},staticRenderFns:[function(){var t=this.$createElement,s=this._self._c||t;return s("thead",[s("tr",[s("th",{attrs:{scope:"col"}},[this._v("Grein")]),this._v(" "),s("th",{attrs:{scope:"col"}},[this._v("PB úti")]),this._v(" "),s("th",{attrs:{scope:"col"}},[this._v("PB inni")]),this._v(" "),s("th",{attrs:{scope:"col"}},[this._v("Fjöldi")])])])}],_compiled:!0,_scopeId:"data-v-4c2386",functional:void 0});})();
},{"axios":"dZBD","vue-spinner/src/PulseLoader.vue":"Rp91","./static/kt_action.jpg":[["kt_action.86c0c7c9.jpg","av81"],"av81"]}],"FheM":[function(require,module,exports) {
var t=null;function e(){return t||(t=n()),t}function n(){try{throw new Error}catch(e){var t=(""+e.stack).match(/(https?|file|ftp|chrome-extension|moz-extension):\/\/[^)\n]+/g);if(t)return r(t[0])}return"/"}function r(t){return(""+t).replace(/^((?:https?|file|ftp|chrome-extension|moz-extension):\/\/.+)\/[^\/]+$/,"$1")+"/"}exports.getBundleURL=e,exports.getBaseURL=r;
},{}],"TUK3":[function(require,module,exports) {
var r=require("./bundle-url").getBundleURL;function e(r){Array.isArray(r)||(r=[r]);var e=r[r.length-1];try{return Promise.resolve(require(e))}catch(n){if("MODULE_NOT_FOUND"===n.code)return new s(function(n,i){t(r.slice(0,-1)).then(function(){return require(e)}).then(n,i)});throw n}}function t(r){return Promise.all(r.map(u))}var n={};function i(r,e){n[r]=e}module.exports=exports=e,exports.load=t,exports.register=i;var o={};function u(e){var t;if(Array.isArray(e)&&(t=e[1],e=e[0]),o[e])return o[e];var i=(e.substring(e.lastIndexOf(".")+1,e.length)||e).toLowerCase(),u=n[i];return u?o[e]=u(r()+e).then(function(r){return r&&module.bundle.register(t,r),r}).catch(function(r){throw delete o[e],r}):void 0}function s(r){this.executor=r,this.promise=null}s.prototype.then=function(r,e){return null===this.promise&&(this.promise=new Promise(this.executor)),this.promise.then(r,e)},s.prototype.catch=function(r){return null===this.promise&&(this.promise=new Promise(this.executor)),this.promise.catch(r)};
},{"./bundle-url":"FheM"}],0:[function(require,module,exports) {
var b=require("TUK3");b.load([]).then(function(){require("wxma");});
},{}]},{},[0], null)
//# sourceMappingURL=/static/single.7f1f2c8e.js.map