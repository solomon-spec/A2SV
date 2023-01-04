var numbers =readline().split(" ");
var n = parseInt(numbers[0]);
var m = parseInt(numbers[1]);
var a = parseInt(numbers[2]);
 
if(n%a !==0){
    n+=(a-n%a)
}
if(m%a !==0){
    m+=(a-m%a)
}
var total = (n/a)*(m/a);
write(total);