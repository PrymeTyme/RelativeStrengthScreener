<template id="card">

    <div class="section">
        <div class="title" v-on:click="toggle">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16">
                <path fill-rule="evenodd"
                    d="M2 12.5a.5.5 0 0 1 .5-.5h11a.5.5 0 0 1 0 1h-11a.5.5 0 0 1-.5-.5zm0-3a.5.5 0 0 1 .5-.5h11a.5.5 0 0 1 0 1h-11a.5.5 0 0 1-.5-.5zm0-3a.5.5 0 0 1 .5-.5h11a.5.5 0 0 1 0 1h-11a.5.5 0 0 1-.5-.5zm0-3a.5.5 0 0 1 .5-.5h11a.5.5 0 0 1 0 1h-11a.5.5 0 0 1-.5-.5z" />
            </svg>

        </div>

        <div class="body" v-show="showSection">
            <div id="options">
                <div class="option" v-for="item in items" :key="item" @click="getOption(item.id)">{{ item.text }}
                    <div class="icon"><fa v-bind:icon="item.icon"/></div>
                </div>
                <div></div>
            </div>
        </div>
    </div>

</template>


<script>

import {useOptionStore} from '../stores/options.js'
import { storeToRefs } from 'pinia'

export default {
    name: 'CardTest',
    template: '#card',
    methods: {
        toggle() {
            this.showSection = !this.showSection
        },

        getOption1(item) {
            console.log(item)
            return item
        },
    },
    data() {
        return {
            showSection: false,
            items: [{ text: 'Open in Chart', icon: 'line-chart',id:'chart' }, { text: 'Show Sector Holdings', icon: 'list-dots',id:'show' }, { text: 'Add to Watchlist', icon: 'add',id:'add' }], // change to objects with value
        }
    },

    setup() {


    const optionStore = useOptionStore();
    const { option } = storeToRefs(optionStore)
    const { getOption } = optionStore
    return { optionStore, option, getOption }

},
}
</script>

<style>
.section {
    width: 50px;
    background: inherit;
    margin-bottom: 0px;
}

#toggle {
    display: block;
}

.body {
    left: 50%;
    transform: translateX(-100%);
    width: 320px;
    border-top: 2px solid #41729F;
    margin-left: 120%;
}

.body:hover {
    border-top: 2px solid #5885AF;
}

.option {
    text-align: left;
    margin-top: 2%;
    display: grid;
    grid-template-columns: 60% auto;
}

.option:hover {
    background: #5885AF;
    width: 320px;
    margin-top: 2%;
    text-align: left;
}

.icon{
    margin-left: 69%;
}

.icon:hover{
    color: black;
}

</style>
  