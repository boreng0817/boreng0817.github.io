---
layout: post
title: "Kotlin with examples" 
date: 2021-07-06 03:18:55 -0700
categories: kotlin 
---
<h1>Kotlin Bootcamp for Programmers Lesson 1-3</h1> 

This article is a short(but quite long) summary that I newly learned on July 5-??, 2021 

Hello kotlin!
```kotlin
fun main() {	
    println("Hello, Kotlin!")
}
```
Code above is a simple function that prints "Hello, Kotlin!" as an output.
I learned Kotlin with various demo in [developer.android.com](https://developer.android.com/codelabs/kotlin-bootcamp-welcome#0) 
I'll cover lesson 1 through lesson 3.
![fig1](https://boreng0817.github.io/asset/TIL/2021-07-05/fig1.PNG) 

---

<h3><span style="color:DarkGreen">Lesson 1: Get started</span></h3>

<details><summary><h4>1.0 Introduction to kotlin</h4></summary><p>

In this lesson, we learn about the language **Kotlin** and install environment for the Kotlin.


**Kotlin** is focused on clarity, conciseness, and code safety.<br>
It has special property that you can use **Kotlin** with java. (e.g calling Java libraries in Kotlin)

The course suggest me to use intelliJ IDEA, but I used andriod studio's Kotlin REPL for codelab.

You can use **Tool > Kotlin > Kotlin REPL** to execute Kotlin REPL in your andriod studio.

</p></details> 

---

<h3><span style="color:DarkGreen">Lesson 2: Kotlin basics</span></h3>

<details><summary><h4>2.0 Operators and types</h4></summary>
<p>

For more readability, you can use _ (underscore) in number

```kotlin
val oneMillion = 1_000_000 // Ok
val socialSecurityNumber = 999_99_9999L // Ok
val hexBytes = 0xFF_EC_DE_5E // Ok
val bytes = 0b11010010_01101001 // Ok
val SomeVersion = 1_01_013_0102 // Ok
``` 

You can use var and val for declaring variable.

**var** is for changable (mutable) variables.<br>
**val** is for unchangable (immutabl) variables, like constant.

```kotlin
var fish = 1
fish = 2 // Ok
val aquarium = 1
aquarium = 2 // error : val cannot be reassigned
```

You can use " for making String in **Kotlin**. <br> 
You can replace a variable's value in some Strings with ```$ variable``` <br>
You can concatenate strings with ```+``` operation. <br>

```kotlin
val numOfFish = 5
val numOfPlants = 12
"I have $numOfFish fish" + " and $numOfPlants plants"

/*
    res: kotlin.String = I have 5 fish and 12 plants
*/
``` 

</p>
</details> 

---- 

<details><summary><h4>2.1 Compare Conditions and Booleans</h4></summary>
<p>

Like other programming language, **Kotlin** has booleans and boolean operators like ```<```, ```==```, ```>```, ```!=```, ```<=```, ```>=```.

You can use ```in``` for ranged comparison. 

```kotlin
val number = 5

if (number in 1..10) {
    println("number is in range 1 to 10!")
} else {
    println("number is not in range 1 to 10!")
}

/*
    number is in range 1 to 10!
*/
``` 

You can use ```when``` instead writing series of ```if```, ```else if```, ```else```. 

```kotlin 
val numberOfFish = 20

if (numberOfFish == 0) {
    println("Empty tank")
} else if (numberOfFish < 40) {
    println("Got fish!")
} else {
    println("That's a lot of fish")
}

// The same as above

when (numberOfFish) {
    0 -> println("Empty tank")
    in 1..39 -> println("Got fish!")
    else -> println("That's a lot of fish")
}
``` 

</p>
</details> 

---- 

<details><summary><h4>2.2 Learn about nullability</h4></summary> 
<p>

In **Kotlin**, there's non-nullable variables and nullable variables. <br> 
Literally, non-nullable variables can't be null. They make error when they are null. <br>
By default, variables are non-nullable. <br> 

```kotlin
var rocks: Int = null
// error: null can not be a value of a non-null type Int
``` 

When we add question mark operator ```?```, the variable can be null.

```kotlin
var marbles: Int? = null // Ok
``` 

You can test for ```null``` with ```?``` operator. 

```kotlin
var fishFoodTreats = 6

/* A */
if (fishFoodTreats != null) {
    fishFoodTreats = fishFoodTreats.dec() // decrease function. It returns var - 1
}

/* B */
fishFoodTreats = fishFoodTreats?.dec()
 
/*
    Result of A and B is the same.
    For B, fishFoodTreats becomes null when itself is null.
*/
``` 

You can use ```?:``` operator instead ```if```, ```else if``` in this case. 

```kotlin 
var fishFoodTreats = 6

/* A */
if (fishFoodTreats != null) {
    fishFoodTreats = fishFoodTreats.dec()
} else {
    fishFoodTreats = 0
}

/* B */
fishFoodTreats = fishFoodTreats?.dec() ?: 0

``` 

When you need to make ```NullPointerExceptions``` you can use ```!!``` operator.

```kotlin
val len = s!!.length

// throws NullPointerExceptions is s is null
```

</p>
</details> 

--- 

<details><summary><h4>2.3 Arrays, Lists, and Loops</h4></summary>
<p>

You can make list with ```listOf``` and ```mutableListOf```. 
List that is made with ```listOf``` can't be changed. It's immutable. But you can change a list made with ```mutableListOf``` 

```kotlin 
val school = listOf("mackerel", "trout", "halibut")
println(school)

/*
    [mackerel, trout, halibut]
*/

val myList = mutableListOf("tuna", "salmon", "shark") 
myList.remove("tuna")

/*
    kotlin.Boolean = true
*/

println(myList)

/*
    [salmon, shark]
*/

myList[1] = "Baby shark"
println(myList)

/*
    [salmon, Baby shark]
*/
``` 


Note that ```val``` and ```var``` work the same as before. <br>
You can't reassign value if you use ```val```. <br>


```kotlin

val list1 = listOf("element1", "element2")
list1 = listOf("element3", "element4")

/*
    error: val cannot be reassigned
    list1 = listOf("element3", "element4")
*/

var list2 = listOf("element1", "element2")
list2 = listOf("element3", "element4") // Ok
``` 

You can make array with ```arrayOf```.<br>
Element of array made with ```arrayOf``` can be anytype but not null.<br>
You can specify the type of arrays. Like `intArrayOf()`, `charArrayof()` 

Note that you can print array with `java.util.Arrays.toString()`.

```kotlin 
val school = arrayOf("gajami", "nong fish", "squid")
println(java.util.Arrays.toString(school)

/* 
    [gajami, nong fish, squid]
*/

val mix = arrayOf("fish", 2)

val numbers = intArrayOf(1, 2, 3)
``` 


You can concatenate arrays with `+` operator.

```kotlin 
val numbers1 = intArrayOf(1, 2, 3)
val numbers2 = intArrayOf(4, 5, 6)
val foo = numbers1 + numbers2

println(foo[2])

/*
    3
*/
``` 

You can store array in list. <br>
Note that strange `[I@...` is an array. 

```kotlin 
val numbers = intArrayOf(1, 2, 3)
val oceans = listOf("Atlantic", "Pacific")
val oddList = listOf(numbers, oceans, "salmon")

println(oddList)

/*
    [[I@89178b4, [Atlantic, Pacific], salmon]
     <-numbers>  <------oceans----->
*/

``` 



You can initialize arrays with code.  <br>
Initialization code is between curly bracket `{}` and `it` refers to the array index with 0 base.

```kotlin 
val array = Array (5) { it * 2 }
println(java.util.Arrays.toString(array))

/*
    [0, 2, 4, 6, 8]
*/

``` 

You can make loop with `for` keyword. 

```kotlin 
val appMaking = arrayOf("Making", "application", "is", "fun!")
for (element in appMaking) {
    print(element + " ")
}

/*
    Making application is fun!
*/
``` 

If you need loop with indexes, you can use `withIndex()` 

```kotlin 
for ((index, element) in appMaking.withIndex()) {
    print("Item at $index: $element\n)
}

/*
    Item at 0: Making
    Item at 1: application
    Item at 2: is
    Item at 3: fun!
*/

``` 

Some examples with `for` and `in` keyword.

```kotlin 
for (i in 1..5) print(i)
/*
    12345
*/

for (i in 5 downTo 1) print(i)
/*
    54321
*/

for (i in 3..6 step 2) print(i)
/*
    35
*/

for (i in 'd'..'g') print(i)
/*
    defg
*/

``` 

Also, you can use `while` and `do...while` loops, and `++` and `--` work as well. <br>
Kotlin has `repeat` loop. 

```kotlin 
var bubbles = 0
while (bubles < 50) {
    bubbles++
}
println("$bubbles bubbles in the water\n")

do {
    bubbles--
} while (bubbles > 50)
println("$bubbles bubbles in the water\n")

repeat(2) {
    println("A fish is swimming")
}

/*
    50 bubbles in the water
    49 bubbles in the water
    A fish is swimming
    A fish is swimming
*/ 
``` 

</p>
</details> 

--- 


<h3><span style="color:DarkGreen">Lesson 3: Functions</span></h3> 

<details><summary><h4>3.0 Explore the main() function</h4></summary><p> 
<p>

Here's a simple code that prints `Hello world`.

```kotlin 
fun printHello() {
    println ("Hello world")
}

printHello()

/*
    Hello world
*/
``` 

You can define functions with `fun` keyword. <br>
Similar with other languages, you define function arguments in `()` and write code in curly bracket `{}`.

As with other languages, the kotlin `main()` function specifies the entry point for execution. <br>
Our main function return nothing, and print a simple message to the screen. <br>
Bascially you should use `args: Array<String>` for the argument of main, but after **Kotlin 1.3**, you can skip adding parameter for main.

```kotlin 
fun main(args: Array<String>) {
    println("Hello, world!")
}

/* This also works after kotlin 1.3 */
fun main() {
    println("Hello, world!")
}
``` 

Let's try giving command line argument to `main` function. <br>
If you use **IntelliJ IDEA** for kotlin, you can give argument with this procedure.
1. select **Run > Edit Configurations**
2. In **Run/Debug Configurations** window, you can type arguments in **Program arguments** field.
3. Click **Ok**

```kotlin 
/* Assume that we gave "Kotlin!" as a command line argument. */
fun main(args: Array<String>) {
    println("Hello, ${args[0]}")
}

/*
    Hello, Kotlin!
*/
```
</p>
</details>

--- 

<details><summary><h4>3.1 Learn why (almost) everything has a value</h4></summary> 
<p>

In kotlin, almost everyting is value. <br>
Here's a simple print statement. Even this print statement is a value.

```kotlin 
val isUnit = println("This is an expression")
println(isUnit)

/*
    This is an expression
    kotlin.Unit
*/
``` 

Also, a `if` expression is a value.

```kotlin 
val temperature = 10
val isHot = if (temperature > 50) true else false

println(isHot)

/*
    false
*/

``` 

You can plug `if` expression directly into string template.

```kotlin 
val temperature = 10
val message = "The water temperature is ${ if (temperature > 50) "too warm" else "OK" }."
println(message)
``` 

/*
    The water temperature is OK.
*/

</p>
</details>

--- 

<details><summary><h4>3.2 Learn more about functions</h4></summary> 
<p>

Here's a function `feedTheFish()` that calls `randomDay()`. 

```kotlin 
fun feedTheFish() {
    val day = randomDay()
    val food = "pellets"
    println ("Today is $dat and the fish eat $food")
}

fun main(args: Array<String>) {
    feedTheFish()
}
``` 

And `randomDay()` function is implemented as below. <br>
You should import `java.util.*` for using `Random().nextInt(size: Int)`.

```kotlin
import java.util.*

// It returns a String
fun randomDay() : String {
    val week = arrayOf (arrayOf ("Monday", "Tuesday", "Wednesday", "Thursday",
            "Friday", "Saturday", "Sunday")
    return week[Random().nextInt(week.size)]
}
``` 

It Simply returns a random day in String.

We get an output as
```kotlin
/*
    Today is Tuesday and the fish eat pellets
*/
``` 

Let's upgrade our function for variety of food. <br>
We add `fishFood(day: String)` and modify `feedTheFish()` a bit.

```kotlin
fun fishFood (day : String) : String {
    var food = ""
    when (day) {
        "Monday" -> food = "flakes"
        "Tuesday" -> food = "pellets"
        "Wednesday" -> food = "redworms"
        "Thursday" -> food = "granules"
        "Friday" -> food = "mosquitoes"
        "Saturday" -> food = "lettuce"
        "Sunday" -> food = "plankton"
    }
    return food
}

fun feedTheFish() {
    val day = randomDay()
    val food = fishFood(day)

    println ("Today is $day and the fish eat $food")
}

/* output of main
    Today is Thursday and the fish eat granules
*/
```

We can add default branch for `when` expression with `else` keyword. <br>
For `Tuesday` and `Saturday`, the fish would eat nothing.

```kotlin
fun fishFood (day : String) : String {
    val food : String
    when (day) {
        "Monday" -> food = "flakes"
        "Wednesday" -> food = "redworms"
        "Thursday" -> food = "granules"
        "Friday" -> food = "mosquitoes"
        "Sunday" -> food = "plankton"
        else -> food = "nothing"
    }
    return food
}
``` 

We an ensure that `food` doesn't have to be assigned again. <br>
So, we an ommit variable food.

```kotlin
fun fishFood (day : String) : String {
    return when (day) {
        "Monday" -> "flakes"
        "Wednesday" -> "redworms"
        "Thursday" -> "granules"
        "Friday" -> "mosquitoes"
        "Sunday" -> "plankton"
        else -> "nothing"
    }
}
``` 

So, the final version of our code is

```kotlin
import java.util.*    // required import

fun randomDay() : String {
    val week = arrayOf ("Monday", "Tuesday", "Wednesday", "Thursday",
        "Friday", "Saturday", "Sunday")
    return week[Random().nextInt(week.size)]
}

fun fishFood (day : String) : String {
    return when (day) {
        "Monday" -> "flakes"
        "Wednesday" -> "redworms"
        "Thursday" -> "granules"
        "Friday" -> "mosquitoes"
        "Sunday" -> "plankton"
        else -> "nothing"
    }
}

fun feedTheFish() {
    val day = randomDay()
    val food = fishFood(day)
    println ("Today is $day and the fish eat $food")
}

fun main(args: Array<String>) {
    feedTheFish()
}
``` 


</p>
</details>

--- 

<details><summary><h4>3.3 Explore default values and compact functions</h4></summary> 
<p>

You can set default value for function arguement. <br>

```kotlin 
fun swim(speed: String = "fast") {
   println("swimming $speed")
}
```

For function `swim`, parameter `speed` is set to be `"fast"` unless you give argument for the function.

```kotlin
swim()   // uses default speed
swim("slow")   // positional argument
swim(speed="turtle-like")   // named parameter

/*
    swimming fast
    swimming slow
    swimming turtle-like
*/
``` 

You can mix with **required parameters** and parameter with defualt value. (e.g `speed` in the previous example)

```kotlin
fun shouldChangeWater (day: String, temperature: Int = 22, dirty: Int = 20): Boolean {
    return when {
        temperature > 30 -> true
        dirty > 30 -> true
        day == "Sunday" ->  true
        else -> false
    }
}
```

`temperature` and `dirty` have default arguments. But `day` don't. So we need to pass a value for `day`.

```kotlin 
// Code from previous section 3.2
fun feedTheFish() {
    val day = randomDay()
    val food = fishFood(day)
    println ("Today is $day and the fish eat $food")
    println("Change water: ${shouldChangeWater(day)}")
}

/*
    Today is Thursday and the fish eat granules
    Change water: false
*/
``` 

There's a compact functions that make your code more concise and readable. It's also called as _single-expressed_ functions.

```kotlin
fun isTooHot(temperature: Int) = temperature > 30

fun isDirty(dirty: Int) = dirty > 30

fun isSunday(day: String) = day == "Sunday"
```

We can change `shouldChangeWater()` function with these compact functions

```kotlin 
fun shouldChangeWater (day: String, temperature: Int = 22, dirty: Int = 20): Boolean {
    return when {
        isTooHot(temperature) -> true
        isDirty(dirty) -> true
        isSunday(day) -> true
        else  -> false
    }
}
```

Note that **defulat value** doesn't have to be a value. You can assing a function call to parameter.

```kotlin 
// getDirtySensorReading() is a function that returns Int.
fun shouldChangeWater (day: String, temperature: Int = 22, dirty: Int = getDirtySensorReading()): Boolean {
    ...
``` 

</p>
</details>

--- 

<details><summary><h4>3.4 Get started with filters</h4></summary> 
<p>

Filters are a handy wat to get sublist based on some condition.

You can make a sublist from `decorations` that every element of sublist starts with `'p'`

```kotlin
val decorations = listOf ("rock", "pagoda", "plastic plant", "alligator", "flowerpot")

println( decorations.filter {it[0] == 'p'})

/*
    [pagoda, plastic plant]
*/
``` 

There's `eager` and `lazy` filters in kotlin and other programming language. The big difference between `eager` and `lazy` is the time of the result is created. `eager` filter calculates filtered list immediately when you use filter, but `lazy` filter cacluate when you access (simply when you need a value from list) to list's element.

```kotlin
fun main() {
    val decorations = listOf ("rock", "pagoda", "plastic plant", "alligator", "flowerpot")

    // eager, creates a new list
    val eager = decorations.filter { it [0] == 'p' }
    println("eager: $eager")

    // lazy, will wait until asked to evaluate
    val filtered = decorations.asSequence().filter { it[0] == 'p' }
    println("filtered: $filtered")

    // force evaluation of the lazy list
    val newList = filtered.toList()
    println("new list: $newList")
}

/*
    eager: [pagoda, plastic plant]
    filtered: kotlin.sequences.FilteringSequence@386cc1c4
    new list: [pagoda, plastic plant]
*/
``` 

For visualization of lazy evaluation, you can use `map()` function. <br>
_Example will be added_

</p>
</details>

--- 

<details><summary><h4>3.5 Get started with lambdas and higher-order functions</h4></summary> 
</details>
<p>

A lambda is an expression that makes a function. Instead of declaring a named function, you declare a function that has no name. This makes lambda expression can now be passed as data.

You can give parameters to lambda. `->` is a function arrow, and parameters go on the left of `->`. The code to execute goes right of the fuction arrow. When you assign lambda to a variable, you can use the name of that vairable like function.

```kotlin 
var dirtyLevel = 20
val waterFilter = { dirty : Int -> dirty / 2}
println(waterFilter(dirtyLevel))

/*
    10
*/
```

In this examle, lambda takes an `Int` named `dirty`, and return half of `dirty`.

It is nicer to declare a function type. (returns `Int`)
```kotlin 
val waterFilter: (Int) -> Int = { dirty -> dirty / 2 }
```

Higher order <br>
TO-DO

</p>
</details>

--- 

<h3><span style="color:DarkGreen">Lesson 4: Classes and Objects</span></h3> 

<details><summary><h4>4.0 Create a class</h4></summary> 
<p>

You can make classes with `class` keyword.

```kotlin
class Aquarium {
    var width: Int = 20
    var heigth: Int = 40
    var length: Int = 100
}
``` 

In kotlin, `getters` and `setters` are automactically created. You can get and set variables in `Aquarium` class like `Aquarium.width = 10`, `println(Aquarium.width)`

Note that declaring properties of class with `val` and `var` is different. Once you declare variable with `val`, probably every instance of the class have the same value(unless it can be initialized with parameter).

You can add some methods inside a class.

```kotlin
class Aquarium {
    var width: Int = 20
    var heigth: Int = 40
    var length: Int = 100

    fun printSize() {
        println("Width: $width cm " +
                "Length: $length cm "+
                "Height: $height cm ")
    }
}


val aquarium = Aquarium()
aquarium.printSize()

/*
    Width: 20 cm Length: 100 cm Height: 40 cm
*/
``` 

</p>
</details>

--- 

<details><summary><h4>4.1 Add class constructors</h4></summary> 
<p>

In some programming language, the constructor is defined by creating a method named the same as class name.<br>
In kotlin, constructor is defined in class declaration.

```kotlin
class Aquarium(length: Int = 100, width: Int = 20, height: Int = 40) {
   // Dimensions in cm
   var length: Int = length
   var width: Int = width
   var height: Int = height
...
}
``` 

You can simplify constructor with `var` and `val`. For property definition inside `{}` curly bracket, you can write them in `()` bracket.

```kotlin
class Aquarium(var length: Int = 100, var width: Int = 20, var height: Int = 40) {
...
}
``` 

These are some example of constructor of `Aquarium`.<br>
Note that all properties in `Aquarium` have default value.

<codeBlock href="#init"></codeBlock>
```kotlin
val aquarium1 = Aquarium()
aquarium1.printSize()

// default height and length
val aquarium2 = Aquarium(width = 25)
aquarium2.printSize()

// default width
val aquarium3 = Aquarium(height = 35, length = 110)
aquarium3.printSize()

// everything custom
val aquarium4 = Aquarium(width = 25, height = 35, length = 110)
aquarium4.printSize()

/*
    Width: 20 cm Length: 100 cm Height: 40 cm 
    Width: 25 cm Length: 100 cm Height: 40 cm 
    Width: 20 cm Length: 110 cm Height: 35 cm 
    Width: 25 cm Length: 110 cm Height: 35 cm 
*/
```
One nice thing about kotlin constructors is that you don't have to overload for different version of constructors.

In many programming language, you can do some stuffs in constructor like print some message. When you need some specific task in class' constructor, you can use `init` block. <br>
Note that you can use multiple `init` blocks.

```kotlin
class Aquarium (var length: Int = 100, var width: Int = 20, var height: Int = 40) {
    init {
        println("aquarium initializing")
    }
    init {
        // 1 liter = 1000 cm^3
        println("Volume: ${width * length * height / 1000} l")
    }
}
``` 

```kotlin
val aquarium1 = Aquarium()
aquarium1.printSize()

// default height and length
val aquarium2 = Aquarium(width = 25)
aquarium2.printSize()

// default width
val aquarium3 = Aquarium(height = 35, length = 110)
aquarium3.printSize()

// everything custom
val aquarium4 = Aquarium(width = 25, height = 35, length = 110)
aquarium4.printSize()

/*
    aquarium initializing
    Volume: 80 l
    Width: 20 cm Length: 100 cm Height: 40 cm
    aquarium initializing
    Volume: 100 l
    Width: 25 cm Length: 100 cm Height: 40 cm
    aquarium initializing
    Volume: 77 l
    Width: 20 cm Length: 110 cm Height: 35 cm
    aquarium initializing
    Volume: 96 l
    Width: 25 cm Length: 110 cm Height: 35 cm
*/
```

Examine the difference between this [code](#init)

Also if you need another version of constructors, you can define secondary constructor as well. <br>
You can use `constructor` keyword for the secondary constructors.

```kotlin
class Aquarium (var length: Int = 100, var width: Int = 20, var height: Int = 40) {
    init {
        println("aquarium initializing")
    }
    init {
        // 1 liter = 1000 cm^3
        println("Volume: ${width * length * height / 1000} l")
    }
    constructor(numberOfFish: Int) : this() {
        // 2,000 cm^3 per fish + extra room so water doesn't spill
        val tank = numberOfFish * 2000 * 1.1
        // calculate the height needed
        height = (tank / (length * width)).toInt()
    }
}

val aquarium6 = Aquarium(numberOfFish = 29)
aquarium6.printSize()
println("Volume: ${aquarium6.width * aquarium6.length * aquarium6.height / 1000} l")

/*
    aquarium initializing
    Volume: 80 l
    Width: 20 cm Length: 100 cm Height: 31 cm 
    Volume: 62 l
*/
```

You can add new property getter. 

```kotlin
// in Aquarium
val volume: Int
    get() = width * height * length / 1000 

fun printSize() {
    println("Width: $width cm " +
            "Length: $length cm " +
            "Height: $height cm "
    )
    // 1 l = 1000 cm^3
    println("Volume: $volume l")
}
```

Also, you can add a property setter.
```kotlin
// in Aquarium
val volume: Int
    get() = width * height * length / 1000 
    set(value) {
        heigth = (value * 1000) / (width * length)
    }
```

</p>
</details>

--- 

<details><summary><h4>4.2 Learn about visibility modifiers</h4></summary> 
<p>
</details>

TO-DO

</p>
</details>

--- 

<details><summary><h4>4.3 Compare abstract classes and interfaces</h4></summary>
<p>
</details>

TO-DO

</p>
</details>

--- 

<details><summary><h4>4.4 Use interface delegation</h4></summary> 
<p>
</details>

TO-DO

</p>
</details>

--- 

<details><summary><h4>4.5 Create a data class</h4></summary> 
<p>
</details>

TO-DO

</p>
</details>

--- 

<details><summary><h4>4.6 Learn about singletons, enums, and sealed classes</h4></summary> 
<p>
</details>

TO-DO

</p>
</details>

--- 

