import { defineStore } from "pinia";
import { ref } from "vue";


export const useOptionStore = defineStore({
    id: 'options',
    state: () => ({
        option: ref("")


    }),

    actions: {
        getOption(option) {
            console.log(option)
            return this.option = option;
        }
    }
}) 