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
                <div class="option" v-for="item in items" :key="item"  @click="getOption(item)" >{{ item }}</div>
            </div>
        </div>
    </div>
</template>


<script>
export default {
    name: 'CardTest',
    template: '#card',
    methods: {
        toggle() {
            this.showSection = !this.showSection
        },

        getOption(item) {
            console.log(item)
        },
    },
    data() {
        return {
            showSection: false,
            items:['Open in Chart','Open Stocks of Sector','Add to Watchlist'],
            openInChart: 'Open in Chart',
            openStockList: 'Open Stocks of Sector', // add variable
            addToWatchlist: 'Add to Watchlist',
        }
    }
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
}

.option:hover {
    background: #5885AF;
    width: 320px;
    margin-top: 2%;
    text-align: left;
}

</style>
  