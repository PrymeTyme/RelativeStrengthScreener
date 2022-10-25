<template>

    <nav id="headBar">
        <div class="menu-item">Stocks</div>
        <div class="menu-item">Forex</div>
        <div class="menu-item">Commodities</div>
        <div class="menu-item">Crypto</div>
        <div class="menu-item">Timeframe</div>
    </nav>

</template>

<script>
export default {
    name: 'navBar'
}

</script>

<style>
nav {
    width: 70vw;
    background-color: #0d0d0e;
    display: flex;
    align-items: center;
    justify-content: left;
    border-radius: 10px;
    border: solid 3px #41729F;
}

nav .menu-item {
    color: #FFF;
    padding: 25px 40px;
    position: relative;
    text-align: center;
    border-bottom: 5px solid transparent;
    display: flex;
    transition: 0.4s;
}

nav .menu-item.active,
nav .menu-item:hover {
    background-color: #0d0d0e;
    border-bottom-color: #bb3030;
}

nav .menu-item a {
    color: inherit;
    text-decoration: none;
}

nav div:last-of-type{
    margin-left: auto;
}

</style>