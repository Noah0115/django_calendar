<template>
  <div>
    <!-- 面包屑导航 -->
    <el-breadcrumb>
      <el-breadcrumb-item :to="{ path: '/welcome' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>用户管理</el-breadcrumb-item>
      <el-breadcrumb-item>用户列表</el-breadcrumb-item>
    </el-breadcrumb>
    <!-- 卡片区域 -->
    <el-card class="box-card">
      <div>
        <!-- 分栏间隔 -->
        <el-row :gutter="20">
          <el-col :span="6"
            ><div class="grid-content bg-purple">
              <el-input
                placeholder="请输入用户名"
                v-model="queryInfo.query"
                clearable
                @clear="getUserList"
              >
                <el-button
                  slot="append"
                  icon="el-icon-search"
                  @click="getUserList"
                ></el-button>
              </el-input></div
          ></el-col>
          <el-col :span="6"
            ><div class="grid-content bg-purple">
              <el-button type="primary" @click="addDialogVisible = true"
                >添加用户</el-button
              >
            </div></el-col
          >
        </el-row>
        <!-- 用户列表区 -->
        <el-table stripe border :data="userlist" style="width: 100%">
          <el-table-column
            type="index"
            label="索引"
            width="90"
          ></el-table-column>
          <el-table-column prop="username" label="用户名"> </el-table-column>
          <el-table-column prop="email" label="邮箱"> </el-table-column>
          <el-table-column prop="role" label="角色">
            <template slot-scope="{ row }">
              {{ row.role === 1 ? "管理员" : "普通用户" }}
            </template>
          </el-table-column>
          <el-table-column prop="create_time" label="创建时间">
            <template slot-scope="{ row }">
              {{ formatDate(row.create_time) }}
            </template>
          </el-table-column>
          <el-table-column prop="last_time" label="最后一次登陆时间">
            <template slot-scope="{ row }">
              {{ formatDate(row.last_time) }}
            </template>
          </el-table-column>
          <el-table-column label="操作" width="180px">
            <template v-slot="scope">
              <el-button
                type="primary"
                icon="el-icon-edit"
                size="mini"
                @click="showEditDialog(scope.row.id)"
                >修改信息</el-button
              >
              <!-- 删除按钮 -->

              <el-switch
                v-model="scope.row.status"
                @change="StateChanged(scope.row.id)"
                active-text="激活"
                inactive-text="禁用"
              >
              </el-switch>
            </template>
          </el-table-column>
        </el-table>
      </div>
      <!-- 分页 -->
      <!--   <el-pagination
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
        :current-page="queryInfo.pagenum"
        :page-sizes="[1, 2, 5, 10]"
        :page-size="queryInfo.pagesize"
        layout="total, sizes, prev, pager, next, jumper"
        :total="total"
      >
      </el-pagination> -->
      <!-- 弹出框 -->
      <el-dialog
        title="添加用户"
        :visible.sync="addDialogVisible"
        width="50%"
        @close="addDialogClosed"
      >
        <el-form
          :model="addForm"
          :rules="addFormRules"
          ref="addFormRef"
          label-width="70px"
        >
          <el-form-item label="用户名" prop="username">
            <el-input v-model="addForm.username"></el-input>
          </el-form-item>
          <el-form-item label="密码" prop="password">
            <el-input v-model="addForm.password" type="password"></el-input>
          </el-form-item>
          <el-form-item label="邮箱" prop="email">
            <el-input v-model="addForm.email"></el-input>
          </el-form-item>
        </el-form>
        <span slot="footer" class="dialog-footer">
          <el-button @click="addDialogVisible = false">取 消</el-button>
          <el-button type="primary" @click="addUser">确 定</el-button>
        </span>
      </el-dialog>
      <el-dialog
        title="修改用户"
        :visible.sync="editDialogVisible"
        width="50%"
        @close="editDialogClosed"
      >
        <el-form
          :model="editForm"
          :rules="editFormRules"
          ref="editFormRef"
          label-width="70px"
        >
          <el-form-item label="用户名" prop="username">
            <el-input v-model="editForm.username"></el-input>
          </el-form-item>

          <el-form-item label="邮箱" prop="email">
            <el-input v-model="editForm.email"></el-input>
          </el-form-item>
          <el-form-item label="角色" prop="role">
            <el-select v-model="editForm.role" :placeholder="roleLabel">
              <el-option
                v-for="item in options"
                :key="item.value"
                :label="item.label"
                :value="item.value"
              >
              </el-option>
            </el-select>
          </el-form-item>
        </el-form>
        <span slot="footer" class="dialog-footer">
          <el-button @click="editDialogVisible = false">取 消</el-button>
          <el-button type="primary" @click="editUserInfo">确 定</el-button>
        </span>
      </el-dialog>
    </el-card>
  </div>
</template>

<script>
export default {
  data() {
    //验证邮箱规则
    var checkEmail = (rule, value, cb) => {
      const regEmail =
        /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
      if (regEmail.test(value)) {
        return cb();
      }
      cb(new Error("请输入合法邮箱"));
    };
    //手机号验证
    var checkMobile = (rule, value, cb) => {
      const regMobile = /^(?:(?:\+|00)86)?1[3-9]\d{9}$/;
      if (regMobile.test(value)) {
        return cb();
      }
      cb(new Error("请输入合法手机号"));
    };

    return {
      //获取用户列表参数对象
      queryInfo: {
        query: "",
      },
      userlist: [],
      total: 0,
      addDialogVisible: false,
      //添加用户的表单数据
      addForm: {
        username: "",
        password: "",
        email: "",
      },
      options: [{
        value: 0,
        label: '普通用户'
      }, {
        value: 1,
        label: '管理员'
      }],
      // value: '',
      //添加表单的验证规则和对象
      addFormRules: {
        username: [
          { required: true, message: "请输入用户名", trigger: "blur" },
          { min: 1, max: 10, message: "长度在 1 到 10 个字符", trigger: "blur" },
        ],

        //密码校验
        password: [
          { required: true, message: "请输入密码", trigger: "blur" },
          { min: 6, max: 15, message: "长度在 6 到 15 个字符", trigger: "blur" },
        ],
        email: [
          { required: true, message: "请输入邮箱", trigger: "blur" },
          {
            validator: checkEmail,
            trigger: "blur",
          },
        ]

      },
      editDialogVisible: false,
      editForm: {
      },
      editFormRules: {
        username: [
          { required: true, message: "请输入用户名", trigger: "blur" },
          { min: 1, max: 10, message: "长度在 1 到 10 个字符", trigger: "blur" },
        ],

        //密码校验
        password: [
          { required: true, message: "请输入密码", trigger: "blur" },
          { min: 6, max: 15, message: "长度在 6 到 15 个字符", trigger: "blur" },
        ],
        email: [
          { required: true, message: "请输入邮箱", trigger: "blur" },
          {
            validator: checkEmail,
            trigger: "blur",
          },
        ]
      },
      //需要被分配角色的用户信息
      UserInfo: {},
      //所有角色数据列表
      rolesList: [],
      //已选中的角色id
      selectedRoleId: "",


    };
  },
  watch: {

  },
  //创建生命周期对象
  created() {
    this.getUserList();
  },
  methods: {
    async getUserList() {
      if (this.queryInfo.query == '') {
        //调用请求，第一个参数是请求地址
        const { data: res } = await this.$http.get("/get_user");
        if (res.code !== 200) {
          return this.$message.error("获取用户列表失败");
        }
        this.$message.success("获取用户列表成功");
        this.userlist = res.data
      } else {
        const { data: res } = await this.$http.post("/get_user", {
          username: this.queryInfo.query
        });
        if (res.code !== 200) {
          return this.$message.error("获取用户列表失败");
        }
        this.$message.success("获取用户列表成功");
        this.userlist = res.data
      }
      this.userlist.forEach(item => {
        if (item.status === 0) {
          item.status = false;
          // 返回false
        } else if (item.status === 1) {
          item.status = true;
          // 返回true
        }
      })

    },
    //监听Pagesize改变的事件
    handleSizeChange(newSize) {
      // console.log(newSize);
      this.queryInfo.pagesize = newSize;
      this.getUserList();
    },
    //监听页码值改变的事件
    handleCurrentChange(newPage) {
      this.queryInfo.pagenum = newPage;
      this.getUserList();
      // console.log(newPage);
    },
    //监听对话框close事件
    addDialogClosed() {
      this.$refs.addFormRef.resetFields();
    },
    addUser() {
      this.$refs.addFormRef.validate(async (valid) => {
        /* console.log(valid) */
        if (!valid) return;
        // console.log(this.addForm)
        //可以发起添加用户的网络请求
        const { data: res } = await this.$http.post("/register", this.addForm);
        if (res.code !== 200) {
          return this.$message.error("添加用户失败");
        }
        this.$message.success("添加用户成功");
        this.addDialogVisible = false;
        this.getUserList();
      });
    },
    //显示编辑用户的对话框
    async showEditDialog(id) {
      const selectedItem = this.userlist.find(item => item.id === id);
      if (selectedItem) {
        this.editForm = { ...selectedItem, user_id: selectedItem.id };
        // 打开编辑对话框或执行其他操作
      } else {
        console.log("Item not found with id:", id);
      }
      // console.log(this.editForm)
      /* =this.editForm.role */
      this.editDialogVisible = true;
    },
    //监听对话框close事件
    editDialogClosed() {
      this.$refs.editFormRef.resetFields();
    },
    editUserInfo() {
      this.$refs.editFormRef.validate(async (valid) => {

        if (!valid) return;
        // this.editForm.status = this.editForm.status ? 1 : 0;
        // console.log('编辑表单提交', this.editForm)
        //可以发起添加用户的网络请求
        const { data: res } = await this.$http.post("/update_user", this.editForm);

        if (res.code !== 200) {
          return this.$message.error("更新用户信息失败");
        }
        this.$message.success("更新用户信息成功");
        this.editDialogVisible = false;
        this.getUserList();
      });
    },
    //滑块改变
    async StateChanged(id) {
      const selectedItem = this.userlist.find(item => item.id == id);
      // console.log(selectedItem.status)
      if (selectedItem) {
        this.editForm = { ...selectedItem, user_id: selectedItem.id };

        // 打开编辑对话框或执行其他操作
      } else {
        console.log("Item not found with id:", id);
      }

      this.editForm.status = this.editForm.status ? 1 : 0;
      // console.log('666', this.editForm)
      const { data: res } = await this.$http.post("/update_user", this.editForm);
      if (res.code !== 200) {
        return this.$message.error("禁用失败");
      }
      this.$message.success("修改成功");
      // console.log(this.editForm)
      this.getUserList();

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
    }
  },
  computed: {
    //将editForm.role数字转为标签
    roleLabel() {
      const role = this.editForm.role; // 假设这是从数据库获取的用户角色值

      const option = this.options.find(item => item.value === role);

      return option ? option.label : '';
    },

  }
};
</script>

<style lang='less' scoped>
.el-table {
  margin-top: 20px;
}
</style>