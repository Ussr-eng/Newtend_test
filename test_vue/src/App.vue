<template>
    <div id="wrapper">
        <nav class="navbar is-transparent">
      <div class="navbar-brand">
        <a class="navbar-item " >


        </a>
        <div class="navbar-burger" data-target="navbarExampleTransparentExample">
          <span></span>
          <span></span>
          <span></span>
        </div>
      </div>

      <div id="navbarExampleTransparentExample" class="navbar-menu">
        <div class="navbar-start">
          <div class="navbar-item has-dropdown is-hoverable">
            <a class="navbar-link mr-3">
              Page
            </a>
            <div class="navbar-dropdown is-boxed">
              <router-link :to="{ name: 'Home' }" class="navbar-item">
                Students
              </router-link>
              <router-link :to="{ name: 'Courses' }" class="navbar-item">
                Courses
              </router-link>

            </div>
          </div>
        </div>


      </div>
    </nav>
    <section class="section">
       <router-view/>
    </section>
   </div>

</template>


<style lang="scss">
@import '../node_modules/bulma';

</style>