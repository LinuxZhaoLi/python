.pragma library

var scope = {
  add:  function(a,b)
    {
        return a+b;
    }
}

function call(msg) {
    var exp = msg.toString();
    console.log("输入的表达式：",exp)
    var data = {
        expression : msg
    }
    console.log("临时变量 data",JSON.stringify(data,null,2))
    try {
        var fun = new Function('return (' + exp + ');');

        console.log("fun 类型",fun)
        data.result = JSON.stringify(fun.call(scope), null, 2)
    } catch(e) {
        console.log("异常")
        data.error = e.toString();
        data.result = e.toString();
    }


    return data;
}


var name = '小王',age = 17
var obj = {
    name: "obj",
    objAge: this.age,
    myFun: function(){
    console.log(this.name + "年龄" + this.age)
    }

//    var myFun2 = function(fm,t){
//    console.log(this.name + "年龄" + this.age + "来自" + fm + "去往"+ t );
//    }

}
var obj2 = {

    name: "obj2",
    objAge: this.age,
    myFun3: function(fm,t){
    console.log(this.name + "年龄" + this.age + "来自" + fm + "去往"+ t );
    }
//    add: function(fm,t){
//    console.log(this.name + "年龄" + this.age + "来自" + fm + "去往"+ t );
//    }
}

var db = {
    name: "obj1",
    age: 99
}

function test(){

    console.log("test1",obj.objAge);
    obj.myFun()
    console.log("test2")
    obj.myFun.call(db);　　　　// 德玛年龄 99
    obj.myFun.apply(db);　　　 // 德玛年龄 99
    obj.myFun.bind(db)();　　　// 德玛年龄 99

    console.log("test3")
    obj2.myFun3.call(db,"上海","成都")
//    obj2.add.bind(db,"上海","成都")()


    return ;
}



