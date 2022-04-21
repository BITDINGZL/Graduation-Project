var app = new Vue({
	el:"#app",
	data:{
		temp:[
			batchsize='',
			epochs='',
			lr='',
			decay=''
		],
		temp2:[
			age='',
			bf='',
			hz='',
			jl='',
			tj='',
			dc='',
			yz='',
			mb='',
			eeg=''
		],
		res:''
	},
	methods:{
		trainLB:function(){
			var that = this;
			axios.post('http://localhost:5000/trainFederated',{
				batchsize:that.temp.batchsize,
				epochs:that.temp.epochs,
				lr:that.temp.lr,
				decay:that.temp.decay
			})
			.then(function(response){
				console.log(response);
				that.res = response.data;
			},function(err){})
		},
		trainNN:function(){
			var that = this;
			axios.post('http://localhost:5000/trainNeuralNetwork',{
				batchsize:that.temp.batchsize,
				epochs:that.temp.epochs,
				lr:that.temp.lr,
				decay:that.temp.decay
			})
			.then(function(response){
				console.log(response);
				that.res = response.data;
			},function(err){})
		},
		test:function(){
			var that = this;
			axios.post('http://localhost:5000/test',{
				age:that.temp2.age,
				bf:that.temp2.bf,
				hz:that.temp2.hz,
				jl:that.temp2.jl,
				tj:that.temp2.tj,
				dc:that.temp2.dc,
				yz:that.temp2.yz,
				mb:that.temp2.mb,
				eeg:that.temp2.eeg
			})
			.then(function(response){
				console.log(response);
				if(response.data.length==0||response.data=='None'){
					alert('建议不用服药，继续保持哟')
				}
				else{
					alert('建议服用：'+response.data);
				}
			},function(err){})
		},
	}
})