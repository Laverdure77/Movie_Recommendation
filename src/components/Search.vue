<template>
  <div class="search static">

    <!-- Toggle -->
    <!-- <div class="toggle-button-cover  absolute right-0 top-10">
      <div class="button-cover">
        <div class="button r" id="button-2">
          <input v-model="searchType" type="checkbox" class="checkbox" />
          <div class="knobs"></div>
          <div class="layer"></div>
        </div>
      </div>
    </div> -->
    <h2 
      style="cursor: url('/cursor/icons8-clap-48.png')24 24,auto"
      @click="toggle()"
      class="mb-4 px-10 py-2 text-4xl font-extrabold leading-none tracking-tight bg-gradient-to-r text-transparent bg-clip-text to-emerald-600 from-sky-400">Please <br>
      <span v-if="!searchType" class="text-blue-600 dark:text-blue-500 font-extrabold">select 5 favorite movies <br></span> 
      <span v-if="searchType" class="text-blue-600 dark:text-blue-500 font-extrabold">enter 5 keywords <br></span> 
      to get a movie recommendation.
    </h2>
    <!-- Toggle -->
    <!-- <div class="togglecontainer">
      <label for="toggle">
        <input v-model="searchType" class="input" type="checkbox" id="toggle"/>
        <div class="toggle-wrapper"><span class="selector"></span></div>
      </label>
    </div> -->

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
                style="cursor: url('/cursor/icons8-movie-48.png')24 24,auto"
                @click="goToTMDB(film)"
                v-bind:src="baseUrlImage + film.poster_path" 
                width='100' 
                >
            </li>
          </ul>
      </div>
    </div>

    <!-- Search Input -->
    <div class="search-form px-10 py-2 " >
      <div class="px-10 py-2  bg-slate-200/60 rounded-md">
        <div class="max-w-xl">
          <div v-show="query.length<5" class="flex space-x-1 items-center mb-2">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8 text-red-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
            <p class="text-white text-lg font-semibold">Please enter something</p>
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
              <button @click="clearField()" class="bg-white mx-2 p-4 text-lg font-semibold  rounded-md">
                Clear
              </button>
              <button 
                v-if="searchType == true & WordCount >=5"
                @click="getTextAreaRecommandation"
                class=" bg-blue-500 text-white p-4 text-lg font-semibold mx-1 rounded-md w-auto">
                Get recommendations!
              </button>
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

    <!-- submit button -->
    <!-- <button 
      class="m-2 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
      v-if="searchType == true & WordCount >=5"
      @click="getTextAreaRecommandation">
      Get recommendation!
    </button> -->

    <!-- Search Results list -->
    <div class="px-10 py-2">
      <div class="bg-slate-200/60 rounded-md px-10 py-2" v-if="favoritesList.length != 5 & searchType == false">
        <ul  class='flex flex-wrap justify-center'>
          <li 
            v-for='result in results' 
            class="p-10 m-3 rounded-sm bg-slate-300 w-40" 
            :key="results">
            <img 
              v-bind:src="baseUrlImage + result.poster_path" 
              @click="addToFavotitesList(result)" 
              width='100'
              style="cursor: url('/cursor/icons8-blue-heart-48.png')24 24,auto">
            <p class="text-white">{{result.title}}</p>
          </li>
        </ul>
      </div>
    </div>

    <!-- Recommandation  Favorites-->
    <!-- <button 
      class="m-2 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
      @click="getRecommandation" 
      v-if="favoritesList.length == 5 & searchType == false"
      >Get recommendations!
    </button> -->
    <div class="px-10 py-2" >
      <div class="bg-slate-200/60 rounded-md px-10 py-2" v-if="recommandationList.length != 0 & searchType == false">
        <h2 class="text-3xl font-bold px-10 py-2" v-if="recommandationList.length != 0 & searchType == false">My Recommendations:</h2>
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
        <h2 class="text-3xl font-bold" v-if="recommandationListTextArea.length != 0 & searchType == true">My Recommendations:</h2>
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

    // API query for recommandation
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
                              console.log(response.data)
                              Object.values(response.data).forEach( film => {
                                axios.get( this.baseUrlMovie + film)
                                      .then(response => {this.recommandationList.push(response.data.results) })
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
    getTextAreaRecommandation(){
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
    scrollToTop() {
      window.scroll(0,0)
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
        this.scrollToTop()
        return this.overviews
      }
    },
  },
  watch:{
  }
}
</script>

<style>
/* 
togglecontainer {
  display: grid;
  place-content: center;
  height: 100vh;
  background-color: #fefefe;
}
label {
  pointer-events: none;
}
label .input {
  display: none;
}
label .input:checked + .toggle-wrapper {
  box-shadow: 0 8px 14px 0 rgba(18, 51, 215, 0.12);
}
label .input:checked + .toggle-wrapper > .selector {
  left: calc(100% - 50px);
  background-color: #3957ee;
}
label .input:checked ~ .notification > .selected:before {
  content: "enter a prompt";
}
label .toggle-wrapper {
  position: relative;
  width: 120px;
  height: 60px;
  background-color: #eaeaea;
  border-radius: 999px;
  margin: auto;
  cursor: pointer;
  pointer-events: all;
  box-shadow: 0 8px 14px 0 rgba(215, 60, 18, 0.12);
}
label .toggle-wrapper .selector {
  width: 40px;
  height: 40px;
  position: absolute;
  top: 50%;
  left: 10px;
  transform: translateY(-50%);
  background-color: blue;
  transition: left 0.25s ease;
  border-radius: 50%;
}
label .notification {
  font-size: 20px;
  width: 100%;
}
label .notification .selected:before {
  content: "fill in your favorite movie list";
  font-size: 20px;
} */
/* Style toggle */
.toggle-button-cover {
  font-family: Arial, Helvetica, sans-serif;
  margin: 0;
  /* background-color: #f1f9f9; */
  display: table-cell;
  position: relative;
  width: 200px;
  height: 140px;
  box-sizing: border-box;
}

.button-cover {
  height: 100px;
  margin: 20px;
  /* background-color: #fff; */
  /* box-shadow: 0 10px 20px -8px #c5d6d6; */
  border-radius: 4px;
}

.button-cover:before {
  /* counter-increment: button-counter;
  content: counter(button-counter); */
  position: absolute;
  right: 0;
  bottom: 0;
  color: #d7e3e3;
  font-size: 12px;
  line-height: 1;
  padding: 5px;
}

.button-cover,
.knobs,
.layer {
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
}

.button {
  position: relative;
  top: 50%;
  width: 74px;
  height: 36px;
  margin: -20px auto 0 auto;
  overflow: hidden;
}

.button.r,
.button.r .layer {
  border-radius: 100px;
}

.button.b2 {
  border-radius: 2px;
}

.checkbox {
  position: relative;
  width: 100%;
  height: 100%;
  padding: 0;
  margin: 0;
  opacity: 0;
  cursor: pointer;
  z-index: 3;
}

.knobs {
  z-index: 2;
}

.layer {
  width: 100%;
  background-color: #ebf7fc;
  transition: 0.3s ease all;
  z-index: 1;
}

/* Button 2 */
#button-2 .knobs:before,
#button-2 .knobs:after {
  content: "favorites";
  position: absolute;
  top: 4px;
  left: 4px;
  width: 20px;
  height: 10px;
  color: #fff;
  font-size: 10px;
  font-weight: bold;
  text-align: center;
  line-height: 1;
  padding: 9px 4px;
  background-color: #03a9f4;
  border-radius: 50%;
  transition: 0.3s ease all;
}

#button-2 .knobs:before {
  content: "fav";
}

#button-2 .knobs:after {
  content: "txt";
}

#button-2 .knobs:after {
  right: -28px;
  left: auto;
  background-color: #f44336;
}

#button-2 .checkbox:checked + .knobs:before {
  left: -28px;
}

#button-2 .checkbox:checked + .knobs:after {
  right: 4px;
}

#button-2 .checkbox:checked ~ .layer {
  background-color: #fcebeb;
}
</style>