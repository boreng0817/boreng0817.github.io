---
layout: post
title: "Kotlin problem solving week1" 
date: 2021-07-19 21:52:00 -0700
categories: kotlin 
---
<h1>PS using kotlin</h1> 
약간 딴 길로 샌 느낌이 있지만,, <br>
kotlin을 익히려고 백준을 조금 풀어보았습니다! <br>
비교적 간단한 문제들이니 설명은 넘어가려고 합니다.

다만, command line 입출력과 관련하여 한 가지만 짚고 가면 좋을 것 같아 이 부분만 언급하도록 해보겠습니다.

출력은 간단하게 `print` 혹은 `println`함수를 사용하면 간단합니다.

입력은 다양한 방법이 있지만, 간결하고 쉬운 방법을 소개하려고 합니다.
```kotlin
val listOfInput = readLine()!!.split(' ').map { it.toInt() }
```

복잡하게 생겼지만, 한 줄씩 나누어 보면 생각보다 간단합니다.

```kotlin
// input -> 5 6 8 1 7
val listOfInput = readLine()!! // 입력 한 줄을 받습니다. 아직까지는 string 형태입니다. "5 6 8 1 7"
		 .split(' ') // ' ' 공백을 기준으로 string을 나누어 list로 바꿉니다. ["5", "6", "8", "1", "7"]
		 .map { it.toInt() } // list의 각 원소에 toInt()를 적용합니다. [5, 6, 8, 1, 7]
``` 

참고로 `!!` operator는 값이 null일 때 `NullPointerException`을 throw합니다.			 <br>
구글링을 통해 찾은 코드라 아직 왜 `!!` operator를 붙이는지는 정확하게는 모르겠지만,<br>
찾는다면 여기에 추가하도록 해야겠습니다.

몇 문제를 푼 소감은.. kotlin으로 PS를 하기 너무나 벅찬 느낌이 들었습니다.<br>
문제를 풀다가 조금이라도 막히면 C 혹은 python을 써서 문제를 풀어버릴까? 고민도 했답니다. (그렇게 해결한 문제도 사실 있습니다)<br>

아직 입출력도 버거워서 그렇다고 생각하고 있습니다! 앱 개발과 약간 거리가 있지만, 틈틈이 코틀린 활용을 해보려고 합니다.

아래에는 문제와 문제 해결에 사용한 코드가 있습니다. 혹시 궁금하면 펼쳐 살짝 읽어주시면 감사하겠습니다 ㅎㅎ

1330 [두 수 비교하기](https://www.acmicpc.net/problem/1330)
<details><summary>code</summary>

```kotlin
fun readInts() = readLine()!!.split(' ').map { it.toInt() }
 
fun main(args: Array<String>) {
    val (a, b) = readInts()
    if (a > b) {
        println('>')
    } else if (a < b){
        println('<')
    } else {
        println("==")
    }
}
```

</details>

---

2475 [검증수](https://www.acmicpc.net/problem/2475)

<details><summary>code</summary>

```kotlin
fun readInts() = readLine()!!.split(' ').map { it.toInt() }

fun main(args: Array<String>) {
     print((readInts().map { it * it }).sum() % 10)
}
```


</details>

---

2884 [알람 시계](https://www.acmicpc.net/problem/2884)
<details><summary>code</summary>

```kotlin
fun readInts() = readLine()!!.split(' ').map { it.toInt() }
 
fun main(args: Array<String>) {
    val (H, M) = readInts()
    var time = H * 60 + M - 45
    
    if (time < 0) {
        time += 60 * 24
    }
    
    println("${time/60} ${time%60}")
}
```
</details>

---

9012 [괄호](https://www.acmicpc.net/problem/9012)
<details><summary>code</summary>

```kotlin
fun main(args: Array<String>) {
    val T = readLine()!!.toInt()
    
    for (i in 1..T) {
        val string = readLine()!!
        var isVPS = true
        var depth = 0
        for (ch in string) {
            if (ch == '(')
                depth += 1
            else if(ch == ')')
                depth -= 1
            if (depth < 0)
                isVPS = false
        }
        if (isVPS && depth == 0)
            isVPS = true
        else if (depth != 0)
            isVPS = false
        
        println("${if (isVPS) "YES" else "NO"}")
    }
}
```
</details>

---

2798 [블랙잭](https://www.acmicpc.net/problem/2798)
<details><summary>code</summary>

```kotlin
fun readInt() = readLine()!!.split(" ").map { it.toInt() }
fun main(args: Array<String>) {
    val (_, sum) = readInt()
    val list = readInt()
    var output = -1

    for (n1 in list) {
        for (n2 in list) {
            for (n3 in list) {
                if (n1 != n2 && n2 != n3 && n1 != n3) {
                    if(n1 + n2 + n3 <= sum && n1 + n2 + n3 > output)
                        output = n1 + n2 + n3
                }
            }
        }
    }

    println(output)

}
```

</details>


