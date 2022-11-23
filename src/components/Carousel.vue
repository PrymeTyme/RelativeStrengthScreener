<template>
    <div class="carousel-container">
        <button class="btn1" @click="next">
            <fa icon="angle-left" />
        </button>
        <div class="carousel">
            <div class="inner" ref="inner" :style="innerStyles">
                <div class="card" v-for="card in cards" :key="card">
                    {{ card.ticker }}
                </div>
            </div>
        </div>
        <button class="btn2" @click="prev">
            <fa icon="angle-right" />
        </button>
    </div>

</template>
  
<script>
import { getData } from "../getData.js";
//import { useTickerStore } from "../stores/tickers.js"
//import { useTimeframeStore } from "../stores/timeframes.js";
//import { mapState } from 'pinia'
//import { storeToRefs } from 'pinia';


export default {
    name: 'CarouselHead',
    data() {
        return {
            cards: [0,0,0,0,0,0,0,0,0],
            innerStyles: {},
            step: '',
            transitioning: false
        }
    },

    mounted() {
        this.setStep()
        this.resetTranslate()
    },
    methods: {


        setStep() {
            const innerWidth = this.$refs.inner.scrollWidth
            const totalCards = this.cards.length
            this.step = `${innerWidth / totalCards}px`
        },
        next() {
            console.log(this.cards)
            console.log(typeof this.cards)
            if (this.transitioning) return
            this.transitioning = true
            this.moveLeft()
            this.afterTransition(() => {
                const card = this.cards.shift()
                this.cards.push(card)
                this.resetTranslate()
                this.transitioning = false
            })
        },
        prev() {
            if (this.transitioning) return
            this.transitioning = true
            this.moveRight()
            this.afterTransition(() => {
                const card = this.cards.pop()
                this.cards.unshift(card)
                this.resetTranslate()
                this.transitioning = false
            })
        },
        moveLeft() {
            this.innerStyles = {
                transform: `translateX(-${this.step})
                            translateX(-${this.step})`
            }
        },
        moveRight() {
            this.innerStyles = {
                transform: `translateX(${this.step})
                            translateX(-${this.step})`
            }
        },
        afterTransition(callback) {
            const listener = () => {
                callback()
                this.$refs.inner.removeEventListener('transitionend', listener)
            }
            this.$refs.inner.addEventListener('transitionend', listener)
        },
        resetTranslate() {
            this.innerStyles = {
                transition: 'none',
                transform: `translateX(-${this.step})`
            }
        },
        
    },

    async created() {
    getData('sector', 'daily').then(response => {
      console.log(response);
      this.cards = response
    })

  },

}
</script>
  
<style scoped>
.carousel-container {
    grid-row-start: 2;
    grid-column-start: 1;
    display: grid;
    grid-template-columns: 5% auto 5%;
    width: 830px;
}

.carousel {
    border: solid 3px #2A2E39;
    padding: 1em;
    cursor: pointer;
    background: #2A2E39;
    border-radius: 10px;
    color: #C3E0E5;
    overflow: hidden;
    height: 150px;
    width: 64vw;
    

}

.inner {
    transition: transform 0.2s;
    white-space: nowrap;
}

.card {
    width: 150px;
    margin-right: 10px;
    display: inline-flex;
    height: 150px;
    background-color: #131722;
    color: #C3E0E5;
    border-radius: 10px;
    align-items: center;
    justify-content: center;

    
}


.btn1 {
    left: 0%;
    color: #C3E0E5;
    background: #2A2E39;
    border-radius: 10px;
    border: solid 3px #2A2E39;
    color: #C3E0E5;
    font-size: 25px;
    cursor: pointer;

}

.btn2 {
    right: 0%;
    color: #C3E0E5;
    background: #2A2E39;
    border-radius: 10px;
    border: solid 3px #2A2E39;
    color: #C3E0E5;
    font-size: 25px;
    cursor: pointer;


}
</style>