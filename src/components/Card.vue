<template id="card">

    <div class="section">
        <div class="title" v-on:click="toggle">
            <fa icon="angle-down"  class="arrow-down" v-show="!showSection"/>
            <fa icon="angle-down" flip="vertical" class="arrow-down" v-show="showSection"/>
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

<style scoped>
.section {
    width: 50px;
    background: inherit;
    margin-bottom: 0px;
    transition: 0.4s;
}

#toggle {
    display: block;
}

.body {
    left: 50%;
    transform: translateX(-100%);
    width: 320px;
    border-top: 2px solid #2A2E39 transparent;
    margin-left: 120%;
}

.body:hover {
    border-top: 2px solid #131722 transparent;
}

.option {
    text-align: left;
    margin-top: 2%;
    display: grid;
    grid-template-columns: 60% auto;
}

.option:hover{
    width: 320px;
    margin-top: 2%;
    text-align: left;
    color: #E3B844;

}

.icon{
    margin-left: 69%;
}

.icon:hover{
    color: #E3B844;
}


.arrow-down:hover{
    color: #E3B844;
}


</style>
  