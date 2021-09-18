const app = Vue.createApp({
	data() {
		return {
			'title' : 'World',
			'value' : 1
		}
	},
	methods: {
		ajouter(increment) {
			this.value += increment
		}
	}
})

app.mount('#app')

