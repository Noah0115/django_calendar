<template>
  <div>
    <!-- 面包屑导航 -->
    <el-breadcrumb>
      <el-breadcrumb-item :to="{ path: '/welcome' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>事件管理</el-breadcrumb-item>
      <el-breadcrumb-item>事件列表</el-breadcrumb-item>
    </el-breadcrumb>
    <!-- 卡片区域 -->
    <el-card class="box-card">
      <div>
        <!-- 分栏间隔 -->
        <el-row :gutter="20">
          <el-col :span="6"
            ><div class="grid-content bg-purple">
              <el-input
                placeholder="请输入事件标题"
                v-model="queryInfo.query"
                clearable
                @clear="getEvenList"
              >
                <el-button
                  slot="append"
                  icon="el-icon-search"
                  @click="getEvenList"
                ></el-button>
              </el-input></div
          ></el-col>
          <el-col :span="6"
            ><div class="grid-content bg-purple">
              <el-button type="primary" @click="showAddDialog"
                >添加事件</el-button
              >
            </div></el-col
          >
        </el-row>
        <!-- 用户列表区 -->
        <el-table stripe border :data="evenlist" style="width: 100%">
          <el-table-column
            type="index"
            label="索引"
            width="90"
          ></el-table-column>
          <el-table-column prop="title" label="标题"> </el-table-column>
          <el-table-column prop="area" label="地点"> </el-table-column>
          <el-table-column prop="detail" label="详情"> </el-table-column>
          <el-table-column prop="more" label="是否周期事件" width="80px">
            <template slot-scope="{ row }">
              {{ row.more ? "周期事件" : "普通事件" }}
            </template>
          </el-table-column>
          <el-table-column prop="duration" label="事件时长" width="80px">
            <template slot-scope="{ row }">
              {{ formatDuration(row.duration) }}
            </template>
          </el-table-column>
          <el-table-column prop="user_id" label="用户id" width="80px">
          </el-table-column>
          <el-table-column prop="freq" label="周期频率">
            <template slot-scope="{ row }">
              {{ row.more ? formatFreq(row.freq) : "普通事件" }}
            </template>
          </el-table-column>
          <el-table-column prop="interval" label="周期间隔">
            <template slot-scope="{ row }">
              {{ row.more ? row.interval + "次" : "普通事件" }}
            </template>
          </el-table-column>
          <el-table-column prop="dtstart" label="开始时间">
            <template slot-scope="{ row }">
              {{ formatDate(row.dtstart) }}
            </template>
          </el-table-column>
          <el-table-column prop="until" label="事件结束时间">
            <template slot-scope="{ row }">
              <!-- {{ row.until != null ? formatDate(row.until) : "永久事件" }} -->
              {{ row.more ? endDate(row.until) : endDataFalse(row) }}
            </template></el-table-column
          >

          <el-table-column label="操作" width="120px">
            <template v-slot="scope">
              <el-button
                type="primary"
                icon="el-icon-edit"
                size="mini"
                @click="showEditDialog(scope.row)"
                >修改信息</el-button
              >
            </template>
          </el-table-column>
        </el-table>
      </div>

      <!-- 弹出框 -->
      <el-dialog
        :title="optTitle"
        :visible.sync="dialogFormVisible"
        @close="DialogClosed"
      >
        <el-form :model="form" ref="FormRef">
          <el-form-item label="用户" prop="user_id" label-width="110px">
            <el-select v-model="form.user_id" placeholder="请选择用户">
              <el-option
                v-for="item in userlist"
                :key="item.id"
                :label="item.username"
                :value="item.id"
              >
              </el-option>
            </el-select>
          </el-form-item>

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
            <el-form-item label="间隔" label-width="110px">
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
    </el-card>
  </div>
</template>
  
  <script>
export default {
  data() {
    return {
      queryInfo: {
        query: "",
      },
      evenlist: [],
      userlist: [],
      addDialogVisible: false,
      optTitle: '添加事件',
      dialogFormVisible: false,
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
          dtstart: '', //开始时间
          until: '', // 周期事件结束时间,空的时候就是无限周期
          count: 1 //周期循环几次,1的时候代表循环一次就是普通事件,""的时候就是周期事件
        }
      },
      defaultform: {
        user_id: '',
        id: null,
        title: '',
        area: "",
        detail: '',
        duration: '10:00',
        more: false,
        rrule: {
          freq: 'weekly',
          interval: 1,
          dtstart: '',
          until: '',
          count: 1
        }
      },
    };
  },
  //创建生命周期对象
  created() {
    this.getEvenList();
    this.getUserList();
  },
  methods: {
    async getEvenList() {
      //   console.log('查寻信息', this.queryInfo)
      if (this.queryInfo.query == '') {
        //调用请求，第一个参数是请求地址
        const { data: res } = await this.$http.get("/get_all_events");

        if (res.code !== 200) {
          return this.$message.error("获取事件列表失败");
        }
        this.$message.success("获取事件列表成功");
        this.evenlist = res.data
      } else {
        const { data: res } = await this.$http.post("/get_all_events", {
          title: this.queryInfo.query
        });

        if (res.code !== 200) {
          return this.$message.error("获取事件列表失败");
        }
        this.$message.success("获取事件列表成功");
        this.evenlist = res.data

      }
    },
    async getUserList() {
      const { data: res } = await this.$http.post("/get_user", {
        username: this.queryInfo.query
      });
      if (res.code !== 200) {
        return this.$message.error("获取用户列表失败");
      }
      this.$message.success("获取用户列表成功");
      this.userlist = res.data
    },

    //显示新增事件的对话框
    showAddDialog() {
      //数据初始化
      this.form = { ...this.defaultform };

      this.optTitle = '新增事件';
      this.form.rrule.dtstart = ''
      this.form.duration = '10:00'
      let durationArr = this.form.duration.split(':');
      this.form.duration = parseInt(durationArr[0], 10);

      //   console.log('this.form:', this.form)
      //   console.log('this.defaultform', this.defaultform)
      this.dialogFormVisible = true;
    },
    //显示编辑事件的对话框
    showEditDialog(info) {
      this.optTitle = '修改事件';
      this.form.id = info.id
      this.form.title = info.title
      this.form.detail = info.detail
      this.form.area = info.area
      this.form.more = info.more
      this.form.duration = info.duration
      this.form.user_id = info.user_id
      this.form.rrule.freq = info.freq
      this.form.rrule.interval = info.interval
      this.form.rrule.dtstart = info.dtstart
      this.form.rrule.until = info.until
      this.form.rrule.count = info.count
      if (typeof this.form.duration != 'number') {
        let durationArr = this.form.duration.split(':');
        this.form.duration = parseInt(durationArr[0], 10);
      }
      this.dialogFormVisible = true;
    },
    //监听对话框close事件
    DialogClosed() {
      this.form = { ...this.defaultform };
      this.$refs.FormRef.resetFields();
      this.getEvenList()
    },
    async saveEvent() {
      //   this.form.user_id = this.userid
      //判断是否为周期事件
      if (this.form.more == false) {
        this.form.rrule.count = 1
      } else {

        delete this.form.rrule.count
      }
      //将持续时间字段格式化
      if (typeof this.form.duration === 'number') {
        this.form.duration = this.form.duration.toString() + ':00'
      }
      if (this.form.rrule.until === "") {
        delete this.form.rrule.until;
      }

      if (this.form.id === undefined || this.form.id == '' || this.form.id === null) {
        //新增

        const { data: res } = await this.$http.post("/add_event", this.form);
        if (res.code !== 200) {
          return this.$message.error(res.msg)
        }
        this.$message.success(res.msg)
      } else { //修改
        const { data: res } = await this.$http.post("/update_event", this.form);

        if (res.code !== 200) {
          return this.$message.error(res.msg)
        }
        this.$message.success(res.msg)

      }
      this.dialogFormVisible = false;
      this.form = { ...this.defaultform };
    },
    async delEvent() {
      const { data: res } = await this.$http.post("/del_event", { id: this.form.id });
      if (res.code !== 200) {
        return this.$message.error(res.msg)
      }
      this.$message.success(res.msg)
      this.dialogFormVisible = false;
      this.getEvenList()
    },
    formatDuration(durationString) {
      const hours = durationString.split(':');
      return `${parseInt(hours)}小时`;
    },
    //格式化日期
    formatDate(dateTimeString) {
      const date = new Date(dateTimeString);
      const year = date.getFullYear();
      const month = ('0' + (date.getMonth() + 1)).slice(-2);
      const day = ('0' + date.getDate()).slice(-2);
      const hours = ('0' + date.getHours()).slice(-2);
      const minutes = ('0' + date.getMinutes()).slice(-2);
      const seconds = ('0' + date.getSeconds()).slice(-2);
      return `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`;
    },
    formatFreq(freq) {
      switch (freq) {
        case 'weekly':
          return '每周';
        case 'monthly':
          return '每月';
        case 'yearly':
          return '每年';
        default:
          return '';
      }
    },
    endDate(until) {
      //先判断是不是为空
      if (until == null) {
        //空是永久事件
        return '永久事件'
      } else {
        return this.formatDate(until)
      }
    },
    endDataFalse(info) {
      
      let dtstart = new Date(info.dtstart);
      let [hours1, minutes1] = info.duration.split(':');
      dtstart.setMinutes(dtstart.getMinutes() + parseInt(hours1) * 60 + parseInt(minutes1));
      const date = dtstart;
      const year = date.getFullYear();
      const month = ('0' + (date.getMonth() + 1)).slice(-2);
      const day = ('0' + date.getDate()).slice(-2);
      const hours = ('0' + date.getHours()).slice(-2);
      const minutes = ('0' + date.getMinutes()).slice(-2);
      const seconds = ('0' + date.getSeconds()).slice(-2);
      return `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`;
    }
  },
  computed: {
    //将editForm.role数字转为标签
    userLabel() {
      const role = this.editForm.role; // 假设这是从数据库获取的用户角色值

      const option = this.options.find(item => item.value === role);

      return option ? option.label : '';
    }

  }
};
  </script>
  
  <style lang='less' scoped>
.el-table {
  margin-top: 20px;
}
</style>