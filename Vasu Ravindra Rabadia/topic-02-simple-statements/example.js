console.log("hello\n");

d = [1, 2, 3]
z = 12

function x(n) {
    console.log(d);
    d[2] = 99;
    console.log(d);
    return d
}

function f(n) {
    console.log(z);
    z = 55;
    console.log(z);
    return z
}

console.log("result=", x(3))
x(3)[2] = 88
console.log(d)

console.log("f(3)=", f(3))
f(3) = 77
console.log(z)