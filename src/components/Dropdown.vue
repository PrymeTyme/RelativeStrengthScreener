<template>

    <div class="menu-item" @click="isOpen = !isOpen">
        <a>{{ title }}</a>
        <fa icon="angle-down" />
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
    background-color: #131722d5;
    top: calc(100% + 5px);
    left: 50%;
    transform: translateX(-50%);
    width: max-content;
    z-index: 5;
    border-bottom-left-radius: 10px;
    border-bottom-right-radius: 10px;
    border: 2px solid #E3B844 transparent;

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