
<html>
    <head>
        <title>datatypes in js</title>
    </head>
    <body>
        <h1>javascript datatypes</h1>
        <div id = "output"></div>
        <script>
            fnction show(text){
                document.getElementById("output").innerHtml+=text+"<br>";
                
            }
        </script>
    </body>
</html>
//1.string
let name="Raju";
console.log("student_name:",name);

//2.number
let Age = 24
console.log("student_Age:",Age);

//3.boolean
let isStudent=true;
console.log("boolean:",isStudent);

//4.undefined

let x;
console.log("undefined:",x);

//5.Null
let emptyvalue=null;
console.log("null:",emptyvalue);

//6.object

let person={
    student_name:"vasu",
    age:25
};
console.log("object:",person);

//7.array

let python=["pandas","numpy","matplotlib","django"];
console.log("array:",python);

//bigint
let bignumber=6446736538675646488463725222n;
console.log("bigint:",bignumber);
//9.symbol
let id=Symbol("mySymbol");
console.log("Symbol:",id);
