---
layout: post
title: "Kotlin problem solving week3" 
date: 2021-07-25 17:55:00 -0700
categories: kotlin 
---
<h1>PS using kotlin</h1> 

2주차 백준 풀이입니다.

1259번 펠린드롬수와 18111번 마인크래프트 문제를 풀었는데, <br>
마인크래프트 문제를 풀면서 생긴 TLE(Time Limit Exceeded), <br>
시간초과에 대해 잠깐 짚고 넘어가려고 합니다.

PS를 할 때 문제에는 대부분 시간제한이 있습니다. <br>
맞는 답을 내는 코드를 제출해도 문제 해결에 시간이 오래 걸리면 채점 프로그램은 제출한 코드를 틀렸다고 판단합니다. <br>
18111번 문제를 처음에는 list를 이용하여 구현했는데, 연산량을 얼추 계산했을 때 1초면 충분하겠다고 생각했으나, <br>
채점 프로그램은 1초 채점을 하고 TLE를 뱉었습니다.

연산량 계산에 앞서 문제를 어느 정도 이해를 해야 합니다.<br>
이 문제는 m, n 2차원 지역에 블록들이 쌓여있는 지역을 평평하게 하는데<br>
최소 얼마의 시간이 걸리고, 그때 높이는 얼마인지 구하는 문제입니다.<br>
* 이때, (i, j)칸에 있는 블록을 하나 깨서 주머니에 넣을 때는 2초가 걸립니다.<br>
* 블록을 (i, j)칸에 쌓는 데 1초가 걸립니다.
m, n은 1과 500 사이의 정수이고,<br>
(i, j)에 블록은 최소 0개, 최대 256개까지 쌓을 수 있습니다.<br>


입력이 이럴 때, 블록은 이렇게 있습니다.
![fig2](https://boreng0817.github.io/asset/TIL/2021-07-25/fig2.PNG)

설명은 여기까지 하고, 제가 구현한 코드에서 이 부분이 가장 오래 걸리는데
```kotlin
...
    for (level in minOfList..maxOfList) {
        var dig = 0
        var put = 0
        for (element in blockList) {
           if (element > level)
               dig += element - level
            else
                put += level - element
        }

        if (dig + blocks - put >= 0) {
            val time = dig*2 + put
            if (min >= time) {
                min = time
                floor = level
            }
        }
    }
...
```

입력으로 들어온 블록의 개수가 최대 500x500, 250_000이고, <br>
이 중 한 칸에 256개의 블록이, 그리고 다른 한 칸에 0칸의 블록이 있다면<br>
높이를 0부터 256까지 모두 체크해줘야 하니, 대충 250_000 x 257 x ${for 내부의 코드 연산 수} 정도가 됩니다.<br>
for문 내부 연산의 횟수를 넉넉잡아서 10정도로 잡으면 약 6억정도가 됩니다.<br>
이전에 C 혹은 C++로 PS를 했을 때는 1초는 대략 10억번 정도 연산을 할 수 있다!라는 것을 머리에 넣고 코딩을 하곤 했는데,<br>
자바나 파이썬은 보통의 경우 1천만, 최대 1억회까지 연산을 할 수 있다고 합니다.<br>
이는 컴퓨터의 환경, 사용하는 연산의 종류 등에 따라 굉장히 다르지만, 아무튼 코틀린은 자바를 기반으로 하니 6억번은 어림도 없다는 것을 깨달았습니다.<br>

그래서 list를 array로 컴팩트하게 하는 작업을 추가하여, 1초 시간제한에 0.984초가 걸려,, 아슬아슬하게 답에 통과했답니다.<br>
![fig1](https://boreng0817.github.io/asset/TIL/2021-07-25/fig1.PNG)

1259번 펠린드롬수는 비교적 간단한 문제니, 설명은 생략하겠습니다!<br>
풀이에 살짝 언급하면, string의 절반씩 직접 비교하는 코드를 처음 구현하고,<br>
String.reversed() 메소드를 이용하여 더 간단하게 구현하여 둘 다 pass를 받았습니다.<br>
물론 시간상으로는 String method를 사용하는 후자의 경우가 살짝 더 오래 걸렸습니다.<br>

저번 주에는 난이도가 쉬웠지만 그래도 5문제를 풀었는데, 이번 주는 2문제만 풀었네요..
개수를 더 늘려보도록 하겠습니다 :D 읽어주셔서 감사합니다!

1259 [펠린드롬수](https://www.acmicpc.net/problem/1259)

<details><summary>code</summary>

```kotlin
fun main(args: Array<String>) {
    while (true) {
        val str = readLine()!!
        var isPel = true

        // Check for exit condition [input is 0]
        if (str == "0")
            break

        // Check first half is the same as reversed second half
        // Ex 12321
        //    ^^ ^^
        //    |   \__*second half -> reversed
        //     \__*first half
        for (i in 0..(str.length - 1) / 2) {
            if (str[i] != str[str.length - 1 - i]) {
                isPel = false
                break
            }
        }
        println("${if (isPel) "yes" else "no"}")
    }
}
```


```kotlin
// Simpler version
fun main(args: Array<String>) {
    while (true) {
        val str = readLine()!!
        if (str == "0")
            break
        println("${if (str == str.reversed()) "yes" else "no"}")
    }
}
```
</details>

---

18111 [마인크래프트](https://www.acmicpc.net/problem/18111)

<details><summary>code</summary>

```kotlin
// get a line and make as list<Int>
fun readInts() = readLine()!!.split(" ").map { it.toInt() }

//  m, _, blocks
// get input m, n, and the number of blocks in inventory. 
// n is actually needless in this code. 
//  blockList
// get first row of blocks. [blockList] is initialized as kotlin.list<Int> 
//  blockArray
// Collect the number of level in [blockList]
// blockArray[level] --> the number of level in blockList
//  min
// min is initialized as max value of int
//  floor
// store a level that makes minimum cost
fun main(args: Array<String>) {
    val (m, _, blocks) = readInts()
    var blockList = readInts()
    val blockArray = IntArray(260) { 0 }
    var min = Int.MAX_VALUE
    var floor = 0

    // Make 2d array into flat list.
    for (i in 1..(m - 1))
        blockList += readInts()

    // build blockArray from blockList
    for (num in blockList)
        blockArray[num] += 1

    // Get min and max from blockArray
    var maxOfArray = -1
    var minOfArray = -1
    for (i in 0..256) {
        if (minOfArray == -1 && blockArray[i] != 0)
            minOfArray = i
        if (blockArray[i] != 0)
            maxOfArray = i
    }

    // Calculate cost for each level between minOfList and maxOfList
    for (level in minOfArray..maxOfArray) {
        var dig = 0
        var put = 0
        for (i in 0..maxOfArray) {
            if (i > level)
                dig += (i - level) * blockArray[i]
            else
                put += (level - i) * blockArray[i]
        }

        if (dig + blocks - put >= 0) {
            val time = dig*2 + put
            if (min >= time) {
                min = time
                floor = level
            }
        }
    }
    println("$min $floor\n")
}
```

Wrong (TLE)
```kotlin
// get a line and make as list<Int>
fun readInts() = readLine()!!.split(" ").map { it.toInt() }

//  m, _, blocks
// get input m, n, and the number of blocks in inventory. 
// n is actually needless in this code. 
//  blockList
// get first row of blocks. [blockList] is initialized as kotlin.list<Int> 
//  min
// min is initialized as max value of int
fun main(args: Array<String>) {
    val (m, _, blocks) = readInts()
    var blockList = readInts()
    var min = Int.MAX_VALUE
    var floor = 0

    // Make 2d array into flat list.
    for (i in 1..(m - 1))
        blockList += readInts()

    // Get min and max from blockList
    val maxOfList = blockList.maxOrNull()!!
    val minOfList = blockList.minOrNull()!!

    // Calculate cost for each level between minOfList and maxOfList
    for (level in minOfList..maxOfList) {
        var dig = 0
        var put = 0
        for (element in blockList) {
           if (element > level)
               dig += element - level
            else
                put += level - lement
        }

        if (dig + blocks - put >= 0) {
            val time = dig*2 + put
            if (min >= time) {
                min = time
                floor = level
            }
        }
    }

    println("$min $floor\n")

}
```
</details>

---
