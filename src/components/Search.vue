<template>
  <div class="search">

    <!-- Toggle -->
    <div class="togglecontainer">
      <label for="toggle">
        <input v-model="searchType" class="input" type="checkbox" id="toggle"/>
        <div class="toggle-wrapper"><span class="selector"></span></div>
        <h2 class="text-neutral-700 notification font-bold">Please <span class="selected text-9xl font-bold"></span> to get a movie recommandation.</h2>
      </label>
    </div>

    <!-- favorites list --> 
    <div v-if="favoritesList.length > 0 & searchType == false" class="mt-4">
      <h2 class="bg-blend-color p-2">My Favorite List:</h2> 
      <div class="bg-slate-200/50 rounded-md">
          <ul class='flex justify-center'>
            <li class='p-2 rounded-sm m-4' 
                style="cursor: url('/src/assets/cursor/icons8-cross-mark-48.png')24 24,auto"
                @click="removeFromFavoritesList(film)"
                v-for="film in favoritesList" 
                :key="film">
              <img 
                style="cursor: url('/src/assets/cursor/icons8-movie-48.png')24 24,auto"
                @click="goToTMDB(film)"
                v-bind:src="baseUrlImage + film.poster_path" 
                width='100' 
                >
            </li>
          </ul>
      </div>
    </div>

    <!-- Search Input -->
    <div class="bg-slate-400" >
      <form>
        <textarea 
          placeholder= "Enter at least 5 Keywords"
          v-if="searchType == true"
          v-model="textAreaInput"
          maxlength='1000' 
          minlength='20'
          rows="2" 
          cols="55">
        </textarea>
        <input 
          v-if="favoritesList.length != 5 & searchType == false"  
          placeholder= "Enter movie title"
          class="p-3 border-solid boder-2 text-blue-600/100 border-indigo-600" 
          type="text" 
          v-model="query" 
          @keyup="getResult(query)">
      </form>
    </div>

    <!-- submit button -->
    <button 
      v-if="searchType == true & WordCount >=5"
      @click="getTextAreaRecommandation()"
      type="submit">
      Get recommendation!
    </button>

    <!-- Search Results list -->
    <div class="bg-slate-200/60 rounded-md" v-if="favoritesList.length != 5 & searchType == false">
      <ul  class='flex flex-wrap justify-center'>
        <li 
          v-for='result in results' 
          class="p-10 m-3 rounded-sm bg-slate-300 w-40" 
          :key="results"
          >
          <img 
            v-bind:src="baseUrlImage + result.poster_path" 
            @click="addToFavotitesList(result)" 
            width='100'
            style="cursor: url('/src/assets/cursor/icons8-green-heart-48.png')24 24,auto">
          <p class="text-white">{{result.title}}</p>
        </li>
      </ul>
    </div>

    <!-- Recommandation -->
    <button @click="getRecommandation" v-if="favoritesList.length == 5">submit</button>
    <div class="bg-slate-200/60 rounded-md" v-if="recommandationList.length != 0">
      <h2>My Recommandations:</h2>
      <ul class="">
        <li v-for='reco in recommandationList' class="p-5 m-3 rounded-sm bg-slate-300 flex">
          <div class="card-left p-2 basis-1/2">
            <p class="text-black">{{reco[0].title}}</p> 
            <img 
              v-bind:src="baseUrlImage + reco[0].poster_path" 
              @click="goToTMDB(reco[0])" 
              style="cursor: url('/src/assets/cursor/icons8-movie-48.png')24 24,auto"
              width='150'>
          </div>
          <div class="card-right basis-1/2">
            <p class="text-black pt-8">{{reco[0].overview}}</p>
          </div>
        
        </li>
      </ul>
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
      baseUrlImage: 'http://image.tmdb.org/t/p/w500',
      baseUrlMovie: 'https://api.themoviedb.org/3/search/movie?api_key=58dff008e6a9f668953c9a34796bec27&query=',
      favoritesList: [],
      favoritesIdList: [],
      recommandationList: []
    }
  },
  methods: {
    // TMDB query for movies details
    async getResult(query) {
      console.log(this.baseUrlMovie + query)
      axios.get( this.baseUrlMovie + query)
            .then(response => { this.results = response.data.results})
    },

    // API query for recommandation
    async getRecommandation() {
      console.log(JSON.stringify(Object.assign({},this.queryFromFavorites)))
      // console.log(this.baseUrlApi + '/recommandation')
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
      console.log('recommandation list filled')
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
      // console.log(JSON.stringify(Object.assign({},this.textAreaInput)))
      console.log(JSON.stringify(this.textAreaInput))
      axios.post( this.baseUrlApi + '/recommandation',
                  JSON.stringify(this.textAreaInput),
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
    },
    removeFromFavoritesList(film){
      this.favoritesIdList.splice(this.favoritesIdList.indexOf(film.id),1)
      this.favoritesList.splice(this.favoritesList.indexOf(film),1)
      this.$toast.warning('Film removed from favorite list')
    },
    goToTMDB(film){
      window.open('https://www.themoviedb.org/movie/'+ film.id)
    }
  },
  computed:{
    WordCount() {
      return this.textAreaInput.trim().split(/\s+/).length;
    },
    queryFromFavorites(){
      this.overviews = []
      if(this.favoritesList.length == 5) {
        this.favoritesList.forEach(film => {
          this.overviews.push(film.overview)
        })
        return this.overviews
      }
    },
    recommandationListFavorites() {
      if (this.favoritesList.length == 5) {
        this.getRecommandation()
      }
    }
  },
  watch:{
  }
}
</script>

<style>

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
}

</style>