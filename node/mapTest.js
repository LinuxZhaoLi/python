//1  去掉偶数
// var arr = [1,2,3,4,5,6,7,8]
// var r = arr.filter(function(x){
// 	return x % 2 !== 0;
// });

// console.log(r)

// 2 去掉空字符  filter() 高阶函数
// var arr = ['A','','B',null,undefined,'C']

// var r = arr.filter(function(s){
// return s && s.trim(); 
// })
// console.log(r)
//3 接收回调函数
// var arr = ['a','B','C']
// var r = arr.filter(function(element,index,self){
// console.log(element);
// console.log(index);
// console.log(self);
// return true;

// })
// 4 去除重复元素
'use strict'
//var r,arr = ['apple','starwberry','banana','pear','apple','orange','orange','starwberry'];
//去除重复元素依靠的是indexOf总是返回第一个元素的位置，后续的重复元素位置与indexOf返回的位置不相等，因此被filter滤掉了。
// r = arr.filter(function(element,index,self){
// 	console.log(self.indexOf(element),index);
// 	console.log(self.indexOf(element) === index); 
//    return self.indexOf(element) === index;

// });

// console.log(arr.filter([true,true,true,false,false,false,true])) //运行错误
// console.log(r.toString());
// 5 求素数
// function get_primes(arr){  //[]
	
// 	return arr.filter(function(element){
// 		var flag=true;
// 		if(element<2)
// 		{
// 			flag=false;
// 		}
// 		else{
// 			for(var i=2;i<element;i++)
// 			{
// 				if(element%i===0){
// 					flag=false;
// 				break;
// 							}
// 			}
// 	}
// 	return flag;
// })
// }

// var x,r,arr=[];
// for(x=1;x<100;x++){
// 	arr.push(x);
// }
// r = get_primes(arr)
// console.log(r.toString())

