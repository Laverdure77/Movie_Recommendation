<template>
  <div class="search static">

  <!-- Hero -->
    <h2 
      ref="hero"
      style="cursor: url('/cursor/icons8-clap-48.png')24 24,auto"
      @click="toggle()"
      class="mb-4 px-10 py-2 text-4xl font-extrabold leading-none tracking-tight bg-gradient-to-r text-transparent bg-clip-text to-emerald-600 from-sky-400">Please <br>
      <span v-if="!searchType" class="text-blue-600 dark:text-blue-500 font-extrabold">select 5 favorite movies <br></span> 
      <span v-if="searchType" class="text-blue-600 dark:text-blue-500 font-extrabold">enter 5 keywords <br></span> 
      to get a movie recommendation.
    </h2>

    <!-- favorites list --> 
    <div v-if="favoritesList.length > 0 & searchType == false" class="mt-4 px-10 py-2">
      <div class="bg-slate-200/60 rounded-md">
        <h2 class="text-3xl font-bold bg-blend-color p-2">My Favorite List:</h2> 
          <ul class='flex justify-center'>
            <li class='p-2 rounded-sm m-4' 
                style="cursor: url('/cursor/icons8-cross-mark-48.png')24 24,auto"
                @click="removeFromFavoritesList(film)"
                v-for="film in favoritesList" 
                :key="film">
              <img 
                v-if="film.poster_path"
                style="cursor: url('/cursor/icons8-movie-48.png')24 24,auto"
                @click="goToTMDB(film)"
                v-bind:src="baseUrlImage + film.poster_path" 
                width='100' 
                >
              <img 
                v-else
                src="/image/No-Image-Placeholder.png" 
                style="cursor: url('/cursor/icons8-movie-48.png')24 24,auto"
                @click="goToTMDB(film)"
                width='100' 
                >
            </li>
          </ul>
      </div>
    </div>

    <!-- Search Input -->
    <div ref="form" class="search-form px-10 py-2 " >
      <div class="px-10 py-2  bg-slate-200/60 rounded-md">
        <div class="max-w-xl">
          <div 
            v-show="query.length<5 & favoritesList.length != 5" 
            class="flex space-x-1 items-center mb-2">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8 text-red-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
              <p 
                v-if="favoritesList.length != 5"
                class="text-white text-lg font-semibold">
                Please enter something
              </p>
          </div>
          <div class="flex space-x-4">
            <div class="flex rounded-md overflow-hidden w-full">
            <!-- textarea -->
              <textarea 
                class="p-3"
                placeholder= "Enter at least 5 Keywords"
                v-if="searchType == true"
                v-model="textAreaInput"
                maxlength='1000' 
                minlength='20'
                rows="2" 
                cols="35">
              </textarea>
              <!-- Input search film favorites -->
              <input type="text" class="w-full rounded-md rounded-r-none p-3"
                v-if="favoritesList.length != 5 & searchType == false"  
                placeholder= "Enter movie title" 
                v-model="query" 
                @keyup="getResult(query)" />
              <!-- Clear Button -->
              <button 
                v-if="favoritesList.length != 5"
                @click="clearField()" 
                class="bg-white mx-2 p-4 text-lg font-semibold  rounded-md">
                Clear
              </button>
              <!-- Get Reco from textarea -->
              <button 
                v-if="searchType == true"
                v-bind:disabled="WordCount < 5"
                @click="getTextAreaRecommandation"
                class=" bg-blue-500 text-white p-4 text-lg font-semibold mx-1 rounded-md w-auto">
                Get recommendations!
              </button>
              <!-- Get reco from favorite list -->
              <button 
                v-if="favoritesList.length == 5 & searchType == false"
                @click="getRecommandation" 
                class=" bg-blue-500 text-white px-6 text-lg font-semibold py-4 mx-1 rounded-md">
                Get recommendations!
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Search Results list -->
    <div class="px-10 py-2">
      <div class="bg-slate-200/60 rounded-md px-10 py-2" v-if="favoritesList.length != 5 & searchType == false">
        <ul  class='flex flex-wrap justify-center'>
          <li 
            v-for='result in results' 
            class="p-10 m-3 rounded-sm bg-slate-300 w-40" 
            :key="results">
            <!-- if poster exist -->
            <img 
              v-if="result.poster_path"
              v-bind:src="baseUrlImage + result.poster_path" 
              @click="addToFavotitesList(result)" 
              width='100'
              style="cursor: url('/cursor/icons8-blue-heart-48.png')24 24,auto">
              <!-- if poster is missing -->
            <img 
              v-else
              src="/image/No-Image-Placeholder.png" 
              @click="addToFavotitesList(result)" 
              width='100'
              style="cursor: url('/cursor/icons8-blue-heart-48.png')24 24,auto">
            <p class="text-white">{{result.title}}</p>
          </li>
        </ul>
      </div>
    </div>

    <!-- Recommandation  Favorites-->
    <div ref="recommendation" class="px-10 py-2" >
      <div class="bg-slate-200/60 rounded-md px-10 py-2" v-if="recommandationList.length != 0 & searchType == false">
        <h2  class="text-3xl font-bold px-10 py-2" v-if="recommandationList.length != 0 & searchType == false">My Recommendations:</h2>
        <ul class="">
          <li v-for='reco in recommandationList' class="p-5 m-3 rounded-sm bg-slate-300 flex">
            <div class="card-left p-2 basis-1/2">
              <p class="text-black text-lg font-semibold pb-1">{{reco[0].title}}</p> 
              <img 
                v-bind:src="baseUrlImage + reco[0].poster_path" 
                @click="goToTMDB(reco[0])" 
                style="cursor: url('/cursor/icons8-movie-48.png')24 24,auto"
                width='150'>
            </div>
            <div class="card-right basis-1/2">
              <p class="text-black pt-8">{{reco[0].overview}}</p>
            </div>
          </li>
        </ul>
      </div>
    </div>

    <!-- Recommandation TextArea-->
    <div class="px-10 py-2">
      <div class="bg-slate-200/60 rounded-md px-10 py-2" v-if="recommandationListTextArea.length != 0 & searchType == true">
        <h2 ref="recommendationText" class="text-3xl font-bold" v-if="recommandationListTextArea.length != 0 & searchType == true">My Recommendations:</h2>
        <ul class="">
          <li v-for='reco in recommandationListTextArea' class="p-5 m-3 rounded-sm bg-slate-300 flex">
            <div class="card-left p-2 basis-1/2">
              <p class="text-black text-lg font-semibold pb-1">{{reco[0].title}}</p> 
              <img 
                v-bind:src="baseUrlImage + reco[0].poster_path" 
                @click="goToTMDB(reco[0])" 
                style="cursor: url('/cursor/icons8-movie-48.png')24 24,auto"
                width='150'>
            </div>
            <div class="card-right basis-1/2">
              <p class="text-black pt-8">{{reco[0].overview}}</p>
            </div>
          </li>
        </ul>
      </div>
    </div>

  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'search',
  data () {
  return {
      searchType: false,
      textAreaInput: '',
      query: '',
      results: null, 
      baseUrlApi: 'https://movie-recommandation.onrender.com',
      // baseUrlApi: 'http://127.0.0.1:5100',
      baseUrlImage: 'http://image.tmdb.org/t/p/w500',
      baseUrlMovie: 'https://api.themoviedb.org/3/search/movie?api_key=58dff008e6a9f668953c9a34796bec27&query=',
      favoritesList: [],
      favoritesIdList: [],
      recommandationList: [],
      recommandationListTextArea: []

    }
  },
  methods: {
    // TMDB query for movies details
    async getResult(query) {
      console.log(this.baseUrlMovie + query)
      axios.get(this.baseUrlMovie + query)
            .then(response => { this.results = response.data.results})
    },

    // API query for recommendation
    async getRecommandation() {
      this.$toast.info('Recommendation request sent to API')
      this.$toast.info('Please allow at least 30 sec to get a recommendations!')
      axios.post( this.baseUrlApi + '/recommandation',
        JSON.stringify(this.queryFromFavorites),
        {
          headers: {
            'Content-Type': 'application/json',  
          }
        }
      )
      .then(response => { 
                        this.recommandationList.length = 0  
                        console.log(response.data)
                        Object.values(response.data).forEach( film => {
                          axios.get( this.baseUrlMovie + film)
                                .then(response => {
                                  this.recommandationList.push(response.data.results) })
                        
                        })
                      }
            )
      console.log('recommendation query sent')
    },
    addToFavotitesList(film) {
      console.log(film.id)
      if (this.favoritesIdList.includes(film.id)){
        this.$toast.error('Already in favorite list')
      }
      else{
        if (this.favoritesList.length < 5){
            this.favoritesIdList.push(film.id)
            this.favoritesList.push(film)
            this.recommandationList = []
            this.$toast.info('Film added to favorite list')
          }
          else{
            console.log('Favorites List is full')
          }
        }
    },
    async getTextAreaRecommandation(){
      this.$toast.info('Recommendation request sent to api')
      this.$toast.info('Please allow at least 30 sec to get the recommendations!')
      axios.post( this.baseUrlApi + '/recommandation',
                  JSON.stringify({textareainput: this.textAreaInput}),
                  {
                    headers: {
                      'Content-Type': 'application/json',
                    }
                  }
            )
            .then(response => { 
                              console.log(response.data)
                              Object.values(response.data).forEach( film => {
                                axios.get( this.baseUrlMovie + film)
                                      .then(response => {this.recommandationListTextArea.push(response.data.results) })
                              })
                            }
            )
    },
    removeFromFavoritesList(film){
      this.favoritesIdList.splice(this.favoritesIdList.indexOf(film.id),1)
      this.favoritesList.splice(this.favoritesList.indexOf(film),1)
      this.$toast.warning('Film removed from favorite list')
    },
    goToTMDB(film){
      window.open('https://www.themoviedb.org/movie/'+ film.id)
    },
    toggle() {
      this.searchType = !this.searchType
    },
    scrollToEl(el) {
      this.$refs[el].scrollIntoView({behavior:"smooth"})
      console.log('scroll to '+ el)
      
    },
    clearField() {
      if (this.searchType == true){
        this.textAreaInput = ''
      }
      if (this.searchType == false){
        this.query = ''
      }
    }
  },
  computed:{
    WordCount() {
      return this.textAreaInput.trim().split(/\s+/).length;
    },
    queryFromFavorites(){
      if(this.favoritesList.length == 5) {
        this.overviews = {}
        for (let i = 0; i < this.favoritesList.length; i++) {
          this.overviews[i] = this.favoritesList[i].overview
        }
        console.log(this.overviews) 
        this.scrollToEl("hero")
        return this.overviews
      }
    },
  },
  watch:{
  }
}
</script>