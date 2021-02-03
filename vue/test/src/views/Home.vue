<template>
  <div>
    <h1>Welcome {{title2}}!</h1>
    <input type="text" v-model="input1">
    <button type="button" @click="getData">GET</button>
    <button type="button" @click="setData">SET</button>

    <select class="form-control" v-model="region" @change="changeRegion">
      <option :key="i" :value="d.v" v-for="(d, i) in options">{{d.t}}</option>
    </select>

    <table class="table table-bordered" v-if="tableShow">
      <tr :key="i" :value="d.v" v-for="(d, i) in options">
        <td>{{d.v}}</td>
        <td>{{d.t}}</td>
      </tr>
    </table>
  </div>
</template>

<script>
export default {
  data() {
    return {
      title: "Vue.js 입문 강의",
      title2: "Seoul",
      input1: "abcd",
      options: [
        {v:"S", t:"Seoul"},
        {v:"J", t:"Jeju"},
        {v:"B", t:"Busan"},
        ],
        region: "B",
        tableShow: true,
    };
    },
    watch: {
      input1() {
         console.log(this.input1);
        },
    },

    methods: {
      getData() {
          alert(this.input1);
        },
      setData() {
        this.input1 = "12345";
      },
      changeRegion() {
        alert(this.region);
      }
    },
    beforeCreate() {
      console.log("beforeCreated");
    },
    created() {
      console.log("Created");
    },
    beforeMount() {
      console.log("beforeMount");
    },
    mounted() {
      console.log("mounted");
    }, 
    beforeUpdate(){
      console.log("beforeUpdate");
    },
    updated(){
      console.log("updated");
    },
    beforeDestroy() {
      console.log("beforeDestroy");
    },
    destroyed(){
      console.log("destroyed");
    }
}
</script>