<template>
    <div class="content column is-half is-offset-one-quarter">
        <div class="box" >
            <div class="columns is-multiline">
                <div class="column is-10">
                    <h1 class="title">Информация о Курсе {{ course.name }}</h1>
                </div>
                <div class="column is-12">
                    <p v-if="course.start_date"><strong>Дата начала:</strong> {{ course.start_date }}</p>
                    <p v-if="course.end_date"><strong>Дата окончания:</strong> {{ course.end_date }}</p>
                    <p v-if="course.get_count_student"><strong>Количество студентов:</strong> {{ course.get_count_student }}</p>
                    <p><strong>Участники:</strong></p>
                    <div
                        v-for="participant in participants"
                        v-bind:key="participant.id"
                    >
                    <p class="mt-2 ml-4"><strong>ФИО:</strong> {{ participant.first_name }} {{ participant.last_name }} ({{ participant.email }}) <a class="ml-4" @click="deleteparticipant(participant.id)"><i class="fas fa-user-slash"></i></a></p>

                    </div>
                </div>
                <div class="column is-12">
                    <label>Добавить участника:</label>
                </div>
                <div class="column is-12 mb-1">
                    <div class="select ">
                        <select name="potential_participant" v-model="potential_participant" @change="addParticipant()">
                            <option value="">Выберите ученика</option>
                            <option
                                v-for="participant in potential_participants"
                                v-bind:key="participant.id"
                                v-bind:value="participant.id"
                            >
                                {{ participant.first_name }} {{ participant.last_name }}
                            </option>
                        </select>
                    </div>
                </div>
            </div>
        </div>
    </div>


</template>

<script>

    import axios from 'axios'

    export default {
        name: 'Course',
        data() {
            return {
                participants: [],
                course: [],
                potential_participants: [],
                potential_participant: ''
            }
        },
        mounted() {
            this.getCourseParticipant()
            this.getPotentialParticipants()
        },
        methods: {
            getCourseParticipant() {

                axios
                    .get(`/api/v1/course_participant/${this.$route.params.id}/get_course_participant/`)
                    .then(response => {
                        this.participants = response.data
                    })

                axios
                    .get(`/api/v1/course/${this.$route.params.id}/`)
                    .then(response => {
                        this.course = response.data
                    })
            },
            deleteparticipant(participant_id) {

                axios
                    .post(`/api/v1/course_participant/${this.$route.params.id}/delete_participant/`, {'course': participant_id})
                    .then(response => {
                        this.getCourseParticipant()
                        this.getPotentialParticipants()
                    })
            },
            getPotentialParticipants() {
                axios
                    .get(`/api/v1/course_participant/${this.$route.params.id}/potential_participants/`)
                    .then(response => {
                        delete(this.potential_participants)
                        this.potential_participants = response.data[0]
                    })
            },
            addParticipant() {
                console.log(this.potential_participant)
                axios
                    .post(`/api/v1/course_participant/${this.$route.params.id}/add_participant/`, {'participant_id': this.potential_participant})
                    .then(response => {
                        this.getCourseParticipant()
                        this.getPotentialParticipants()
                    })
            }
        }
    }
</script>
