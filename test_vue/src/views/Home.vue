<template>
  <div class="home">
     <div class="columns is-multiline">
        <div class="column is-12">
            <div class="columns ">
                <div class="tabs">
                  <ul>
                    <li class="is-active"><a>Student</a></li>
                  </ul>
                </div>
            </div>
        </div>
     </div>

    <div class="columns is-multiline mt-6">
        <div
            class="column is-2"
            v-for="student in students"
            v-bind:key="student.id"
        >
            <div class="card">
              <header class="card-header">
                <p class="card-header-title">
                  {{ student.first_name }} {{ student.last_name }}
                </p>
                  <p class="card-header-title-right mr-3 mt-3" >
                    <i class="fas fa-user-alt"></i>
                    </p>
              </header>
              <div class="card-content">
                <div class="content">
                  email: {{ student.email }}
                  <br>
                </div>
              </div>
              <footer class="card-footer">
                  <router-link :to="{ name: 'Home' }" class="card-footer-item">информация</router-link>
              </footer>
            </div>
        </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
    import axios from 'axios'

    export default {
        name: 'Home',
        data() {
            return {
                students: []
            }
        },
        mounted() {
            this.getStudents()
        },
        methods: {
            getStudents() {
                axios
                    .get('/api/v1/student/')
                    .then(response => {
                        for (let i = 0; i < response.data.length; i++) {
                            this.students.push(response.data[i])
                        }
                        console.log(this.students)
                    })
                    .catch(error => {
                        console.log(JSON.stringify(error))
                    })
            }
        }
    }
</script>
