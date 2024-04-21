// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App.vue'
import router from './router'
import VueRouter from 'vue-router'
import axios from 'axios'
import Element from 'element-ui'
// import echarts from "echarts";
import moment from 'moment'//导入文件

Vue.prototype.$moment = moment;//赋值使用

// Vue.prototype.$echarts = echarts;
import '../node_modules/element-ui/lib/theme-chalk/index.css'
import '../src/assets/style.css'
import './theme/index.css'
import './assets/css/global.css'
import './assets/fonts/iconfont.css'
import VueQuillEditor from 'vue-quill-editor'
import store from './store'
Vue.use(VueQuillEditor)
//导入富文本编辑器对应的样式
import 'quill/dist/quill.core.css' // import styles
import 'quill/dist/quill.snow.css' // for snow theme
import 'quill/dist/quill.bubble.css' // for bubble theme
import  inputDirective from 'vue-el-input-directive'
Vue.use(inputDirective)
import  MyCalendar  from './components/mycalendar.vue'
Vue.component('my-calendar', MyCalendar);
Vue.use(Element)
Vue.config.productionTip = false
Vue.use(VueRouter)

axios.defaults.baseURL = 'http://127.0.0.1:7000'

axios.defaults.headers['Content-Type'] = 'application/json'
Vue.prototype.$http = axios
Vue.component("App", App);
document.title = '电子日历管理系统'
new Vue({
    el: '#app',
    router,
    store,
    render: h => h(App)
}).$mount('#app')
