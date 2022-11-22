<template>

    <nav id="headBar">
        <div class="menu-item">Stocks</div>
        <div class="menu-item">Forex</div>
        <div class="menu-item">Commodities</div>
        <div class="menu-item">Crypto</div>
        <Dropdown title="Timeframe" :items="timeframes" />
    </nav>

</template>

<script>
import Dropdown from './Dropdown.vue';

export default {
    name: 'navBar',
    components: {
        Dropdown
    },
    data() {
        return {
            timeframes: [
                { title: 'Daily' },
                { title: 'Weekly' },
                { title: 'Monthly' },
                { title: 'Yearly' }
            ]
        }
    }

}



</script>

<style>
nav {
    width: 70vw;
    background-color: #131722; 
    display: flex;
    align-items: center;
    justify-content: left;
    border-radius: 10px;
    border: solid 3px #2A2E39;
}

nav .menu-item {
    color: #C3E0E5;
    padding: 25px 40px;
    position: relative;
    text-align: center;
    border-bottom: 5px solid transparent;
    display: flex;
    transition: 0.4s;

}

nav .menu-item.active,
nav .menu-item:hover {
    background-color: #131722; 
    border-bottom-color: #E3B844;
    cursor: pointer;
}

nav .menu-item a {
    color: inherit;
    text-decoration: none;
}

nav .menu-item:last-of-type{
    margin-left: auto;

}

</style>