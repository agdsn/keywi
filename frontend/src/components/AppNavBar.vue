<template>
  <div class="nav-bar">
    <ul class="list left">
      <li><a href="#">Meine Schlüssel</a></li>
      <li><a href="#">Ausgeliehene Schlüssel</a></li>
      <li><a href="#">Tresore</a></li>
      <li><a href="#">Schlösser</a></li>
    </ul>
    <ul class="list">
      <li><a href="#">Logout</a></li>
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