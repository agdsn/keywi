<template>
  <div class="nav-bar">
    <ul class="list left">
      <li><router-link to="/keys">Meine Schlüssel</router-link></li>
      <li><router-link to="/keys">Ausgeliehene Schlüssel</router-link></li>
      <li><router-link to="/safe">Tresore</router-link></li>
      <li><router-link to="/lock">Schlösser</router-link></li>
      <li><router-link to="/location">Orte</router-link></li>
    </ul>
    <ul class="list">
      <li><router-link to="#">Logout</router-link></li>
    </ul>

  </div>
</template>

<script>
export default {
  name: "AppNavBar"
}
</script>

<style scoped>
  .nav-bar {
    background-color: var(--primary-color);
    padding: 10px 30px;
    display: flex;
    justify-content: space-between;
  }

  .list {
    display: inline-block;
  }

  .list li {
    display: inline-block;

  }

  .list a {
    text-decoration: none;
    color: #ffffff;
  }

  .left {
    max-width: 80%;
  }

  .left li {
    margin-right: 50px;
  }
</style>