<template>

    <div class="menu-item" @click="isOpen = !isOpen">

        <div><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                viewBox="0 0 16 16">
                <path fill-rule="evenodd"
                    d="M2 12.5a.5.5 0 0 1 .5-.5h11a.5.5 0 0 1 0 1h-11a.5.5 0 0 1-.5-.5zm0-3a.5.5 0 0 1 .5-.5h11a.5.5 0 0 1 0 1h-11a.5.5 0 0 1-.5-.5zm0-3a.5.5 0 0 1 .5-.5h11a.5.5 0 0 1 0 1h-11a.5.5 0 0 1-.5-.5zm0-3a.5.5 0 0 1 .5-.5h11a.5.5 0 0 1 0 1h-11a.5.5 0 0 1-.5-.5z" />
            </svg>

            <transition name="fade" appear>
                <div class="sub-menu" v-if="isOpen">
                    <div v-for="(item, i) in items" :key="i" class="menu-item">
                        <a @click="getOption(item.title.toLowerCase())">{{ item.title }}</a>
                    </div>
                </div>
            </transition>
        </div>

    </div>

</template>

<script>

//import { getData } from "../getData.js";
import { useTimeframeStore } from "../stores/timeframes.js"
import { storeToRefs } from 'pinia'

export default {
    name: 'dropDownList',
    props: ['title', 'items'],
    data() {
        return {
            isOpen: false
        }
    },

    methods: {
        getOption(option) {
            console.log(option)
            return option
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
.icon {
    color: black !important;
    transition: 0.4s;
    border-left: 2px solid #41729F;
    background: #5885AF;
    justify-content: center;
    top: 0;
    width: 8%;
    height: 100%;
    position: absolute;
    margin-left: 290px;


}

.icon:hover {
    background-color: #5885AF !important;
    color: #C3E0E5 !important;
    transition: 0.4s;

}


.menu-item .sub-menu {
    position: absolute;
    background-color: #222;
    top: calc(100% + 5px);
    left: 50%;
    transform: translateX(-50%);
    width: max-content;
    z-index: 20;
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