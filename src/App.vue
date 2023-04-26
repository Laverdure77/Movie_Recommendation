<template>
  
  <div class="background bg-gradient-to-l from-gray-700 via-gray-900 to-black">
    <div class="pt-10 bg-center min-h-screen max-h-content bg-blend-darken bg-repeat-y" style="background-image: url(/background/filmstrip-1174228.png);height: 1500px;">
      <div id='app' >
        <div>
          <h1 class=" p-10 text-transparent font-extrabold text-6xl bg-clip-text bg-gradient-to-r to-emerald-600 from-sky-400">
              Movie <br> Recommendation
          </h1>
          <Search/>
        </div>
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