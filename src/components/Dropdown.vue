<template>

    <div class="menu-item" @click="isOpen = !isOpen">
        <a>{{ title }}</a>
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-caret-down-fill"
            viewBox="0 0 16 16">
            <path
                d="M7.247 11.14 2.451 5.658C1.885 5.013 2.345 4 3.204 4h9.592a1 1 0 0 1 .753 1.659l-4.796 5.48a1 1 0 0 1-1.506 0z" />
        </svg>
        <transition name="fade" appear>
            <div class="sub-menu" v-if="isOpen">
                <div v-for="(item, i) in items" :key="i" class="menu-item">
                    <a @click="getTimeframe(item.title.toLowerCase())" >{{ item.title }}</a>
                </div>
            </div>
        </transition>
    </div>

</template>


<script>

//import { getData } from "../getData.js";
import { useTimeframeStore } from "../stores/timeframes.js"
import { storeToRefs } from 'pinia'

export default {
    name: 'dropDown',
    props: ['title', 'items'],
    data() {
        return {
            isOpen: false
        }
    },

    methods:{
        getTimeframe1(timeframe){
           console.log(timeframe)
           return timeframe
        }
    },

    setup() {


    const timeframeStore = useTimeframeStore();
    const { timeframe } = storeToRefs(timeframeStore)
    const { getTimeframe } = timeframeStore
    return { timeframeStore, timeframe, getTimeframe }

  },

}

</script>

<style>
nav .menu-item svg {
    margin-left: 10px;
}

nav .menu-item .sub-menu {
    position: absolute;
    background-color: #222;
    top: calc(100% + 5px);
    left: 50%;
    transform: translateX(-50%);
    width: max-content;
    z-index: 5;
    border-bottom-left-radius: 10px;
    border-bottom-right-radius: 10px;

}

.fade-enter-active,
.fade-leave-active{
    transition: all .5s ease-out;
}

.fade-enter,
.fade-leave-to{
    opacity: 0;
}


</style>