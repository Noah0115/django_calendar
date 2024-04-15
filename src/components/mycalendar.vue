<!-- my-calendar.vue -->
<template>
  <!-- @datesSet="handleDatesRender" -->
  <div class="my-calendar">
    <FullCalendar ref="myCalendar" :options="calendarOptions" />
    <el-dialog
      :title="optTitle"
      :visible.sync="dialogFormVisible"
      @close="DialogClosed"
    >
      <el-form :model="form" ref="FormRef">
        <el-form-item label="事件名称" label-width="110px">
          <el-input
            v-model="form.title"
            auto-complete="off"
            placeholder="请输入事件名称"
          ></el-input>
        </el-form-item>
        <el-form-item label="开始时间" label-width="110px">
          <el-date-picker
            v-model="form.rrule.dtstart"
            type="datetime"
            placeholder="选择日期时间"
          >
          </el-date-picker>
        </el-form-item>
        <el-form-item label="活动时长(小时)" label-width="110px">
          <el-input-number
            v-model="form.duration"
            controls-position="right"
            :min="1"
          >
          </el-input-number>
        </el-form-item>
        <el-form-item label="事件地点" label-width="110px">
          <el-input
            v-model="form.area"
            auto-complete="off"
            placeholder="请输入事件地点"
          >
          </el-input>
        </el-form-item>
        <el-form-item label="事件描述" label-width="110px">
          <el-input
            v-model="form.detail"
            auto-complete="off"
            placeholder="请输入事件描述"
          ></el-input>
        </el-form-item>
        <el-form-item label="重复事件" label-width="110px">
          <el-checkbox-group v-model="form.more">
            <el-checkbox label="是" name="type"></el-checkbox>
          </el-checkbox-group>
        </el-form-item>
        <el-form v-show="form.more" label="重复事件">
          <el-form-item label="重复类型" label-width="110px">
            <el-select v-model="form.rrule.freq" placeholder="请选择重复类型">
              <el-option label="年" value="yearly"></el-option>
              <el-option label="月" value="monthly"></el-option>
              <el-option label="周" value="weekly"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="重复间隔" label-width="110px">
            <el-input-number
              v-model="form.rrule.interval"
              controls-position="right"
              :min="1"
            ></el-input-number>
          </el-form-item>
          <el-form-item label="结束时间" label-width="110px">
            <el-date-picker
              v-model="form.rrule.until"
              type="datetime"
              placeholder="选择日期时间"
            >
            </el-date-picker>
          </el-form-item>
        </el-form>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button
          type="warning"
          @click="delEvent"
          v-if="form.id"
          style="float: left"
          >删 除</el-button
        >
        <el-button @click="dialogFormVisible = false">取 消</el-button>
        <el-button type="primary" @click="saveEvent">确 定</el-button>
      </div>
    </el-dialog>
  </div>
</template>
  
  <script>
// 引入已经安装好的，项目中所需要的 FullCalendar 插件
import FullCalendar from '@fullcalendar/vue'
import dayGridPlugin from '@fullcalendar/daygrid'
import timeGridPlugin from '@fullcalendar/timegrid'
import interactionPlugin from '@fullcalendar/interaction'
import listPlugin from '@fullcalendar/list'
import rrulePlugin from '@fullcalendar/rrule'


export default {
  name: "my-calendar",
  components: {
    FullCalendar
  },
  data() {
    return {
      // 日历配置参数
      calendarOptions: {
        plugins: [dayGridPlugin, timeGridPlugin, interactionPlugin, listPlugin, rrulePlugin,],
        // 日历头部按钮位置
        headerToolbar: {
          left: 'prev,next today',
          center: 'title',
          right: 'dayGridMonth, timeGridWeek, timeGridDay'
        },
        // 日历头部按钮中文转换
        buttonText: {
          today: '今天',
          month: '月',
          week: '周',
          day: '天'
        },

        initialView: 'dayGridMonth', // 指定默认显示视图
        firstDay: '1',
        weekNumberCalculation: 'ISO', // 与firstDay配套使用
        eventColor: '#3d8eec', // 全部日历日程背景色
        // timeGridEventMinHeight: '20', // 设置事件的最小高度
        aspectRatio: '2.2', // 设置日历单元格宽高比
        displayEventTime: true, // 是否显示事件时间
        allDaySlot: false, // 周、日视图时，all-day不显示
        // eventLimit: true, // 设置月日程，与all-day slot 的最大显示数量，超过的通过弹窗展示
        eventTimeFormat: {
          hour: 'numeric',
          minute: '2-digit',
          hour12: false
        },
        slotLabelFormat: {
          hour: '2-digit',
          minute: '2-digit',
          meridiem: false,
          hour12: false // 设置时间为24小时制
        },
        locale: 'zh-cn',
        eventTimeFormat: {
          hour: '2-digit',
          minute: '2-digit',
          hour12: false
        },
        events: [],
        editable: false, // 是否可以进行（拖动、缩放）修改
        eventStartEditable: false, // Event日程开始时间可以改变，默认为true，若为false,则表示开始结束时间范围不能拉伸，只能拖拽
        eventDurationEditable: false, // Event日程的开始结束时间距离是否可以改变，默认为true,若为false，则表示开始结束时间范围不能拉伸，只能拖拽
        selectable: true, // 是否可以选中日历格
        selectMirror: true,
        selectMinDistance: 0, // 选中日历格的最小距离
        weekends: true,
        navLinks: true, // 天链接
        // selectHelper: false,
        // selectEventOverlap: false, // 相同时间段的多个日程视觉上是否允许重叠，默认为true，允许
        dayMaxEvents: true,
        dateClick: this.handleDateClick, // 日期点击
        eventsSet: this.handleEvents, // 事件点击
        eventClick: this.handleEventClick, // 日程点击信息展示
        eventDrop: this.handleEventDrop, // 日程拖动事件
        eventResize: this.eventResize, // 日程缩放事件

      },
      form: {
        user_id: '',
        id: null,//事件id
        title: '',//事件标题
        area: "",//地点
        detail: '',//描述
        duration: '10:00',//事件持续时间
        more: false,//是否为周期时间 默认为false
        rrule: {
          freq: 'weekly', //rrule是周期时间的一个对象 freq为按xx为周期有['weekly','monthly','yearly']
          interval: 1,  //周期循环的间隔,1就是没有间隔 2就是隔一个周期加一个时间
          dtstart: '2024-02-13T00:15:00Z', //开始时间
          until: '2025-02-10T11:30:00Z', // 周期事件结束时间,空的时候就是无限周期
          count: 1 //周期循环几次,1的时候代表循环一次就是普通事件,""的时候就是周期事件
        }
      },
      userid: '',
      calendarEvents: [
        {
          id: 1,
          title: '周事件',
          area: "北京",
          detail: '大商家',
          more: true,
          duration: '1:00',
          rrule: {
            freq: 'weekly',
            interval: 1,
            dtstart: '2024-02-13T00:00:00',
            until: '2025-02-10T11:30:00',
            count: ''
          },
        },
        {
          id: 2,
          title: '月事件',
          area: "北京",
          detail: '大商家',
          duration: '8:00',
          rrule: {
            freq: 'monthly',
            interval: 1,
            // bymonthday:[7],//如果不加就按每月的这一天开始算
            dtstart: '2024-02-10T10:30:00', // will also accept '20120201T103000'
            until: '2024-06-01' // will also accept '20120201'
          },
          more: true,

        },
        {
          id: 3,
          title: '年事件',
          duration: '8:00',
          more: true,
          rrule: {
            freq: 'yearly',
            interval: 1,
            // byyearday:[7],
            dtstart: '2024-02-19T10:30:00', // will also accept '20120201T103000'
            until: '2025-06-01' // will also accept '20120201'
          }
        }
        , {
          id: 4,
          title: '节假日',
          duration: '8:00',
          area: "北京",
          detail: '大商家',
          more: false,
          rrule: {
            count: 1,
            freq: 'weekly',
            interval: 1,
            // bymonthday: ['mo'],
            dtstart: '2024-02-02T10:30:00', // will also accept '20120201T103000'
            until: '2050-06-01' // will also accept '20120201'
          }
        },
        {
          id: 5,
          title: 'K日',
          duration: '8:00',
          area: "北京",
          detail: '大商家',
          more: false,
          rrule: {
            count: 1,
            freq: 'weekly',
            interval: 1,
            // bymonthday: ['mo'],
            dtstart: '2024-02-02T10:30:00', // will also accept '20120201T103000'
            until: '2050-06-01'
          }
        },
        {
          id: 6,
          title: '双休日',
          area: "北京",
          duration: '8:00',
          detail: '大商家',
          more: false,
          rrule: {
            count: 1,
            freq: 'weekly',
            interval: 1,
            // bymonthday: ['mo'],
            dtstart: '2024-02-02T10:30:00', // will also accept '20120201T103000'
            until: '2050-06-01'
          }
        },
      ],

      calendarEventDrop: info => {
        this.dropEvent(info);
      },

      optTitle: '添加事件',
      dialogFormVisible: false,

    }
  },
  mounted() {
    // this.mynotify();
    this.getlist();

  },
  created() {
    this.$notify.closeAll();
    this.getlist();


  },
  methods: {
    //启动测试
    async getlist() {
      this.userid = sessionStorage.getItem('userid') //先拿id
      const { data: res } = await this.$http.post("/get_event", {
        user_id: this.userid
      });//发请求
      // console.log('请求结果', res)
      if (res.code !== 200) {
        return this.$message.error(res.msg)
      }
      // this.$message.success(res.msg)
      this.calendarEvents = res.data
      this.calendarOptions.events = this.calendarEvents
      this.$notify.closeAll();
      // console.log(this.calendarOptions.events)
      this.mynotify();
    },

    handleEvents(info) {

    },

    // 日期点击
    handleDateClick(selectInfo) {

      // console.log(selectInfo.dateStr)
      if (confirm('您是否要在【' + selectInfo.dateStr + '】添加一个新的事件？')) {
        //数据初始化


        this.optTitle = '新增事件';
        this.form.title = '';
        this.form.id = '';
        this.form.duration = '10:00'
        let durationArr = this.form.duration.split(':');
        this.form.duration = parseInt(durationArr[0], 10);
        this.form.area = ''
        this.form.detail = ''
        this.form.more = false
        // 创建一个正则表达式，用于匹配日期字符串中是否包含字母 T
        let regex = new RegExp('T');
        if (regex.test(selectInfo.dateStr)) {
          this.form.rrule.dtstart = selectInfo.dateStr
        } else {
          this.form.rrule.dtstart = selectInfo.dateStr + 'T08:00:00+08:00'
        }
        this.form.rrule.freq = 'weekly'
        this.form.rrule.interval = 1
        this.form.rrule.until = ''
        this.dialogFormVisible = true;
      }
    },

    // 日程点击信息展示
    handleEventClick(info) {
      // console.log('事件点击:', info)
      info.el.style.borderColor = 'red'
      this.dialogFormVisible = true;
      this.optTitle = '修改事件';
      this.calendarEvents.forEach((item, index, arr) => {
        if (item.id == info.event.id) {
          this.form = item
          if (typeof this.form.duration != 'number') {
            let durationArr = this.form.duration.split(':');
            this.form.duration = parseInt(durationArr[0], 10);
          }

        }
      });
    },
    // 日程事件触发
    /* eventClick(info) {
      console.log('eventClick.info:', info)
      info.el.style.borderColor = 'red'
    }, */
    // 日程拖动事件
    handleEventDrop(info) {
      this.form = {
        id: info.event.id,
        title: info.event.title,
        start: info.event.startStr,
        end: info.event.endStr,
        area: info.event._def.extendedProps.area,
        detail: info.event._def.extendedProps.detail,
      };
      this.saveEvent();
      // console.log(this.form)
    },
    // 日程缩放事件
    eventResize(info) {
      this.form = {
        id: info.event.id,
        title: info.event.title,
        start: info.event.startStr,
        end: info.event.endStr,
        area: info.event._def.extendedProps.area,
        detail: info.event._def.extendedProps.detail,
      };
      this.saveEvent();
      // console.log(this.form)
    },
    //保存事件
    async saveEvent() {
      this.form.user_id = this.userid
      //判断是否为周期事件
      if (this.form.more == false) {
        this.form.rrule.count = 1
      } else {
        // console.log("是周期事件")
        delete this.form.rrule.count
      }
      //将持续时间字段格式化
      if (typeof this.form.duration === 'number') {
        this.form.duration = this.form.duration.toString() + ':00'

      }

      if (this.form.rrule.until === "") {
        // console.log("触发了",delete this.form.rrule.until)
        delete this.form.rrule.until;
      }
      // console.log('新增form', this.form)
      if (this.form.id === undefined || this.form.id == '') {
        //新增
        // this.form.id = res.id;
        const { data: res } = await this.$http.post("/add_event", this.form);
        // console.log(res)
        // this.calendarEvents.push(this.form);
        if (res.code !== 200) {
          return this.$message.error(res.msg)
        }
        this.$message.success(res.msg)
      } else { //修改
        const { data: res } = await this.$http.post("/update_event", this.form);
        // console.log(res)
        if (res.code !== 200) {
          return this.$message.error(res.msg)
        }
        this.$message.success(res.msg)

      }
      this.dialogFormVisible = false;
      this.getlist()

    },

    //弹窗
    async mynotify() {

      let calendarApi = this.$refs.myCalendar.getApi();
      let Events = calendarApi.getEvents()
      // let Events = info
      // this.handleEvents()
      let hasRecentEvent = false; // 定义一个变量，表示是否有近期活动
      let time = this.$moment().format('YYYY-MM-DDTHH:mm:ss');
      // console.log('所有事件', Events);
      for (let event of Events) {

        // 创建一个新的 Date 对象，表示当前系统时间
        let now = new Date(time);
        let nowstamp = now.getTime();//当前时间戳
        let startstamp = event.start.getTime();//事件开始时间戳
        let endstamp = event.end.getTime();//事件结束时间戳
        let minutesDifference = (startstamp - nowstamp) / (1000 * 60);//事件开始时间-当前时间
        if (minutesDifference <= 30 && minutesDifference > 0) {

          await this.$notify({
            title: '提示',
            message: event.title + '活动即将开始',
            type: 'warning',
            duration: 5000,
            customClass: "mynotify"
          });
          hasRecentEvent = true; // 将 hasRecentEvent 设置为 true
        } else if (startstamp < nowstamp && nowstamp < endstamp) {

          await this.$notify({
            title: '提示',
            message: event.title + '活动已经开始',
            type: 'warning',
            duration: 5000,
            customClass: "mynotify"
          });
          hasRecentEvent = true; // 将 hasRecentEvent 设置为 true
        }
      }
    },
    async delEvent() {
      const { data: res } = await this.$http.post("/del_event", { id: this.form.id });
      if (res.code !== 200) {
        return this.$message.error(res.msg)
      }
      this.$message.success(res.msg)
      this.dialogFormVisible = false;
      this.$notify.closeAll();
      this.getlist()
    },
    DialogClosed() {
      // console.log('guan')
      this.$refs.FormRef.resetFields();
      this.$notify.closeAll();
      this.getlist()
    },

  },

}
</script>
<style lang="less">
// .mynotify {
//   left: 50%;
//   // transform: translateX(55%);
// }
/* 自定义数字输入框append  */
</style>