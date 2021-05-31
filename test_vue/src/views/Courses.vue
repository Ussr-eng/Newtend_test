<template>
  <div class="home">
     <div class="columns is-multiline">
        <div class="column is-12">
            <div class="columns ">
                <div class="tabs">
                  <ul>
                    <li class="is-active"><a>Course</a></li>
                  </ul>
                </div>
            </div>
        </div>
     </div>
    <div class="columns is-multiline mt-6">
        <div
            class="column is-2"
            v-for="course in courses"
            v-bind:key="course.id"
        >
            <div class="card">
              <header class="card-header">
                <p class="card-header-title">
                  {{ course.name }}
                </p>
                  <p class="card-header-title-right mr-3 mt-3" >
                    <i class="fas fa-book fa-lg"></i>
                    </p>
              </header>
              <div class="card-content">
                <div class="content">
                  description: {{ course.description }}
                  quantity students: {{ course.get_count_student }}
                  <br>
                </div>
              </div>
              <footer class="card-footer">
                  <router-link :to="{ name: 'Course', params: { id:course.id } }" class="card-footer-item">информация</router-link>
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
        name: 'Courses',
        data() {
            return {
                courses: []
            }
        },
        mounted() {
            this.getCourses()
            this.getTest()
        },
        methods: {
            getCourses() {
                axios
                    .get('/api/v1/course/')
                    .then(response => {
                        for (let i = 0; i < response.data.length; i++) {
                            this.courses.push(response.data[i])
                        }
                        console.log(this.courses)
                    })
                    .catch(error => {
                        console.log(JSON.stringify(error))
                    })
            },
            getTest() {
                axios
                    .get(`/api/v1/course_participant/1/get_course_participant/`)
                    .then(response => {
                        console.log(response.data)

                    })
            }
        }
    }
</script>
