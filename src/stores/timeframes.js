import { defineStore } from "pinia";
import { ref } from "vue";


 export const useTimeframeStore = defineStore({
    id: 'timeframes',
    state: () => ({
        timeframe: ref("daily")


    }),

    actions: {
        getTimeframe(index) {
            //var element = document.getElementsByClassName('menue-item');
            var timeframe = index
            timeframe.trim();
            console.log(timeframe);
            console.log(typeof timeframe);
            return this.timeframe = timeframe;
        }
    }
}) 