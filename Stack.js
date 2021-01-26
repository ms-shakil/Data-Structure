// stack data sturcture in javascript
var arr = ["shakil","main"]
define = 10
var top = 1
function Push(arr,top){
   if(top < define){
     var value = "shakil"
     arr.push(value)
     top+=1       

   }else{
       console.log("don't have space in list")
   }
   return arr
}
function Pop(arr,top){
    if (top >=0){
        console.log(arr[top])
        arr.pop()
        top -=1
    }else{
        console.log("don't have any data in this list")
    }
}
var inp = "remove"
if (inp =="add"){
    console.log(Push(arr,top))
}
else if(inp =="remove"){
    Pop(arr,top)
}