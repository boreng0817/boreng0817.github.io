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
</details>
<p>

TO-DO

</p>
</details>

