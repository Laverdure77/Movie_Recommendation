<template>
  <div class="background bg-no-repeat bg-top bg-gradient-to-r from-indigo-500 from-10% via-sky-500 via-30% to-emerald-500 to-90%"  style="background-image: url(/background/filmstrip-1174228.png);height: 1500px;">
    <div id='app'>
      <div>
        <h1 class="text-5xl font-bold">
            Movie <br> Recommendation
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