<template>
  <div class="nav-bar">
    <ul class="list left">
      <li><a href="/keys">Meine Schlüssel</a></li>
      <li><a href="/keys">Ausgeliehene Schlüssel</a></li>
      <li><a href="/safe">Tresore</a></li>
      <li><a href="/lock">Schlösser</a></li>
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