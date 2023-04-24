<template>
  <div class="background bg-no-repeat bg-top bg-gradient-to-r from-indigo-500 from-10% via-sky-500 via-30% to-emerald-500 to-90%"  style="background-image: url(./src/assets/background/filmstrip-1174228.png);">
    <div id='app'>
      <div>
        <h1 class="text-3xl font-bold underline">
            Movies Recommandation
        </h1>
        <Search/>
      </div>
    </div>
  </div>
</template>
<script>
import Search from './components/Search.vue'
export default {
 name: 'App',
 components: {
  Search
 }
}
</script>